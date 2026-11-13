# Coach rubric

Use this rubric when reviewing a screenshot or giving a reviewer feedback on their own critique.

## Before giving feedback

- Start with the intended user, their immediate task, and the screen state. If the task is missing, state a reasonable assumption and keep the findings conditional on it.
- Scan the screen for hierarchy and grouping, readability, visible controls and states, and whether labels set the right expectation. Apply the product’s design system and platform conventions when known.
- Give one strength to preserve and up to three findings, ordered by impact on the task. Treat preference as a design choice unless you can explain its effect on the goal.

## For each finding

Use **location and visible evidence → likely impact on the task → change to try or check to run**. Quote a visible label or name a region someone can find. Explain the relevant design principle in plain language.

- **Visible:** Say what the screenshot shows. For example, “The total and the delivery estimate have the same weight.”
- **Inferred:** Use conditional language when predicting an effect. For example, “Shoppers scanning for their total may have to read both rows.”
- **Needs a check:** Name the evidence that would settle it. Use the source design or live page for contrast and hit area measurements, a working interface for keyboard or screen reader behaviour, and a user task for claims about what people understand or do. Don’t declare a whole product accessible or inaccessible from one image.

## Reviewer feedback

Use this mode when the reviewer shares their own comments. Read the screenshot, the intended task, and the comments together. Choose one comment to work on, ideally the one with the most room to improve on a finding that matters to the user’s task. Score that comment using the four criteria below. Base each score on a phrase the reviewer wrote or a specific detail they could add. If the screenshot or task is unavailable, say what you could assess and mark any affected criterion as **unscored**.

| Criterion | 0 · Missing | 1 · Partial | 2 · Clear |
| --- | --- | --- | --- |
| **Evidence** | Gives an impression without a visible detail. | Points to the area or names a detail. | Names both the location and a visible detail the designer can find. |
| **Reasoning** | Gives a verdict or a fix without saying why it matters. | Names a likely effect or the user’s goal but leaves the connection implicit. | Explains how the observed detail could help or hinder the task and qualifies any untested prediction. |
| **Communication** | Leaves the main point unclear or makes it personal. | States the main point but blends the observation, interpretation, or request. | Makes the point clear in plain, respectful language and distinguishes what was seen from what was inferred. |
| **Next step** | Gives the designer nothing concrete to try or verify. | Suggests a broad direction. | Gives a specific change, a question that would resolve the uncertainty, or a check tied to the finding. |

Return one strength to keep, the four scores with brief reasons, and one rewrite challenge focused on the most useful improvement. If several comments share a pattern, mention it briefly while keeping the score attached to the selected comment. Let the reviewer attempt the rewrite before showing a model answer, unless they ask for one. When they reply, score the rewrite against the same screenshot, task, and criteria. Show what changed and give one thing to practise on the next screen. Use the total out of 8 as an optional personal benchmark when all criteria are scored. Compare first draft with rewrite on the same comment, and use the next screen to see whether the habit carries over.

### Worked example

On a checkout screen with a bottom button labelled “Continue,” the reviewer writes, “The Continue button is confusing. Make it bigger.”

- **Keep** the exact button label. The designer can tell which control you mean.
- **Evidence 1/2.** You named the label. Add where it appears.
- **Reasoning 0/2.** “Confusing” leaves out what the shopper might misunderstand and why.
- **Communication 1/2.** The point is brief. Separate the visible label from your prediction about how shoppers might read it.
- **Next step 1/2.** “Make it bigger” gives a direction. Checking whether the button opens a review step or places the order would address the uncertainty about its label.
- **Rewrite challenge.** In two sentences, name where the button is, explain the two outcomes a shopper might expect, and ask a question that would tell you which label fits.

## References

- [NN/g: Design Critiques](https://www.nngroup.com/articles/design-critiques/) for feedback tied to goals.
- [NN/g: Principles of Visual Design](https://www.nngroup.com/articles/principles-visual-design/) and [Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) for reviewing visible design choices.
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/) for web accessibility criteria.
- [GOV.UK: Moderated Usability Testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) for testing assumptions with users.

## Change log

| Date | Rule added or revised | Evidence from practice | Result when tried again |
| --- | --- | --- | --- |
| 2026-11-13 | Start with screenshot evidence, explain the likely effect, and say what would verify it. | Baseline from the references above. | To be tested in practice. |
| 2026-11-13 | Score one reviewer comment on four criteria and use the same criteria on the rewrite. | Added to give the reviewer feedback on their reasoning and communication. | To be tested with a practice session. |
