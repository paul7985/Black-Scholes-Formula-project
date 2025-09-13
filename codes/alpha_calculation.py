import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

"Extraction de données réelles"

file_path = r'D:\TRAGUS\COURS\M1\Prog\donnees_porc.csv' #destination du fichier
data = pd.read_csv(file_path, delimiter=';', parse_dates=['Date'], dayfirst=True) #précisions sur la nature du fichier
data = data[data['Date'].dt.year >= 2020] #Limitation des données 

#Attribution des données à deux variables
dates_2023 = data['Date'] 
prix_2023 = data['Prix']

"""

Calcul des données d'extrapolation

"""

"Calcul de la volatilité"

# Dates
date_debut = datetime(2023, 10, 6)
date_fin = datetime(2024, 10, 5)

# Initialiser une liste pour stocker les dates
dates_2024 = []

# Boucler à travers les dates et les ajouter à la liste
current_date = date_debut
while current_date <= date_fin:
    dates_2024.append(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)

#Transformation des données de dates 2023 en une liste
dates_2023_liste = dates_2023.tolist()

#Créer une liste alliant les dates de 2022 à 2024
dates = dates_2023_liste + dates_2024

# Prix initial (le dernier prix de votre graphe)
prix_initial = 80.82  # Changez cette valeur avec le dernier prix de votre graphe

# Liste des prix
prix_2024 = [prix_initial]

volatilité = 1.8
for i in range(1, len(dates_2024)):
    # Générer un prix aléatoire pour le jour suivant
    variation = random.choice([-volatilité, volatilité])
    nouveau_prix = prix_2024[-1] + variation

    # Ajouter ce prix à la liste
    prix_2024.append(nouveau_prix)

#Création d'une liste à partir des données de prix
prix_2023_liste = prix_2023.tolist()

prix = prix_2023_liste + prix_2024

"Présentation des résultats"

# Tracer le graphique
plt.figure(figsize=(10, 6), facecolor='black')
plt.plot(dates, prix, color='skyblue', linewidth=1, label='Prix du porc', marker='')

# Personnaliser l'apparence du graphique
plt.title(f'Évolution du prix du porc (à partir de 2022), variation quotidienne de ± {volatilité}USD', color='white')
plt.xlabel('Date', color='white')
plt.ylabel('Prix en USD', color='white')
plt.gca().set_facecolor('black')
# plt.gca().spines['bottom'].set_color('white')
# plt.gca().spines['top'].set_color('white') 
# plt.gca().spines['right'].set_color('white')
# plt.gca().spines['left'].set_color('white')
plt.gca().xaxis.label.set_color('white')
plt.gca().yaxis.label.set_color('white')
plt.gca().tick_params(axis='x', colors='white')
plt.gca().tick_params(axis='y', colors='white')
# plt.legend(loc='upper left', fontsize='small', frameon=False)

# Agrandir l'axe des x jusqu'au 5 octobre 2024
# plt.xlim(dates_2023.min(), pd.to_datetime('2025-10-05'))

# Afficher le graphique
plt.show()
