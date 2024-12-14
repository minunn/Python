import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Je charge les données
# kaggle utilisé : https://www.kaggle.com/code/maulipatel18/weather-data-analysis
chemin_fichier = './weather_data.csv'
donnees = pd.read_csv(chemin_fichier)

# J'explore les données pour identifier les colonnes à nettoyer
print("Aperçu des premières lignes :")
print(donnees.head())

print("\nTypes des colonnes :")
print(donnees.dtypes)

print("\nNombre de valeurs manquantes :")
print(donnees.isnull().sum())

print("\nStatistiques descriptives :")
print(donnees.describe(include='all'))

# Je nettoie les données en supprimant les colonnes inutiles et les valeurs manquantes
colonnes_numeriques = donnees.select_dtypes(include=['float64', 'int64'])

Q1 = colonnes_numeriques.quantile(0.25)
Q3 = colonnes_numeriques.quantile(0.75)
IQR = Q3 - Q1

borne_inferieure = Q1 - 1.5 * IQR
borne_superieure = Q3 + 1.5 * IQR

for col in colonnes_numeriques.columns:
    donnees = donnees[(donnees[col] >= borne_inferieure[col]) & (donnees[col] <= borne_superieure[col])]

print("\nDimensions après nettoyage des valeurs aberrantes :", donnees.shape)

# Je transforme les données pour les analyser : normalisation, encodage et agrégation
colonnes_categoriques = [col for col in donnees.columns if donnees[col].dtype == 'object' and donnees[col].nunique() < 50]
donnees_dummies = pd.get_dummies(donnees[colonnes_categoriques], drop_first=True)

for col in colonnes_numeriques.columns:
    donnees[col] = zscore(donnees[col])

if 'Date_Time' in donnees.columns:
    donnees['mois'] = pd.to_datetime(donnees['Date_Time']).dt.month

donnees_transformees = pd.concat([donnees_dummies, colonnes_numeriques, donnees[['mois']] if 'mois' in donnees.columns else pd.DataFrame()], axis=1)

print("\nAperçu des données transformées :")
print(donnees_transformees.head())

# J'agrége les données pour les analyser : moyennes par mois
if 'Temperature_C' in donnees_transformees.columns and 'mois' in donnees_transformees.columns:
    temperature_par_mois = donnees_transformees.groupby('mois')['Temperature_C'].mean()
    print("\nTempératures moyennes par mois :")
    print(temperature_par_mois)

# Je visualise les données transformées : température moyenne par mois et matrice de corrélation
if 'mois' in donnees_transformees.columns and 'Temperature_C' in donnees_transformees.columns:
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=temperature_par_mois.index, y=temperature_par_mois.values)
    plt.title("Température moyenne par mois")
    plt.xlabel("Mois")
    plt.ylabel("Température moyenne (°C)")
    plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(donnees_transformees.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()

# Je simule des données de ventes pour analyser les ventes par produit
np.random.seed(123)
dates = pd.date_range(start="2023-06-01", end="2023-12-31", freq="D")
produits = ["Article X", "Article Y", "Article Z", "Article W"]

donnees_ventes = pd.DataFrame({
    'date': np.random.choice(dates, 1200),
    'produit': np.random.choice(produits, 1200),
    'prix': np.random.uniform(5, 80, 1200),
    'quantite': np.random.randint(2, 15, 1200)
})
donnees_ventes['ventes_totales'] = donnees_ventes['prix'] * donnees_ventes['quantite']

ventes_par_produit = donnees_ventes.groupby('produit')['ventes_totales'].sum()
print("\nVentes totales par produit :")
print(ventes_par_produit)

plt.figure(figsize=(10, 6))
sns.barplot(x=ventes_par_produit.index, y=ventes_par_produit.values)
plt.title("Ventes totales par produit")
plt.xlabel("Produit")
plt.ylabel("Ventes totales (€)")
plt.show()

produit_le_plus_rentable = ventes_par_produit.idxmax()
print(f"\nProduit le plus rentable : {produit_le_plus_rentable}, avec {ventes_par_produit.max()} € de ventes.")
