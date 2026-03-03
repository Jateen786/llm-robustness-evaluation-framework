from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts):
    return model.encode(texts)

def compute_similarity(texts):
    embeddings = get_embeddings(texts)
    similarity_matrix = cosine_similarity(embeddings)
    return similarity_matrix

def detect_novel_prompt(new_prompt, existing_prompts, threshold=0.85):
    all_prompts = existing_prompts + [new_prompt]
    similarity_matrix = compute_similarity(all_prompts)

    new_prompt_similarities = similarity_matrix[-1][:-1]

    max_similarity = np.max(new_prompt_similarities)

    if max_similarity > threshold:
        return False, max_similarity
    else:
        return True, max_similarity
