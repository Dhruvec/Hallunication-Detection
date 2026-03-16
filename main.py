from generator.groq_generator import generate_multiple_answers
from claims.claim_extractor import extract_claims
from retrieval.retrieve import retrieve_evidence
from verification.verify_claim import verify_claim
from detection.self_consistency import compute_consistency
from detection.hallucination_score import hallucination_score
from correction.correct_answer import correct_answer

question = input("Enter a question: ")

# 1 generate multiple answers
answers = generate_multiple_answers(question, n=3)

print("\nGenerated Answers:")
for a in answers:
    print("-", a)

# 2 compute consistency
consistency = compute_consistency(answers)

print("\nSelf Consistency Score:", consistency)

# use first answer for claim verification
claims = extract_claims(answers[0])

verification_results = []

for claim in claims:

    evidence_list = retrieve_evidence(claim)

    for evidence in evidence_list:

        result = verify_claim(claim, evidence)

        verification_results.append(result)

# 3 hallucination score
score = hallucination_score(verification_results, consistency)

print("\nHallucination Score:", score)

# 4 correction
if score > 0.5:

    evidence = retrieve_evidence(question)[0]

    corrected = correct_answer(question, evidence)

    print("\nCorrected Answer:\n", corrected)