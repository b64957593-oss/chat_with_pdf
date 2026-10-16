# 📄 Chat with Your PDF

Upload a PDF and ask questions about it. The app splits the PDF into chunks, finds the most relevant ones using TF-IDF search, and sends them to Claude to generate the answer.

## Tech
Python, Streamlit, pypdf, scikit-learn (TF-IDF + cosine similarity), Claude API

## Run locally
1. Clone the repo
2. python -m pip install -r requirements.txt
3. Create a .env file and add your API key
4. python -m streamlit run app.py

## How it works
PDF → text extraction → chunking → TF-IDF similarity search → top chunks + question → Claude → answer
