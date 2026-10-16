from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
import requests

load_dotenv()

def find_relevant_chunks(user_question: str, chunks: List[str], top_n: int = 3) -> List[str]:
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([user_question] + chunks)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    top_indices = cosine_sim.argsort()[0][-top_n:][::-1]
    return [chunks[i] for i in top_indices]

def call_claude_api(prompt: str, context_chunks: List[str]) -> str:
    full_prompt = f"""
    **Context:**
    {chr(10).join([f"Chunk {i+1}: {chunk}" for i, chunk in enumerate(context_chunks)])}

    **Question:**
    {prompt}

    **Instructions:**
    - Sirf diye gaye context se jawab do.
    - Agar jawab nahi milta, "Sorry, I don't have enough information."
    """

    headers = {
        "Authorization": f"Bearer {os.getenv('CLAUDE_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": full_prompt,
        "max_tokens": 500
    }

    response = requests.post("https://api.claude.ai/v1/chat", json=data, headers=headers)
    return response.json().get("completion", "Sorry, I couldn't process your request.")