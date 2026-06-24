# AI Resume Screening System

## Overview

AI Resume Screening System is a web-based application developed using Python and Streamlit that automates the process of screening resumes against job descriptions. The system analyzes PDF resumes, extracts textual information, and calculates a matching score using Natural Language Processing (NLP) techniques.

This project helps recruiters and hiring teams quickly identify suitable candidates by comparing resume content with job requirements.

## Features

* Upload PDF resumes
* Enter custom job descriptions
* Extract text from resumes automatically
* Calculate resume-job match score
* Display candidate suitability percentage
* User-friendly Streamlit interface

## Technology Stack

* Python
* Streamlit
* Scikit-learn
* PyPDF2
* Pandas
* Natural Language Processing (NLP)

## Working Principle

1. User uploads a resume in PDF format.
2. User enters a job description.
3. The application extracts text from the resume.
4. TF-IDF Vectorization converts text into numerical features.
5. Cosine Similarity measures the similarity between the resume and job description.
6. A matching score is generated and displayed.

## Project Structure

AI_Resume_Screener/

├── app.py

├── requirements.txt

├── .gitignore

└── venv/

## Installation

### Clone the Repository

```bash
git clone https://github.com/chittygoud130-ctrl/AI-Resume-Screening-System.git
cd AI-Resume-Screening-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Future Enhancements

* Automatic skill extraction
* Candidate ranking system
* Resume parsing (Name, Email, Phone)
* Multiple resume comparison
* Dashboard and analytics
* Cloud deployment

## Learning Outcomes

* Python Application Development
* Machine Learning Fundamentals
* Natural Language Processing
* Git and GitHub Version Control
* Streamlit Web Application Development

## Author

**Vamshi**

GitHub: https://github.com/chittygoud130-ctrl

## License

This project is developed for educational and learning purposes.
