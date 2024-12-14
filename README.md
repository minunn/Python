# Rapport d'Analyse des Données de Ventes

## Introduction

Ce projet se concentre sur l’analyse d’un ensemble de données de ventes, comprenant des informations sur les revenus, les coûts et les profits générés par diverses transactions. L’objectif principal était de nettoyer, prétraiter et visualiser les données pour identifier des tendances, des relations entre les différentes variables, et segmenter les données pour une analyse plus approfondie. Voici un résumé des étapes réalisées et des résultats obtenus.

## Préparation des données

La première étape a consisté à charger et nettoyer les données brutes pour se concentrer sur les éléments pertinents pour l’analyse. Les principales étapes sont les suivantes :

1. **Chargement des données** : Le fichier CSV contenant les enregistrements de ventes a été chargé à l’aide de `pandas`.
2. **Nettoyage des données** : Des colonnes inutiles, telles que `Order ID` et `Ship Date`, ont été supprimées pour se concentrer sur les informations essentielles.
3. **Conversion des types de données** : Les colonnes liées aux revenus (`Total Revenue`), aux unités vendues (`Units Sold`), aux coûts (`Total Cost`) et aux profits (`Total Profit`) ont été converties en types numériques.
4. **Suppression des lignes incorrectes** : Les lignes contenant des données manquantes ou incorrectes dans des colonnes clés ont été supprimées pour garantir la qualité de l’analyse.
5. **Transformation des dates** : La colonne `Order Date` a été convertie en format datetime pour faciliter les analyses temporelles.

### 1. Tendances des Ventes

Une première analyse a consisté à visualiser l’évolution des ventes mensuelles, en traçant un graphique de l’évolution du revenu total par mois. Cette visualisation a permis d’observer :

- Les tendances de croissance des ventes au fil du temps.
- Des variations saisonnières ou des pics de vente, ainsi que des périodes de stagnation.

### 2. Matrice de Corrélation

Une analyse de corrélation entre les variables numériques a été réalisée pour identifier les relations entre les revenus, les coûts et les profits. Le résultat a montré des corrélations significatives, ce qui a permis de conclure que les profits sont fortement liés aux revenus, et les coûts sont un facteur clé dans la gestion des marges bénéficiaires.

### 3. Clustering des Données

Pour approfondir l’analyse, une méthode de clustering K-Means a été appliquée sur les colonnes `Total Revenue` et `Total Profit`. Cette segmentation a permis d’identifier des groupes de transactions ayant des caractéristiques similaires. Les clusters obtenus permettent de distinguer :

- Des groupes de transactions générant des revenus et des profits élevés.
- Des groupes de transactions avec des marges bénéficiaires plus faibles.
## Conclusion

En conclusion, cette analyse a permis de mieux comprendre les tendances de ventes, de repérer les corrélations entre revenus, coûts et profits, et de segmenter les données en groupes significatifs. Les résultats obtenus peuvent être utilisés pour affiner les stratégies commerciales et optimiser la gestion des marges bénéficiaires. Ces analyses offrent une base solide pour des investigations futures sur la rentabilité et les performances des ventes.
