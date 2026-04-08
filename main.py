# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:54:55 2026

@author: Sene
"""
from maths.operations import addition,soustractions,multiplication
from maths.statistiques import moyenne,maximum,minimum
from utils.string_utils import inverser_chaine,compter_mots
import requests

a=int(input("saisir a: "))
b=int(input("saisir b: "))
print(f"la somme est : {addition(a,b)}")
print(f"la difference est : {soustractions(a,b)}")
print(f"le produit est : {multiplication(a,b)}")

liste=[10, 20, 30, 40, 50]
print(f"la moyenne est: {moyenne(liste)}")
print(f"le max de la liste est: {maximum(liste)}")
print(f"le min de la liste est: {minimum(liste)}")

chaine="Bonjour tout le monde"
print(f"la chaine inversé est: {inverser_chaine(chaine)}")
print(f"le nbre de mot est: {compter_mots(chaine)}")



def tester_requete(url: str):
    """Teste une requête HTTP GET simple avec requests."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Requête réussie !")
            print("Contenu (premiers 300 caractères) :")
            print(response.text[:300])
        else:
            print(f"Erreur HTTP : {response.status_code}")
    except Exception as e:
        print(f"Erreur de connexion : {e}")
