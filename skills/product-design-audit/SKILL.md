---
name: product-design-audit
description: Audit a digital product's UX and UI from an attached screenshot or mockup, including the user's own design. Use when asked what works, what to improve first, or whether a design revision addresses earlier findings. For feedback on how the reviewer wrote their own critique, use a critique coach instead.
---

# Product Design Audit

Review the interface directly. Help the designer decide what to keep, what to change first, and what evidence would tell them whether the change helped.

## Work from the screenshot

- A screenshot alone is enough to start. Identify the screen, visible state, and likely user task in one line. Use any task, platform, or design system the user supplies; otherwise state the assumption. If two plausible goals would change a recommendation, explain the difference and continue with the findings that apply to both.
- Review what matters for that task: next action, navigation and orientation, labels and copy, hierarchy and grouping, consistency of controls, visible feedback or recovery, and signs of accessibility barriers. Use only the lenses relevant to the screen. Identify specific strengths and why they help so the designer knows what to preserve.
- Anchor each finding to an exact label, component, region, or visible state. Separate the observation from its likely effect on the user. If the image is cropped or text is unreadable, say so; an element outside the frame is unverified. Continue with what is legible. If there is no image or none of it can be assessed, ask for a screenshot or a clearer crop.
- Treat a static image as evidence of appearance in the shown state. Put uncertain behavior, other screen sizes, keyboard and screen reader use, and unshown loading, error, or success states under **Verify** when they matter. Flag apparent contrast or target size risks and specify how to measure them in the design or implementation. Do not infer accessibility conformance, exact sizes from an unscaled image, or actual user outcomes.

## Return a usable audit

Lead with the main takeaway, then give **Keep**, **Improve first**, and **Verify** as applicable. For a single screen, start with up to three changes that would make the biggest difference. Rank by effect on the user’s task: a likely blocker or costly mistake comes before delay or hesitation, which comes before visual polish. Merge findings that share a fix and leave out filler.

For each change, connect the visible detail to the likely consequence, propose a specific adjustment or sample copy, and give a proportionate check if the effect is uncertain. If the adjustment depends on unseen behavior, state the condition. Use [the source guide](references/sources.md) to verify and link a relevant principle, pattern, or standard beside the finding it supports. Let the product’s own design system guide component changes when available. Treat outside design systems as examples unless they apply to this product.

When given a revised screenshot, compare the same task and state where possible. Say which earlier issues are visibly addressed, which remain, and whether the revision introduces a consequential tradeoff. Keep behavioral claims open until tested.
