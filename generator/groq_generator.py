import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


def generate_answer(question, temperature=0.2):

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model=MODEL,
        temperature=temperature
    )

    return chat.choices[0].message.content


def generate_multiple_answers(question, n=3):

    answers = []

    for _ in range(n):
        answer = generate_answer(question, temperature=0.7)
        answers.append(answer)

    return answers