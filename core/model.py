# ===============================================
# File: model.py
# Description: Classe générique pour gérer les modèles ML
# ===============================================

import joblib
from sklearn.base import BaseEstimator

class Model:
    def __init__(self, model: BaseEstimator = None):
        self.model = model

    def train(self, X_train, y_train):
        if self.model is None:
            raise ValueError("Aucun modèle défini.")
        self.model.fit(X_train, y_train)
        print(" Modèle entraîné ")

    def predict(self, X):
        if self.model is None:
            raise ValueError("Aucun modèle défini.")
        return self.model.predict(X)

    def predict_proba(self, X):
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X)
        else:
            raise AttributeError("Le modèle ne supporte pas predict_proba.")

    def save(self, filepath):
        joblib.dump(self.model, filepath)
        print(f" Modèle sauvegardé dans {filepath}")

    def load(self, filepath):
        self.model = joblib.load(filepath)
        print(f" Modèle chargé depuis {filepath}")