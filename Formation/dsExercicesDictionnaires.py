employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
           }

del employes["id03"]

print(employes)

employes["id02"]["age"] = 26

print(employes)

age_paul = employes.get("id01").get("age")
print(age_paul)          