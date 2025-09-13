"""

Preparatifs

"""

#Importation des bibliotheques
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

"""

Etape 1 : Extraction des donnees reelles

"""

# 1.1. Extraction des donnees brutes
file_path = r'C:\Personnel\TRAGUS\Projets Code\Black_Scholes_project\donnees_porc.csv'
data = pd.read_csv(file_path, delimiter=';', parse_dates=['Date'], dayfirst=True)
data = data[data['Date'].dt.year >= 2022]

# 1.2. Attribution des donnees aux variables
dates_reelles_data = data['Date']
prix_reels_data = data['Prix']

"""

Etape 2 : Calcul des donnees d'extrapolation

"""

# 2.1. Generation de dates futures
date_debut = datetime(2023, 10, 6) #date du projet
date_fin = datetime(2024, 11, 30)

dates_extrapolees = [date_actuelle.strftime("%Y-%m-%d") for date_actuelle in pd.date_range(date_debut, date_fin)]

# 2.2. Extrapolation sur les prix de 2024
N = 50
mu = 0
ecart_type = 1.0
nb_echantillons = 100000
prix_initial = 80.82
prix_extrapoles = [[prix_initial] for _ in range(N)]

for j in range(N):
    proba_gauss = np.random.normal(mu, ecart_type, nb_echantillons)

    for i in range(1, len(dates_extrapolees)):
        variation = proba_gauss[i - 1]
        nouveau_prix = prix_extrapoles[j][-1] + variation
        prix_extrapoles[j].append(nouveau_prix)

"""

Etape 3 : Mise en commun des donnees reelles et extrapolées

"""
# 3.1. Formatage et mise en commun des dates
dates_reelles = dates_reelles_data.tolist()
dates = dates_reelles + dates_extrapolees

# 3.2. Formatage et mise en commun des prix
prix_reels = prix_reels_data.tolist()
prix = prix_reels + prix_extrapoles


"""

Etape 4 : Calcul du coût pour la banque

"""

K = 95.00

couts_banque = []

for j in range(N):
    prix_final = prix_extrapoles[j][-1]
    cout = max(0, prix_final - K) 
    couts_banque.append(cout)

moyenne_couts_banque = sum(couts_banque) / N

print(f"La moyenne des coûts pour la banque sur {N} évolutions possibles est : {moyenne_couts_banque}")

"""

Etape 5 : Présentation des résultats

"""

fig, ax = plt.subplots(figsize=(10, 6), facecolor='black', dpi=300)

def animate(i):
    ax.clear()

    ax.plot(dates_reelles, prix_reels, color='#79F8F8', antialiased=True, linewidth=0.15, label='Prix reels', marker='', linestyle='-')

    for j in range(i+1):
        if prix_extrapoles[j][-1] > K:
            ax.plot([datetime.strptime(date, "%Y-%m-%d") for date in dates_extrapolees], prix_extrapoles[j], color='red', alpha=0.5, linewidth=0.5, label=f'Extrapolation {j+1}', linestyle='-')
        else:
            ax.plot([datetime.strptime(date, "%Y-%m-%d") for date in dates_extrapolees], prix_extrapoles[j], color='green', alpha=0.5, linewidth=0.5, label=f'Extrapolation {j+1}', linestyle='-')

        cout = max(0, prix_extrapoles[j][-1] - K)

        if j > 0:
            previous_cout_text.remove()

        if cout > 0:
            couleur_texte = 'red'
        else:
            couleur_texte = 'green'

        cout_text = ax.text(datetime(2024, 11, 30), prix_extrapoles[j][-1], f'Coût: {cout:.2f}', color=couleur_texte, fontsize=8, ha='right')
        
        previous_cout_text = cout_text

    ax.axhline(y=K, color='lightyellow', linestyle='--', linewidth=0.2)
    ax.text(datetime(2023, 9, 1), K+2, f'K = {K}', color='lightyellow', fontsize=6)
    ax.set_title(f'Evolutions possibles et moyennage pour un ecart type = {ecart_type}', color='white')
    ax.set_xlabel('Date', color='white')
    ax.set_ylabel('Prix en USD', color='white')
    ax.set_facecolor('black')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white', labelsize=6)
    ax.tick_params(axis='y', colors='white', labelsize=6)
    ax.grid(True, which='both', linestyle='-', linewidth=0.15, color='gray')

output_path = r"C:\Personnel\TRAGUS\Projets Code\Black_Scholes_project\animation.gif"

ani = FuncAnimation(fig, animate, frames=N, repeat=False, interval=150)

ani.save(output_path, writer="pillow")

print(f"✅ Animation enregistrée avec succès : {output_path}")
plt.show()