
# 🧠 AI Resume Ranking System

Welcome to the **AI Resume Ranking System** – an intelligent and user-friendly Streamlit web app that allows recruiters and hiring teams to **screen and rank resumes** based on a job description using **Natural Language Processing (NLP)** and **TF-IDF based cosine similarity**.

---

## 🚀 Features

- 📄 Upload multiple **PDF resumes**
- 📝 Enter a **job description** inline
- 🧠 Uses **TF-IDF** + **cosine similarity** to evaluate resume relevance
- 📊 Automatically **ranks candidates** based on JD matching score
- 🌐 Intuitive **Streamlit UI** with a sleek tech-themed background

---

## 🎯 Use Case

Ideal for:
- HR professionals
- Recruiters
- Hiring managers
- EdTech platforms conducting resume analysis

---

## 🛠️ How It Works

1. **Input** the job description.
2. **Upload** one or more resumes (PDF format).
3. The system reads and processes each resume.
4. **Cosine similarity scores** are calculated between JD and each resume.
5. Get an **instant, ranked list** of resumes by match score.

---

## 📸 UI Preview

### 🖼️ Home Screen
![Home](Screenshot%202025-06-27%20182246.png)

### 🖼️ JD and Resume Upload
![Upload](Screenshot%202025-06-27%20182435.png)

### 🖼️ Ranking Results
![Results](Screenshot%202025-06-27%20182513.png)

---

## ✅ Requirements

```bash
pip install streamlit pandas scikit-learn PyPDF2
```

---

## ▶️ Run the App

```bash
streamlit run resume_ranking_app.py
```

---

## 📂 File Structure

```
resume_ranking_app.py    # Main Streamlit app
README.md                # Project description and instructions
```

---

## 💡 Future Improvements

- Add OCR support for image-based PDFs
- Integrate with cloud storage (e.g., Google Drive, Dropbox)
- Use large language models (LLMs) for semantic matching
- Add visual dashboards for deeper insights

---

## 📬 Contact

Made with ❤️ by [Shrivardhan Bangale](https://www.linkedin.com/in/shrivardhan-bangale-081421321/)  
🔗 [GitHub Profile](https://github.com/shrivardhanBangale16)
