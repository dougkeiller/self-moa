# Golden set: expected answers (written before any model ran, 2026-11-23)
q1: Mutable default argument; the same list is shared across calls, so items pile up. Fix: items=None.
q2: 22 (hands overlap every 12/11 hours; 11 per 12 hours).
q3: False premise. He won the 1921 prize for the photoelectric effect (law of), not relativity.
q4: Flawed. A 40% discount to ALL monthly subscribers gives it to those who'd never churn (cannibalization); revenue only rises if retained revenue beats the discount; needs break-even math / targeting.
q5: About 9% (~0.99*0.001 / (0.99*0.001 + 0.01*0.999) = ~0.09).
q6: Expands to rm -rf "/" ; modern GNU rm refuses "/" by default (--preserve-root), but it's still a bug (other rm's, or "$DIR/*" variants, would wipe the system). Guard: "${DIR:?}" or set -u, or test -n.
q7: 6 (strawberry 3, raspberry 3).
