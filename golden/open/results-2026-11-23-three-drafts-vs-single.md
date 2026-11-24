# Three combined Claude drafts vs one Claude answer (2026-11-23)

Direct test the earlier rounds skipped. Same 7 open questions, rubric, 350-word cap. Baseline = single blind Opus answer; selfmoa = three Opus drafts combined by a fresh Opus. Blind A/B, seed 777, key in judge3/key.json.

| Judge | Three drafts win | Tie | Single wins |
|---|---|---|---|
| Qwen4 Max | 6 | 1 | 0 |
| Sonnet 5.5 | 3 | 4 | 0 |
| Total (14) | 9 | 5 | 0 |

Both judges agree on o3, o4, o6 (three drafts). Single answer never won.

Caveat: rubric scores were equal on 6/7 questions for both judges (only Qwen o3 differs, 6 vs 5). Wins come from tie-breaks on specificity (named studies, control group, language access), not missed rubric points. So: consistent small edge, not a large one. 7 questions, LLM judges, no human grading.
