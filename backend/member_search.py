# Semantic matching using Superteam's member DB
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_members(query: str, threshold=0.3):
    query_embed = model.encode(query)
    # Compare with precomputed member embeddings
    similarities = {
        member["name"]: np.dot(query_embed, member["embedding"])
        for member in members_db
    }
    best_match = max(similarities, key=similarities.get)
    return best_match if similarities[best_match] > threshold else "No match found."
