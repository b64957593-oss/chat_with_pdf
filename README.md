# 📄 Chat with Your PDF
<img width="742" height="840" alt="image" src="https://github.com/user-attachments/assets/bb66da14-b8df-488e-ac16-f5d3e29404b2" />

https://chatwithpdf-pvzpspsjtuqgmsubuzsbyr.streamlit.app/

Upload a PDF and ask questions about it. The app splits the PDF into chunks, finds the most relevant ones using TF-IDF search, and sends them to an LLM (GROQ API ) to generate the answer 

## Tech
Python, Streamlit, pypdf, scikit-learn (TF-IDF + cosine similarity), GROQ API

## Run locally
1. Clone the repo
2. python -m pip install -r requirements.txt
3. GROQ_API_KEY= "your_key_here".
4. python -m streamlit run app.py

## How it works
PDF → text extraction → chunking → TF-IDF similarity search → top chunks + question → Claude → answer
