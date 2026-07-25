import streamlit as st
import pandas as pd
import joblib


# Chargement du modèle
model = joblib.load("modele_faux_billets.joblib")


st.set_page_config(
    page_title="Détecteur de faux billets",
    page_icon="💶"
)


st.title("💶 Détection automatique de faux billets")

st.write(
    """
    Cette application utilise un modèle de régression logistique 
    entraîné sur les caractéristiques physiques des billets.
    
    Importez un fichier CSV contenant les mesures des billets 
    afin d'obtenir une prédiction automatique.
    """
)


# Colonnes attendues par le modèle
features = [
    "diagonal",
    "height_left",
    "height_right",
    "margin_low",
    "margin_up",
    "length"
]


# Upload du fichier
uploaded_file = st.file_uploader(
    "Déposez votre fichier CSV",
    type=["csv"]
)


if uploaded_file is not None:

    # Lecture du fichier
    df = pd.read_csv(
        uploaded_file,
        sep=";"
    )


    st.subheader("Aperçu des données")
    st.dataframe(df.head())


    # Vérification des colonnes
    missing_columns = [
        col for col in features
        if col not in df.columns
    ]


    if missing_columns:

        st.error(
            f"Colonnes manquantes : {missing_columns}"
        )

    else:

        # Sélection des variables nécessaires
        X = df[features]


        # Prédictions
        predictions = model.predict(X)
        probabilities = model.predict_proba(X)


        # Ajout des résultats
        result = df.copy()

        result["prediction"] = predictions


        result["statut"] = result["prediction"].apply(
            lambda x: 
            "Faux billet" if x == 1
            else "Vrai billet"
        )


        result["probabilite_vrai"] = (
            probabilities[:,0] * 100
        ).round(2)


        result["probabilite_faux"] = (
            probabilities[:,1] * 100
        ).round(2)


        st.subheader("Résultats")


        st.dataframe(
            result
        )


        # Résumé
        st.subheader("Résumé")


        col1, col2 = st.columns(2)


        with col1:
            st.metric(
                "Billets vrais",
                (predictions == 0).sum()
            )


        with col2:
            st.metric(
                "Billets faux",
                (predictions == 1).sum()
            )


        # Téléchargement
        csv = result.to_csv(
            sep=";",
            index=False
        )


        st.download_button(
            label="📥 Télécharger les résultats",
            data=csv,
            file_name="resultats_detection_billets.csv",
            mime="text/csv"
        )