import glob
import json
import os

dossierCourant = os.path.dirname(__file__)

dossierRecherche = os.path.join(dossierCourant, "DossierTest", "**")
fichiers = glob.glob(dossierRecherche, recursive=True)

for fichier in fichiers:
    name, extension = os.path.splitext(fichier)

    # cprint(extension)
    if extension:
        if extension == ".txt":
            # print("Fichier Text: " + fichier)
            with open(fichier, "r", encoding="utf8") as f:
                text = f.read()
                secuSociale = text.split(": ")
        elif extension == ".json":
            # print("Fichier JSON: " + fichier)
            with open(fichier, "r", encoding="utf8") as f:
                jFileContent = json.load(f)
        else:
            print("Unknown extesion: " + extension)
            continue

print("Contenu fichier JSON:\n")
# print(jFileContent)
# print(type(jFileContent))

print("Compte crédit mutuel: " + str(jFileContent["Credit Mutuel"]["Numero de compte"]))


print("Numéro sécurité sociale: " + str(secuSociale[1]))



        


