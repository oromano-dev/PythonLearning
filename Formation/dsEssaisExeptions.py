import os

dossierCourant = os.path.dirname(__file__)
# print(dossierCourant)

fichier = input("Entrez un fichier à ouvrir: ")
# f = open(fichier, "r", encoding="utf8")
# content = f.read()
# print(content)


try:
    f = open(fichier, "r")
    print(f.read())
except FileNotFoundError:
    print("Fichier introuvable")
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier")
except Exception as e:
    print("Erreur: ", e)
else:
    f.close()






















# a = 12
# # b = "a"

# try:
#     print(a / b)
# except NameError:

# except Exception as e:
#     print("Erreur: ", e)



