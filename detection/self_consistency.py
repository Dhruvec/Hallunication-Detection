from collections import Counter


def compute_consistency(answers):

    normalized = [a.lower().strip() for a in answers]

    counts = Counter(normalized)

    most_common = counts.most_common(1)[0][1]

    score = most_common / len(answers)

    return score