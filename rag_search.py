from sentence_transformers import SentenceTransformer
import numpy as np
from chunk_store import chunks

model = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query):
    q_vec = model.encode(query)

    scores = []

    for chunk, vec in chunks:
        score = cosine_similarity(q_vec, vec)
        scores.append((chunk, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:2]