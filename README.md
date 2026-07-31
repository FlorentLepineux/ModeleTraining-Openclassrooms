# 💶 Détection automatique de faux billets

## 📖 Présentation

Ce projet a été réalisé dans le cadre de la formation **Data Analyst** d'OpenClassrooms.

L'objectif est de développer un modèle de Machine Learning capable de déterminer automatiquement si un billet est authentique ou contrefait à partir de ses caractéristiques physiques.

Une application interactive développée avec **Streamlit** permet ensuite à l'utilisateur d'importer un fichier CSV contenant plusieurs billets afin d'obtenir instantanément les prédictions.

---

## 🎯 Objectifs

- Réaliser une analyse exploratoire des données.
- Prétraiter les données (gestion des valeurs manquantes).
- Comparer plusieurs modèles de Machine Learning.
- Sélectionner le modèle le plus performant.
- Déployer une application web accessible à tous.

---

## 📊 Données

Le jeu de données contient les mesures physiques de billets.

Variables utilisées :

| Variable | Description |
|----------|-------------|
| diagonal | Longueur de la diagonale |
| height_left | Hauteur du côté gauche |
| height_right | Hauteur du côté droit |
| margin_low | Marge inférieure |
| margin_up | Marge supérieure |
| length | Longueur du billet |

Variable cible :

- **0** : billet authentique
- **1** : faux billet

---

## 🛠 Prétraitement

Les étapes de préparation des données comprennent :

- Imputation des valeurs manquantes à l'aide d'un **IterativeImputer**
- Création de la variable **is_fake**
- Standardisation des variables numériques
- Séparation des données d'entraînement et de test

---

## 🤖 Modèles évalués

Plusieurs algorithmes ont été comparés :

- Régression Logistique
- K-Nearest Neighbors (KNN)
- Random Forest
- Support Vector Machine (SVM)
- Decision Tree
- Naive Bayes
- K-Means (à titre de comparaison)

---

## 📈 Résultats

| Modèle | Accuracy | F1-score |
|---------|---------:|---------:|
| Régression Logistique | **99 %** | **98,48 %** |
| SVM | **99 %** | **98,48 %** |
| KNN | 98,67 % | 97,98 % |
| Random Forest | 98,67 % | 97,96 % |
| Naive Bayes | 98,67 % | 97,98 % |
| Decision Tree | 97,33 % | 96,00 % |
| K-Means | 98,67 % | 97,97 % |

La **régression logistique** a été retenue pour l'application finale en raison de ses excellentes performances, de sa simplicité d'interprétation et de sa rapidité d'exécution.

---

## 🌐 Application Streamlit

L'application permet de :

- importer un fichier CSV ;
- détecter automatiquement les faux billets ;
- afficher les résultats directement dans le navigateur ;
- télécharger les prédictions.

---

## 🚀 Technologies utilisées

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

---

## 📂 Structure du projet

```
.
├── app.py
├── billets.csv
├── modele_faux_billets.joblib
├── requirements.txt
├── Fake_Bill_Detector.ipynb
├── Modele_Research_And_Training.ipynb
└── README.md
```

---

## 🌍 Application en ligne

👉 https://openclassroom-billet-64pysfznxzrxvhz84bv4vi.streamlit.app

---

## 👤 Auteur

**Florent Lepineux**

Projet réalisé dans le cadre de la formation **Data Analyst - OpenClassrooms**.
