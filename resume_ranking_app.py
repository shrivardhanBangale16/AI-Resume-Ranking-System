
import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set background image using custom CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://img.freepik.com/premium-vector/abstract-background-technology-hud-head-up-display-frame_35887-268.jpg?w=740");
        background-attachment: fixed;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def rank_resumes(job_description, resumes):
    # Combine job description with resumes
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()

    return cosine_similarities

# Streamlit app
st.title("AI Resume Ranking System")
st.write("Empowering recruiters with AI-driven resume screening and candidate ranking for faster, smarter hiring decisions.")

# Job description input
st.header("Job Description")
job_description= st.text_area ("Enter the job description")

# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)


if uploaded_files and job_description:
    st.header("Ranking Resumes")

    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

    # Rank resumes
    scores = rank_resumes(job_description, resumes)

    # Display scores
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores })
    results = results.sort_values(by="Score", ascending=False)

    st.write(results)






