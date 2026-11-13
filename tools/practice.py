#!/usr/bin/env python3
"""Create Markdown practice sessions and attach compact screenshot copies."""

import argparse
import io
import re
import sys
from datetime import date
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required. See README.md for local installation steps.")


ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "practice"
MARKER = "<!-- screenshots -->"
PREFERRED_SIZE = 350 * 1024


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:70].rstrip("-")


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def compress(path, max_edge, lossless):
    with Image.open(path) as original:
        image = ImageOps.exif_transpose(original)
        profile = image.info.get("icc_profile")
        image = image.convert("RGBA" if image.has_transparency_data else "RGB")
        image.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)

        def encode(**options):
            buffer = io.BytesIO()
            image.save(buffer, "WEBP", method=6, icc_profile=profile, **options)
            return buffer.getvalue()

        data = encode(lossless=True)
        if not lossless and len(data) > PREFERRED_SIZE:
            for quality in (90, 84, 78):
                candidate = encode(quality=quality)
                if len(candidate) < len(data):
                    data = candidate
                if len(data) <= PREFERRED_SIZE:
                    break
        return data, image.size


def add_link(notes, label):
    if notes.count(MARKER) != 1:
        raise ValueError(f"Keep one {MARKER} marker in notes.md so screenshots can be linked.")
    alt = f"{label.replace('-', ' ').capitalize()} screenshot"
    return notes.replace(MARKER, f"![{alt}]({label}.webp)\n\n{MARKER}", 1)


def create_session(args):
    title = " ".join(args.title.split())
    if not title:
        raise ValueError("Enter a session title.")
    today = date.today().isoformat()
    name = f"{today}-{slug(title) or 'critique'}"
    notes = (ROOT / "templates" / "critique.md").read_text(encoding="utf-8")
    notes = notes.replace("{{date}}", today).replace("{{title}}", title)
    notes = add_link(notes, "before")
    data, size = compress(args.image, args.max_edge, args.lossless)

    SESSIONS.mkdir(exist_ok=True)
    for index in range(1, 1000):
        session = SESSIONS / (name if index == 1 else f"{name}-{index}")
        try:
            session.mkdir()
        except FileExistsError:
            continue
        break
    else:
        raise ValueError("Too many sessions share that name. Choose a different title.")

    write_screenshot(session, "before", notes, data, size)


def attach_screenshot(args):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+", args.session):
        raise ValueError("Use the session folder name printed by the new command.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.label):
        raise ValueError("Use a label like after, after-2, or detail.")
    session = SESSIONS / args.session
    if (session / f"{args.label}.webp").exists():
        raise ValueError("That label is already used. Choose another one, such as after-2.")
    notes = add_link((session / "notes.md").read_text(encoding="utf-8"), args.label)
    data, size = compress(args.image, args.max_edge, args.lossless)
    write_screenshot(session, args.label, notes, data, size)


def write_screenshot(session, label, notes, data, size):
    image_path = session / f"{label}.webp"
    notes_path = session / "notes.md"
    with image_path.open("xb") as image_file:
        image_file.write(data)
    notes_path.write_text(notes, encoding="utf-8")
    print(f"Screenshot: {image_path.name} ({size[0]} × {size[1]}, {len(data) / 1024:.1f} KiB)")
    print(f"Session:    {session.name}")
    print(f"Notes:      {notes_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    new = subcommands.add_parser("new", help="start a session with a before image")
    new.add_argument("title")
    new.set_defaults(action=create_session)
    attach = subcommands.add_parser("attach", help="add a revision or close-up")
    attach.add_argument("session", help="session folder name")
    attach.add_argument("label", help="for example after, after-2, or detail")
    attach.set_defaults(action=attach_screenshot)
    for command in (new, attach):
        command.add_argument("image", type=Path)
        command.add_argument("--max-edge", type=positive_int, default=1800)
        command.add_argument("--lossless", action="store_true", help="keep pixels exact after resizing")

    args = parser.parse_args()
    try:
        args.action(args)
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        parser.exit(1, f"Could not save screenshot: {error}\n")


if __name__ == "__main__":
    main()
