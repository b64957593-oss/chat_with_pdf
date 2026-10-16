# 📄 Chat with Your PDF
<img width="914" height="962" alt="image" src="https://github.com/user-attachments/assets/23388e00-431c-4f37-a7ad-828f16c320c5" />


Upload a PDF and ask questions about it. The app splits the PDF into chunks, finds the most relevant ones using TF-IDF search, and sends them to an LLM (GROQ API ) to generate the answer 

## Tech
Python, Streamlit, pypdf, scikit-learn (TF-IDF + cosine similarity), GROQ API

## Run locally
1. Clone the repo
2. python -m pip install -r requirements.txt
3. GROQ_API_KEY=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
4. python -m streamlit run app.py

## How it works
PDF → text extraction → chunking → TF-IDF similarity search → top chunks + question → Claude → answer
