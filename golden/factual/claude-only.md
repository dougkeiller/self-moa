# Claude-only answers (Opus 5.5, written before reading any panel output)

q1: Mutable default argument: `items=[]` is created once, so every call without `items` appends to the same list. Use `items=None` and create the list inside.
q2: 22. The minute hand laps the hour hand 11 times every 12 hours.
q3: He didn't. The 1921 Nobel Prize in Physics was for his explanation of the photoelectric effect; relativity was considered too controversial.
q4: Not sound. The discount goes to everyone, including subscribers who would have stayed anyway, so you lose 40% on them. Revenue rises only if the churn saved outweighs that loss; you need break-even math and should target at-risk customers.
q5: About 9%. Of 100,000 people, ~99 true positives vs ~999 false positives.
q6: It becomes `rm -rf "/"`. GNU rm refuses by default (--preserve-root), but it's a real bug elsewhere and in variants like "$DIR"/*. Guard with "${DIR:?DIR unset}", set -u, or an explicit check.
q7: 6 (3 in strawberry, 3 in raspberry).
