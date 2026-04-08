# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:56:24 2026

@author: Sene
"""

import requests

# Étape 1 : Paramètres de l'API
API_KEY = "votre_cle_api"  # Remplace par ta clé OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
VILLE = "Dakar"

# Étape 2 : Construction de la requête
params = {
    "q": VILLE,
    "appid": API_KEY,
    "units": "metric",   # Température en °C
    "lang": "fr"         # Description en français
}

# Étape 3 : Requête GET
response = requests.get(BASE_URL, params=params)

# Étape 4 : Traitement de la réponse
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidite = data["main"]["humidity"]

    print(f"Météo à {VILLE}:")
    print(f"-- Température : {temperature}°C")
    print(f"-- Description : {description}")
    print(f"-- Humidité : {humidite}%")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
    print(response.text)
