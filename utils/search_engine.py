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

def call_claude_api(user_question, relevant_chunks):
    context = "\n\n".join(relevant_chunks)
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-oss-120b",
            "messages": [{
                "role": "user",
                "content": f"Answer using only this context:\n\n{context}\n\nQuestion: {user_question}",
            }],
        },
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]