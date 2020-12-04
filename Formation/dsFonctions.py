import os

dossierCourant = os.path.dirname(__file__)


def maFoncion():
    print("Je suis une fonction")


def afficheLeMeilleur(meilleur="Ordinateur"):
    """Descrition de afficheMeilleur

    Args:
        meilleur (str, optional): Nom du meilleur élément. Defaults to "Ordinateur".
    """
    print(meilleur + " est le meilleur")


maFoncion()
afficheLeMeilleur()
afficheLeMeilleur("Octavio")