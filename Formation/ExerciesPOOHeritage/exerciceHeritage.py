projets = ["pr_Manathan", "HelloWorld", "pr_Newton"]

class Utilisateur:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        
    def __str__(self):
        displayString = "Ulisateur "
        if isinstance(self, Junior):
            displayString += "Junior"
        else:
            displayString += "Senior"

        return f"{displayString} {self.prenom} {self.nom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)


class Junior(Utilisateur):
    def __init__(self, prenom, nom):
         super().__init__(prenom, nom)
         

    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)         

paul = Utilisateur("Paul", "Durant")
print(paul)
paul.afficher_projets()  