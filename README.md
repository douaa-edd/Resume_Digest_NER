# 📄 Resume_Digest_NER – Smart CV Parsing with BERT & spaCy

**Resume_Digest_NER** is a lightweight Streamlit-based web application that allows HR professionals and recruiters to automatically extract and structure key information from CVs (PDF format) using a Named Entity Recognition (NER) model built with **spaCy** and **BERT (bert-base-cased)**.



## 🚀 Key Features

- 📥 Upload multiple resumes in **PDF** format  
- 🧠  Intelligent information extraction using a **fine-tuned BERT** model (bert-base-cased)
- 📄 Extracted fields:
  - First Name, Last Name, Date of Birth, Gender
  - Phone, Email, Address
  - Skills, Diplomas, Languages, Work Experience, Others
- 📊 Outputs structured data in a downloadable **Excel (XLSX)** file  
- 🖥️ Clean and intuitive **Streamlit** web interface  



## 🎯 Project Objectives
- Accelerate CV processing and analysis for HR teams
- Demonstrate the effectiveness of **BERT + spaCy** in real-world information extraction tasks
- Provide a simple, extensible NLP solution that is easy to use



## 🧠 Model Details
The system is based on a **pre-trained Transformer model**, bert-base-cased, fine-tuned for the specific task of named entity recognition in CVs.



## 📁 Project Structure

```bash
Resume_Digest_NER/

├── app.py # 🚀 Main Streamlit application

├── model/ # 🧠 Trained spaCy NER model (with BERT backbone)

├── Data/
│
│   ├── CV_pdf/ # 📄 Input resumes in PDF format
│
│   ├── CV_txt/ # 📝 Raw extracted text from PDFs
│   
│   ├── CV_cleaned/ # 🧹 Cleaned/preprocessed CV text
│   
│   ├── CV_annot/ # 🏷️ (Optional) annotated data for future training
│
│   ├── pdf_to_txt.py # 🔧 PDF-to-text conversion script

├── Data_Preprocessing.py # ⚙️ Cleaning & text preprocessing utilities

├── Training.ipynb # 📘 (Optional) NER training notebook

├── requirements.txt # 📦 Python dependencies

├── README.md # 📄 Project documentation

```



## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Resume_Digest_NER.git
cd Resume_Digest_NER
```

### 2. Create and activate a virtual environment (Optional) 

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4.Run the Application
Make sure your trained spaCy NER model is placed in the model/ directory.

Then launch the app with:

```bash
streamlit run app.py
```

