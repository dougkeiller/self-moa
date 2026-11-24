# Claude-only control vs mixed panel, 2026-11-23

Question: does the mixed panel's gain come from other labs, or just from having more drafts?
- Claude-only ("Self-MoA"): three independent Opus 5.5 drafts (baseline, claude2, claude3), combined by a fresh Opus 5.5 under the identical combiner instructions and 350-word cap.
- Mixed: the earlier combination of the Opus baseline + Gemini 4 Neon + GPT-6.2 Sol (aggregated/).
- Judges: Qwen4 Max and Sonnet 5.5, blind A/B, new shuffle (judge2/key.json).

| Q | Qwen judge | Sonnet judge |
|---|---|---|
| o1 SG&A target | tie | mixed |
| o2 Onboarding | mixed | tie |
| o3 AI scribe | Claude-only | mixed |
| o4 Remote work | mixed | tie |
| o5 Internship | Claude-only | tie |
| o6 Pilot 40% | Claude-only | Claude-only |
| o7 Donor data | tie | tie |

Totals across both judges (14 verdicts): Claude-only 4, mixed 4, tie 6. The judges agree on only two questions: o6 (Claude-only) and o7 (tie).

Finding: no measurable advantage from adding other labs. The earlier mixed-panel win over a single Claude answer is matched by three Claude drafts combined. On o6, where the mixed panel beat a single Claude answer in round 1, three Claude drafts now beat the mixed panel, so that gain came from more drafts, not from different models. This matches the Self-MoA paper (arXiv 2502.00674).
Caveats: one run, 7 questions, two judges; rubric still near ceiling (5-6 of 6 for every answer).
