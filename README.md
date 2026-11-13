# Design Critique Coach

Practise giving design feedback that explains what you see, why it matters, and what to try next. Design Critique Coach is a Codex skill for designers and anyone who reviews digital interfaces.

- **Critique a screen.** Share a screenshot and the user’s task. Get findings grounded in visible details and checks for claims that need a prototype or a user test.
- **Improve your critique.** Share your own comments. Get feedback on your evidence, reasoning, communication, and next step. Rewrite one comment and compare it with your first draft.
- **Keep a practice log.** Save your comments and revisions in Markdown, with compressed WebP copies of the screenshots alongside your notes.

## Use the skill in Codex

Open this repository in Codex and ask for a screen critique or reviewer coaching. The repository instructions point Codex to the skill.

To use the skill in another project, run the following from the root of this repository:

```sh
mkdir -p ~/.agents/skills
cp -R skills/design-critique-coach ~/.agents/skills/
```

Open a new Codex chat, attach a screenshot, and try:

> Use $design-critique-coach to coach me on this critique. The shopper is trying to check their order before paying. My comment is “The Continue button is confusing. Make it bigger.”

The [skill instructions](skills/design-critique-coach/SKILL.md) and [reviewer scorecard](skills/design-critique-coach/references/coach-rubric.md#reviewer-feedback) can also be read directly. See [OpenAI’s skill installation guidance](https://developers.openai.com/api/reference/cli#use-the-cli-from-a-coding-agent) for the supported folders.

## Start a practice session

The log is optional. From this project folder, with Python 3 and Pillow installed:

```sh
python3 tools/practice.py new "Checkout button" "/path/to/before.png"
```

The command prints the path to a new `notes.md` in `practice/`. Open it in a Markdown viewer to see the screenshot beside your notes. Add the user, task, and screen state, then write your own critique before asking the coach.

## Get feedback on your critique

Share the screenshot, the user’s task, and your comments in this workspace and ask:

> Coach me on my critique. Pick one comment and tell me how well I grounded it in the screenshot, explained my reasoning, and gave the designer a useful next step. Give me one rewrite challenge, then assess my rewrite against the same criteria.

Log both attempts in the **Reviewer feedback** section of your notes. Each criterion earns up to two points. Try improving one criterion on the same comment, then practise that skill on a different screen. The scores help you spot what to work on. [Reviewer scorecard and worked example](COACH-RUBRIC.md#reviewer-feedback)

If you also want the coach’s independent take on the design, share the screenshot and task before revealing your comments and ask for a screen critique.

## Attach a design revision

After making a revision, use the session folder name printed by the first command:

```sh
python3 tools/practice.py attach YYYY-MM-DD-checkout-button after "/path/to/after.png"
```

The helper stores a WebP beside the notes and links to it. It leaves the original where it is. By default it caps the longest edge at 1,800 pixels, using lossless compression for small files and trying high-quality compression for larger ones. If the text is hard to read, add a close-up as `detail` or use `--lossless --max-edge 3000` when adding the image. You can also [copy the template](templates/critique.md) and link your images by hand.

If `python3 -c 'import PIL'` fails, install the dependency in a local environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install Pillow
```

Then use `.venv/bin/python` in the commands above.

Git ignores `practice/` so your screenshots and notes stay local by default.

## Close the feedback loop

1. **Compare.** Read your first comment alongside your rewrite. Could another designer locate the issue, explain why it matters, and decide what to do? If you asked for an independent screen critique, also record where you and the coach agreed or missed something.
2. **Revise and check.** Make one change and attach the new screenshot. Record what visibly changed. When the claim is about behaviour, use an interactive prototype or a live page. If you want to know whether people hesitate or succeed, watch representative users try the task. Record how you checked and leave untested claims open.
3. **Refine the rubric.** When a pattern repeats or you find a clear error, add a specific rule and log the reason in [the rubric’s change log](COACH-RUBRIC.md#change-log). Try it on a new screenshot and an earlier case to check that it helps without weakening other feedback.

For example, suppose you wrote “Make Continue more prominent” and the coach pointed out that the label could mean either “review” or “submit.” Check the actual action first. If it opens a review step, try “Review order,” then ask someone to say what they expect to happen before clicking. The screenshot can confirm the new wording; their response gives you evidence about what it communicates.
