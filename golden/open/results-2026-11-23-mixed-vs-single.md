# Mixture golden test, open-ended set, 2026-11-23

Design: 7 ambiguous, judgement-heavy questions (prompts/), rubric written first (rubric.md).
- Baseline: fresh Opus 5.5 helper, never saw rubric.
- Mixture: panel (Gemini 4 Neon, GPT-6.2 Sol) + baseline, combined by a second fresh Opus 5.5 helper under the skill's rules. Same 350-word cap as baseline, so length can't win.
- Judges, blind A/B with randomized order (judge/key.json): Qwen4 Max (not on the panel) and Sonnet 5.5.

| Q | Topic | Qwen judge | Sonnet judge | Both agree |
|---|---|---|---|---|
| o1 | PE 15% SG&A target | mixture | mixture | **mixture** |
| o2 | "Make onboarding better" | mixture | mixture | **mixture** |
| o3 | AI scribe, California | baseline | baseline | **baseline** |
| o4 | Remote work productivity | baseline | mixture | split |
| o5 | Internship choice | baseline | tie | split |
| o6 | Pilot 40% extrapolation | mixture | mixture | **mixture** |
| o7 | Donor data into AI tool | tie | tie | tie |

Totals: Qwen 3 mixture / 3 baseline / 1 tie. Sonnet 4 / 1 / 2. Both judges agree: mixture better on 3, baseline on 1.
Rubric scores were near ceiling for both (5-6 of 6), so the preferences rest mostly on off-rubric content.

What the mixture added that judges valued: in-year vs run-rate savings and double counting (o1); "nobody owns onboarding" hypothesis (o2); random assignment and checking the spread of a 12-person average (o6); kill criteria and a flag on California AB 3030 (o3, unverified).
Where it lost: o3. Under the 350-word cap the combined answer dropped the baseline's point about note accuracy and liability to make room for panel additions.
Aggregation also filtered: it dropped GPT's recalled lawsuit and acceptance figure as unverified, and rejected Gemini's "fully remote cuts productivity 10-20%".

Verdict against the pre-set kill criterion (beat Claude on about half, or catch something Claude got wrong): BORDERLINE PASS. Better on 3 of 7 by both judges (4 of 7 by one), worse on 1, and it caught decision-useful gaps Claude missed on plan-critique questions. Not a clear win on contested-evidence or personal-choice questions.
Caveats: one run, n=7, two judges, rubric near ceiling.
Change made from this: skill now tells the aggregator to keep every core point of its own answer and let panel additions replace only weaker lines (fixes the o3 loss).
