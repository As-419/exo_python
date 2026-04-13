# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:04:53 2026

@author: Sene
"""
from .operations import addition
def moyenne(liste):
  return sum(liste) / len(liste)

def maximum(liste):
    return max(liste)

def minimum(liste):
    return min(liste)

def somme_des_carres(liste):
    total=0
    for x in liste:
        total=addition(total, x**2)
    return total
liste=[10, 20, 30, 40, 50]
print(somme_des_carres((liste)))