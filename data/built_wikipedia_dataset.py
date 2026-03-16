import wikipedia
import json

topics = [
    "Telephone",
    "Albert Einstein",
    "Isaac Newton",
    "World War II",
    "Artificial Intelligence",
    "Quantum mechanics"
]

passages = []

for topic in topics:
    page = wikipedia.page(topic)
    text = page.content.split("\n")

    for paragraph in text:
        if len(paragraph) > 100:
            passages.append(paragraph)

with open("data/wiki_passages.json","w") as f:
    json.dump(passages,f)

print("Collected", len(passages), "passages")