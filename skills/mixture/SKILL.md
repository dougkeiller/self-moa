---
name: mixture
description: Self mixture-of-agents for Claude Code - three independent Claude drafts written in parallel, then combined by Claude into one answer that shows where the drafts agree and disagree. Use when the user says "mixture", "MoA", "ask the panel", "get a few takes", "cross-check this", or for a high-stakes critique of a plan, target or claim where one draft's blind spot would be costly. Not for routine or factual questions.
---

# Mixture of drafts (Claude aggregates)

Three independent Claude answers to the same question (yours plus two fresh subagents), combined by you. No other providers, no API keys, nothing leaves Claude.

Why Claude-only: in blind tests (see `golden/` in this repo), three Claude drafts combined tied a panel that mixed in Gemini and GPT (4 wins each, 6 ties, two judges), and in a direct test beat a single Claude answer 9-0 with 5 ties (a small edge in detail, 7 questions). That matches the Self-MoA paper (Li et al., arXiv 2502.00674): mixing models often lowers average quality, while sampling the strongest model several times keeps quality and still adds variety.

## Steps
1. Write the full question to a prompt file in the scratchpad, with any context the drafters need: subagents can't see this conversation.
2. In one message, start two subagents (model: the strongest available, e.g. opus). Tell each to read only the prompt file, answer it on its own, and write the answer to `<out_dir>/draft2.md` / `draft3.md`.
3. While they run, write your own answer to `<out_dir>/draft1.md` BEFORE reading theirs, so it stays independent.
4. Read all three. If one failed or came back empty, say so and carry on with the rest.
5. Combine. Don't average or vote:
   - **Answer**: the best-supported conclusion, first.
   - **Agreement**: where all drafts agree. This is weak evidence on facts all three could get wrong together; say so where it matters.
   - **Disagreement**: each real split, and which side you trust and why.
   - **Raised once**: points only one draft raised, kept if sound.
   - Keep every core point of your own draft; the others' additions replace only weaker lines.
   - Mark which parts you checked and which rest on model output alone.

## When it pays
Best on critiquing a plan, target or claim (a savings target, a pilot result, a rollout proposal), where each draft notices different gaps. Little or no gain on questions with a checkable answer. Each run costs about three times a single answer, so don't run it on every message.
