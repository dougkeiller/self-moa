# self-moa

A mixture-of-agents skill for Claude Code that uses **only Claude**. Claude writes an answer, two subagents write theirs independently in parallel, and Claude combines the three into one answer: the best-supported conclusion first, then where the drafts agree, where they split, and points only one draft raised.

## Why Claude only

Most MoA setups mix models from several labs. In blind tests here, that bought nothing over three Claude drafts:

| Comparison (7 open-ended questions, two blind judges) | Result |
|---|---|
| Mixed panel (Claude + Gemini 4 Neon + GPT-6.2 Sol) vs one Claude answer | mixed panel preferred on 3, single on 1, rest split/tie |
| Three Claude drafts combined vs one Claude answer (direct test) | three drafts 9, tie 5, single 0 of 14 verdicts; judges agree on 3 of 7. Rubric scores mostly equal: a small, consistent edge from sharper detail |
| Three Claude drafts vs the mixed panel | 4 wins each, 6 ties out of 14 verdicts |

The gain over a single answer came from having more drafts, not from other labs. On 7 factual questions with checkable answers, every model already scored 7/7, so there was nothing to gain. This matches the published research: [Self-MoA](https://arxiv.org/abs/2502.00674) found sampling the top model several times beats mixing models in most settings, and a [67-model study](https://arxiv.org/abs/2606.27288) found combining models "rarely beats the single best model" on checkable tasks.

Claude-only also means no extra API keys, and no content sent to other providers.

Caveats: one run, 7 questions per set, two judges (Qwen4 Max and Sonnet 5.5), and rubric scores near the ceiling. Treat the result as "no detectable gain from other labs", not proof. Everything needed to rerun the tests is in `golden/`.

## Install

```
claude plugin marketplace add dougkeiller/self-moa
claude plugin install self-moa@self-moa
```

Or copy `plugin/skills/mixture/` into `~/.claude/skills/`.

## Use

Say "mixture", "MoA", "ask the panel" or "get a few takes" on a question worth it: critiquing a plan, a target, a pilot result or a proposal. It costs about three times a single answer, so it isn't meant for every message.

## Golden tests

- `golden/factual/`: 7 questions with known answers, expected answers, results.
- `golden/open/`: 7 open-ended judgement questions, the rubric (written before any model ran), the blind A/B judging scripts, and both result write-ups.

## License

MIT
