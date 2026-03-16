def hallucination_score(verification_results, consistency_score):

    evidence_conflict = 0

    for r in verification_results:

        if r == "CONTRADICTION":
            evidence_conflict += 1

        elif r == "NEUTRAL":
            evidence_conflict += 0.5

    if len(verification_results) > 0:
        evidence_conflict = evidence_conflict / len(verification_results)

    score = (
        0.6 * evidence_conflict +
        0.4 * (1 - consistency_score)
    )

    return score