import os
from pprint import pprint

dossierCourrant = os.path.dirname(__file__)
sourcePrenoms = os.path.join(dossierCourrant, "prenoms.txt")
destPrenoms = os.path.join(dossierCourrant, "prenoms_final.txt")


with open(sourcePrenoms, "r", encoding="utf8") as f:
    lines = f.read().splitlines()

# pprint(lines)

prenom_ordre = []
for line in lines:
    prenom_ordre.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenom_ordre]
with open(destPrenoms, "w", encoding="utf8") as f:
    f.write("\n".join(sorted(prenoms_final)))