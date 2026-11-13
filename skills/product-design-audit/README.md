# Product Design Audit

Attach a screenshot or mockup to get direct feedback on a product screen. The audit identifies details worth keeping, ranks the changes that would help the user's task, and flags what to verify in a prototype or live product.

## Install and try it

```sh
npx skills add tawfikmanham/product-design-critique-coach
```

Choose `product-design-audit` and select Codex or the agent you use.

Attach a screenshot in Codex and send this prompt.

> Use $product-design-audit to review this screenshot. Tell me what to keep, what to improve first, and what to verify.

A screenshot is enough to start. Add the user's task or your design system if you have it. After a revision, share the updated screenshot and ask which findings it addresses.

## Example: a checkout screen

Imagine a checkout screenshot with an order summary and a primary button labelled **Continue**. The shopper wants to review the order before paying.

- **Keep** the item list and total together so shoppers can check what they are paying for.
- **Improve first** by clarifying what **Continue** does. If it opens a review step, try **Review order** so shoppers can predict what happens next. [U.S. Web Design System button guidance](https://designsystem.digital.gov/components/button/#usability-guidance)
- **Verify** the button's destination in the prototype. Ask a shopper what they expect before they press it.

[Read the skill instructions](SKILL.md) · [Browse the audit sources](references/sources.md) · [See both skills](../../README.md)
