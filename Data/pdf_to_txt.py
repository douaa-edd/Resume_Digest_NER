import pdfplumber
import os

def lire_pdf_avec_newlines(chemin_pdf):
    try:
        texte = ""
        with pdfplumber.open(chemin_pdf) as pdf:
            for page in pdf.pages:
                texte += page.extract_text() + '\n'  # Respecte les sauts de ligne entre pages
        return texte
    except FileNotFoundError:
        print("Fichier non trouvé :", chemin_pdf)
        return ""

# Chemin vers le fichier PDF
chemin_pdf = "CV_pdf/cv.pdf"
texte = lire_pdf_avec_newlines(chemin_pdf)

# Sauvegarde dans le même répertoire que le notebook
nom_fichier_txt = os.path.splitext(os.path.basename(chemin_pdf))[0] + ".txt"
with open(nom_fichier_txt, "w", encoding="utf-8") as f:
    f.write(texte)

print(f"Fichier texte sauvegardé sous : {nom_fichier_txt}")
