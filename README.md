# Product Design Critique Coach

Product Design Critique Coach is a portable [Agent Skill](https://agentskills.io/specification) for reviewing the UX and UI of digital products. Use it with a screenshot, a mockup, or a sequence of screens from a flow such as onboarding, checkout, or settings.

- **Critique a product screen or flow.** Share the user’s task and the relevant screens. Review navigation, interaction states, hierarchy, labels, and accessibility through the parts that affect that task.
- **Improve your critique.** Share your own comments. Get feedback on your evidence, reasoning, communication, and next step. Rewrite one comment and compare it with your first draft.
- **Learn the principles behind the feedback.** Use the source guide for terms, citations, and short exercises you can try on another screen. [Sources and practice examples](skills/product-design-critique-coach/references/source-guide.md)
- **Keep a practice log.** Save your comments and revisions in Markdown, with compressed WebP copies of the screenshots alongside your notes.

## Install with one command

With Node.js installed, run this from the project where you want to use the coach:

```sh
npx skills add tawfikmanham/product-design-critique-coach
```

The [Vercel Skills CLI](https://github.com/vercel-labs/skills) fetches the skill and its references from GitHub. Choose your agent if prompted, or specify one with `--agent codex`, `--agent claude-code`, or `--agent cursor`. Add `--global` to make the skill available across your local projects.

After installing, open your agent and ask it to use **Product Design Critique Coach** with a screenshot and the user’s task.

## Manual install and other agents

The entire skill lives in [`skills/product-design-critique-coach/`](skills/product-design-critique-coach/). Keep `SKILL.md` and its `references/` folder together. The coaching instructions require no Python, Node.js, or npm.

For local agents, copy the whole `product-design-critique-coach` folder into one of these directories.

| Agent | User-level skill directory |
| --- | --- |
| Codex | `~/.agents/skills/` ([docs](https://developers.openai.com/api/reference/cli#use-the-cli-from-a-coding-agent)) |
| Claude Code | `~/.claude/skills/` ([docs](https://code.claude.com/docs/en/skills)) |
| Cursor | `~/.cursor/skills/` or `~/.agents/skills/` ([docs](https://cursor.com/docs/skills)) |
| Grok Build | `~/.grok/skills/` or `~/.agents/skills/` ([docs](https://docs.x.ai/build/features/skills-plugins-marketplaces)) |

For Claude on the web or in the desktop app, zip the `product-design-critique-coach` folder and upload it as a custom skill. For Grok Bot, share the skill instructions, rubric, and source guide and ask the Bot to save the workflow as a private skill. [Claude custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Grok Bot skills](https://docs.x.ai/grok-bot/skills-routines-and-automations)

In a session that accepts images, attach a screenshot and ask:

> Use Product Design Critique Coach to coach me on this critique. The shopper is trying to check their order before paying. My comment is “The Continue button is confusing. Make it bigger.”

If you installed the earlier version, replace the old `design-critique-coach` folder with `product-design-critique-coach`. Where your agent uses a command to invoke the skill, use the new name.

If you’re building your own agent, load the [skill instructions](skills/product-design-critique-coach/SKILL.md) when the user asks for a critique. Make the [rubric](skills/product-design-critique-coach/references/coach-rubric.md) and [source guide](skills/product-design-critique-coach/references/source-guide.md) available, then pass the screenshot to an image-capable model along with the user’s task and comments. In a chat app without skill installation, attach or paste those three Markdown files as instructions.

The skill ships through GitHub. The `npx` command runs the shared installer. A Node.js agent can also read the Markdown files directly.

## Start a practice session

You can log a session by hand with the [Markdown template](templates/critique.md). The optional command-line helper uses Python and Pillow to compress screenshots and link them in your notes. From this project folder, with Python 3 and Pillow installed:

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
