import streamlit as st

from generator.groq_generator import generate_multiple_answers
from claims.claim_extractor import extract_claims
from retrieval.retrieve import retrieve_evidence
from verification.verify_claim import verify_claim
from detection.self_consistency import compute_consistency
from detection.hallucination_score import hallucination_score
from correction.correct_answer import correct_answer


st.title("LLM Hallucination Detection System")

st.write(
    "This system verifies LLM answers using Wikipedia evidence and detects hallucinations."
)

question = st.text_input("Enter your question:")

if st.button("Run Verification"):

    if question:

        st.subheader("Generated Answers")

        answers = generate_multiple_answers(question, n=3)

        for a in answers:
            st.write(a)

        consistency = compute_consistency(answers)

        st.subheader("Self Consistency Score")

        st.write(consistency)

        claims = extract_claims(answers[0])

        st.subheader("Extracted Claims")

        for c in claims:
            st.write(c)

        verification_results = []

        st.subheader("Evidence Retrieval & Verification")

        for claim in claims:

            evidence_list = retrieve_evidence(claim)

            for evidence in evidence_list:

                label = verify_claim(claim, evidence)

                verification_results.append(label)

                st.write("Claim:", claim)
                st.write("Evidence:", evidence)
                st.write("Verification:", label)
                st.write("---")

        score = hallucination_score(verification_results, consistency)

        st.subheader("Hallucination Score")

        st.write(score)

        if score > 0.5:

            st.subheader("Corrected Answer")

            evidence = retrieve_evidence(question)[0]

            corrected = correct_answer(question, evidence)

            st.write(corrected)

    else:

        st.warning("Please enter a question.")