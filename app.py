
import streamlit as st
st.set_page_config(page_title="Smart CV Parser", page_icon="📄", layout="wide")

import pdfplumber
import pandas as pd
import spacy
from io import BytesIO


# ====== Load spaCy model ======
@st.cache_resource
def load_model():
    return spacy.load("model")  # Change path if different

nlp = load_model()

# ====== Extract text from PDF ======
def extract_text_from_pdf(file):
    full_text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text.strip()

# ====== Extract entities using spaCy ======
def extract_entities(text, filename):
    doc = nlp(text)
    data = {
        "File Name": filename,
        "First Name": "",
        "Last Name": "",
        "Birth Date": "",
        "Gender": "",
        "Phone": "",
        "Email": "",
        "Address": "",
        "Skills": [],
        "Diplomas": [],
        "Languages": [],
        "Work Experience": [],
        "Other": []
    }
    for ent in doc.ents:
        label = ent.label_.upper().strip()
        value = ent.text.strip()
        if label == "FIRST NAME":
            data["First Name"] = value
        elif label == "LAST NAME":
            data["Last Name"] = value
        elif label == "BIRTH DATE":
            data["Birth Date"] = value
        elif label == "GENDER":
            data["Gender"] = value
        elif label == "PHONE":
            data["Phone"] = value
        elif label == "EMAIL":
            data["Email"] = value
        elif label == "ADDRESS":
            data["Address"] = value
        elif label == "SKILLS":
            data["Skills"].append(value)
        elif label == "DIPLOMA":
            data["Diplomas"].append(value)
        elif label == "LANGUAGES":
            data["Languages"].append(value)
        elif label == "WORK_EXPERIENCE":
            data["Work Experience"].append(value)
        elif label == "OTHERS":
            data["Other"].append(value)

    for key in ["Skills", "Diplomas", "Languages", "Work Experience", "Other"]:
        data[key] = ", ".join(data[key])
    return data

# ====== Streamlit App ======

st.title("📄 Smart CV Parser")
st.write("Upload one or more resumes in PDF format. This app uses a custom-trained Named Entity Recognition (NER) model to automatically extract key information from each CV.")

uploaded_files = st.file_uploader("Upload your PDF file(s):", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    extracted_data = []

    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        result = extract_entities(text, file.name)
        extracted_data.append(result)

    df = pd.DataFrame(extracted_data)

    st.success("✅ Extraction complete!")
    st.dataframe(df)

    # ====== Convert to Excel ======
    def convert_df_to_excel(dataframe):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            dataframe.to_excel(writer, index=False, sheet_name='Results')
        return output.getvalue()

    excel_file = convert_df_to_excel(df)

    st.download_button(
        label="📥 Download results as Excel",
        data=excel_file,
        file_name="extracted_cv_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
