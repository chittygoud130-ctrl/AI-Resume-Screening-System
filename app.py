import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening System")

job_description = st.text_area("Enter Job Description")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file and job_description:
    pdf = PdfReader(uploaded_file)
    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(documents)

    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100

    st.success(f"Resume Match Score: {score:.2f}%")