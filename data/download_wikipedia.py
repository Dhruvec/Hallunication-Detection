import wikipediaapi
import json
from tqdm import tqdm

wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='llm-hallucination-detector (dhruv-project)',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

topics = [
    "Artificial intelligence",
    "Quantum mechanics",
    "Telephone",
    "Albert Einstein",
    "Isaac Newton",
    "World War II",
    "Computer science",
    "Machine learning",
    "Deep learning",
    "Neural network"
]

passages = []

for topic in tqdm(topics):

    page = wiki.page(topic)

    if page.exists():

        text = page.text.split("\n")

        for paragraph in text:

            if len(paragraph) > 100:
                passages.append(paragraph)

print("Total passages:", len(passages))

with open("data/wiki_passages.json", "w", encoding="utf-8") as f:
    json.dump(passages, f)