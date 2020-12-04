import os

dossierCourant = os.path.dirname(__file__)
dossierTest = os.path.join(dossierCourant, "DossierTest")
# print(f"Nous sommes dans le dossier : {dossierTest}")

if not os.path.exists(dossierTest):
    os.mkdir(dossierTest)
# else:
#     print("Le dossier existe déjà")


d ={ "Films" : ["Le Seigneur Des Anneaux",
                    "Harry Potter",
                    "Moon",
                    "Forest Gump"],
        "Employés" : ["Paul",
                        "Pierre",
                        "Marie"],
        "Exercices" : ["les_variables",
                        "les_fichiers",
                        "les_boucles"]}

for cle, valeurs in d.items():
    for valeur in valeurs:
        folder = os.path.join(dossierTest, cle, valeur)
        # print(f"Nous allons créer le dossier {folder}")
        os.makedirs(folder, exist_ok=True)




