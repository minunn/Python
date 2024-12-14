import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Je charge les données
# kaggle utilisé : https://www.kaggle.com/datasets/annakhew/sample-country-sales-dataset
donnees = pd.read_csv('Sales_records.csv')

# J'explore les données pour identifier les colonnes à nettoyer
print("Aperçu des données :")
print(donnees.head())
print("\nInformations sur les données :")
print(donnees.info())
print("\nValeurs manquantes :")
print(donnees.isnull().sum())

# Je nettoie les données en supprimant les colonnes inutiles et les valeurs manquantes
colonnes_a_supprimer = ['Order ID', 'Ship Date']
colonnes_existantes_a_supprimer = [col for col in colonnes_a_supprimer if col in donnees.columns]
donnees = donnees.drop(columns=colonnes_existantes_a_supprimer)

# Je nettoie les données en convertissant les colonnes numériques en type numérique
donnees['Total Revenue'] = pd.to_numeric(donnees['Total Revenue'], errors='coerce')
donnees['Units Sold'] = pd.to_numeric(donnees['Units Sold'], errors='coerce')
donnees['Total Cost'] = pd.to_numeric(donnees['Total Cost'], errors='coerce')
donnees['Total Profit'] = pd.to_numeric(donnees['Total Profit'], errors='coerce')

# Je nettoie les données en supprimant les lignes avec des valeurs manquantes
donnees = donnees.dropna(subset=['Total Revenue', 'Units Sold', 'Total Cost', 'Total Profit'])

print("\nDonnées nettoyées :")
print(donnees.head())

# Je transforme les données pour les analyser
donnees['Order Date'] = pd.to_datetime(donnees['Order Date'], errors='coerce')

# Je crée une colonne pour le mois de la commande
donnees.set_index('Order Date', inplace=True)
donnees_mensuelles = donnees.resample('ME').sum().reset_index()

# Je crée une colonne pour le mois de la commande
plt.figure(figsize=(10, 6))
sns.lineplot(data=donnees_mensuelles, x='Order Date', y='Total Revenue', marker='o')
plt.title('Ventes au fil du temps (mensuelles)')
plt.xlabel('Date de commande')
plt.ylabel('Revenu total')
plt.grid()
plt.show()

# Je crée une colonne pour le mois de la commande
print("\nCalcul de la matrice de corrélation :")
donnees_numeriques = donnees.select_dtypes(include=[np.number])
matrice_correlation = donnees_numeriques.corr()
print(matrice_correlation)

plt.figure(figsize=(8, 6))
sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matrice de corrélation')
plt.show()

# Je crée une colonne pour le mois de la commande
donnees_clustering = donnees[['Total Revenue', 'Total Profit']].dropna()
normaliseur = StandardScaler()
donnees_normalisees = normaliseur.fit_transform(donnees_clustering)

if len(donnees_normalisees) > 0:
    # Je crée les clusters avec l'algorithme K-means
    kmeans = KMeans(n_clusters=3, random_state=42)
    donnees_clustering['Cluster'] = kmeans.fit_predict(donnees_normalisees)

    # Je limite le nombre de points pour la visualisation des clusters
    echantillon_donnees = donnees_clustering.sample(n=min(1000, len(donnees_clustering)), random_state=42)

    # Je visualise les clusters en fonction des ventes et profits
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=echantillon_donnees, x='Total Revenue', y='Total Profit', hue='Cluster', palette='viridis')
    plt.title('Clustering des ventes et profits (échantillon)')
    plt.xlabel('Revenu total')
    plt.ylabel('Profit total')
    plt.legend(title='Cluster')
    plt.show()
else:
    print("\nPas assez de données pour effectuer le clustering.")
