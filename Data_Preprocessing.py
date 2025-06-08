import os
import re

def nettoyer_cv(texte):
    # Supprimer les caractères non imprimables
    texte = re.sub(r'[^\x00-\x7F]+', ' ', texte)
    
    # Supprimer les balises HTML ou XML s'il y en a
    texte = re.sub(r'<.*?>', '', texte)

    # Supprimer les répétitions de ponctuation
    texte = re.sub(r'[-=]{2,}', ' ', texte)

    # Remplacer les tabulations et retours chariot multiples par un espace
    texte = re.sub(r'\s+', ' ', texte)

    # Supprimer les lignes très courtes 
    lignes = texte.split('\n')
    lignes_filtrees = [ligne.strip() for ligne in lignes if len(ligne.strip()) > 2]
    texte = '\n'.join(lignes_filtrees)

    # Supprimer les doublons de lignes
    lignes_uniques = list(dict.fromkeys(texte.split('\n')))
    texte = '\n'.join(lignes_uniques)

    return texte.strip()

# Chemins des dossiers
dossier_source = "Data/CV_txt"         # Dossier où sont les .txt extraits
dossier_destination = "Data/CV_cleaned"  # Dossier de sortie nettoyé

os.makedirs(dossier_destination, exist_ok=True)

# Parcours des fichiers texte
for nom_fichier in os.listdir(dossier_source):
    if nom_fichier.endswith(".txt"):
        chemin_fichier = os.path.join(dossier_source, nom_fichier)

        with open(chemin_fichier, "r", encoding="utf-8") as f:
            texte_original = f.read()

        texte_nettoye = nettoyer_cv(texte_original)

        # Sauvegarde du texte nettoyé
        chemin_sortie = os.path.join(dossier_destination, nom_fichier)
        with open(chemin_sortie, "w", encoding="utf-8") as f:
            f.write(texte_nettoye)

        print(f"✅ {nom_fichier} nettoyé et sauvegardé.")
