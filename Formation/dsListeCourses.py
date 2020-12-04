import json
import os

# https://www.pierre-giraud.com/python-apprendre-programmer-cours/condition-if-elif-else/

dossierCourant = os.path.dirname(__file__)
cheminListe = os.path.join(dossierCourant,"maListeCourses.json")
#print(f"Nous sommes dans le dossier : {dossierCourant}")
print(f"Le fichier est {cheminListe}")

if os.path.exists(cheminListe):
    with open(cheminListe, "r", encoding="utf8") as f:
        listeCourses = json.load(f)
        
    # print(listeCourses)
else:
    print([])


affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""
choix="0"
while choix != "5":
    choix = input(affichage)

    if choix == "1": # Ajout element
        element = input("Entrez le nom de l'élément à ajouter: ")
        listeCourses.append(element)
        continue
    elif choix=="2": # Enlever element
        element = input("Entrez le nom de l'élément à enlever: ")
        listeCourses.remove(element)
        continue
    elif choix=="3": # Afficher liste
        for x in listeCourses:
            print(x)
        continue
    elif choix=="4": # Vider liste
        listeCourses.clear()
        continue
    elif choix=="5": # Terminer programme
        with open(cheminListe, "w", encoding="utf8") as f:
            json.dump(listeCourses, f, indent=4)
        print("Bye bye")
        break
    else:
        print("!!! Choix invalide. Veuillez enrez une valeur comprise entre 1 et 5 !!!!")
        continue