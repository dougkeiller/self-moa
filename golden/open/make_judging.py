import json, pathlib, random
d = pathlib.Path(__file__).parent
random.seed(20261123)
rubric = (d/"rubric.md").read_text()
key = {}
(d/"judge").mkdir(exist_ok=True)
for i in range(1, 8):
    q = f"o{i}"
    pair = [("baseline", (d/"baseline"/f"{q}.md").read_text()), ("mixture", (d/"aggregated"/f"{q}.md").read_text())]
    random.shuffle(pair)
    key[q] = {"A": pair[0][0], "B": pair[1][0]}
    prompt = f"""You are a strict, impartial grader. Score two answers to the same question against the rubric for this question.
Rubric rules and all rubrics:
{rubric}

Grade ONLY question {q}.
QUESTION:
{(d/'prompts'/f'{q}.md').read_text()}
ANSWER A:
{pair[0][1]}
ANSWER B:
{pair[1][1]}

Reply in exactly this format and nothing else:
A_points: <list rubric letters covered>
A_penalties: <number and reason, or 0>
A_score: <number>
B_points: <list>
B_penalties: <number and reason, or 0>
B_score: <number>
Better: <A, B, or tie>
Off-rubric value: <one line: anything valuable in either answer not on the rubric>
"""
    (d/"judge"/f"{q}.prompt.md").write_text(prompt)
(d/"judge"/"key.json").write_text(json.dumps(key, indent=1))
print("ok")
