from generator.groq_generator import generate_answer

def correct_answer(question, evidence):

    prompt = f"""
Question: {question}

Evidence:
{evidence}

Generate a correct answer using the evidence.
"""

    corrected = generate_answer(prompt)

    return corrected