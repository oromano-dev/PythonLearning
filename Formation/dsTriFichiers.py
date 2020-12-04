import os
import glob
import shutil

dossierCourrant = os.path.dirname(__file__)
dossierTri = os.path.join(dossierCourrant, "TriFichiers")
fichiersATrier = os.path.join(dossierCourrant, "DossierTest", "Fichiers", "**")

# print(fichiersATrier)
extensions = { ".mp3": "Musique",
                ".wav": "Musique",
                ".mp4": "Videos", 
                ".mov": "Videos",
                ".jpeg": "Images",
                ".jpg": "Images",
                ".png": "Images",
                ".pdf": "Documents"
                }


# listeDossiers = ["Musique", "Videos", "Images", "Documents"]
listeFichiers = glob.glob(fichiersATrier, recursive=True)

# for repertoire in listeDossiers:
#     # print(repertoire)
#     os.makedirs(os.path.join(dossierTri, repertoire), exist_ok=True)

for fichier in listeFichiers:
    extension = os.path.splitext(fichier)[-1]
    # print(extension)
    dossier = extensions.get(extension)
    # print(dossier)
    if dossier:
        shutil.move(fichier, os.path.join(dossierTri, dossier))  
        # print(os.path.join(dossierTri, dossier))
