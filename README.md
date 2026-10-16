# 📄 Chat with Your PDF
Chat with Your PDF

Upload a PDF

FinGuar ..._ 2Page.pdf
276.3KB

+

Ask a question about the PDF:

tell me about this pdf and also tell me members name which is mention in this pdf

Answer:

Based on the text you provided, the "PDF" appears to be a pitch-deck or idea-submission document for
FG FinGuard Al - Your Financial Protection Assistant (Round 01).
It outlines the problem (complex financial documents, suspicious return claims, missed actions) and
proposes a solution that guides users through four safeguards:

1. Simplify - translate documents into plain language.
2. Detect - flag suspicious claims and inconsistencies.
3. Identify - surface missing information that needs verification.
4. Remind - track important actions and deadlines.

The document also lists a suggested MVP tech stack (React + Tailwind, FastAPI, OCR+LLM APIs,
Supabase/Render) and the expected real-world value (clearer understanding, earlier scam awareness,
fewer missed actions, more confidence).

Members named in the document

. Yuvraj Patel - Team Lead (appears multiple times, e.g., "THE CARTEL 2.0 / YUVRAJ PATEL
(TEAM LEAD)").
. Shripad Patnaik - listed alongside Yuvraj Patel (e.g., "/ SHRIPAD PATNAIK").

No other individual names are mentioned in the supplied text.

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
