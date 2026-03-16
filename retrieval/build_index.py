import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/wiki_passages.json", encoding="utf-8") as f:
    passages = json.load(f)

print("Encoding passages...")

embeddings = []

for passage in tqdm(passages):

    emb = model.encode(passage)

    embeddings.append(emb)

embeddings = np.array(embeddings)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "data/wiki_index.faiss")

print("Index built with", len(passages), "passages")