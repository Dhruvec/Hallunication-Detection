import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("data/wiki_index.faiss")

with open("data/wiki_passages.json", encoding="utf-8") as f:
    passages = json.load(f)


def retrieve_evidence(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []

    for idx in indices[0]:

        results.append(passages[idx])

    return results