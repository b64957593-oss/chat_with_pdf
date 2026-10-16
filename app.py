import streamlit as st
from utils.pdf_processor import extract_text_from_pdf, split_into_chunks
from utils.search_engine import find_relevant_chunks, call_claude_api

st.title("📄 Chat with Your PDF")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        chunks = split_into_chunks(text)

    user_question = st.text_input("Ask a question about the PDF:")

    if user_question:
        with st.spinner("Finding answers..."):
            relevant_chunks = find_relevant_chunks(user_question, chunks)
            answer = call_claude_api(user_question, relevant_chunks)
            st.success("**Answer:**")
            st.write(answer)