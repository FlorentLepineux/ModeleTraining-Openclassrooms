import joblib
import pandas as pd

model = joblib.load("modele_faux_billets.joblib")

df = pd.read_csv("billets.csv", sep=";")

X = df[
    [
        "diagonal",
        "height_left",
        "height_right",
        "margin_low",
        "margin_up",
        "length"
    ]
]

prediction = model.predict(X)

print(prediction[:10])

print("\nRépartition des prédictions :")
print(pd.Series(prediction).value_counts())