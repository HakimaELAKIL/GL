# ===============================================
# File: trainer.py
# Description: Entraîne et sauvegarde le modèle
# ===============================================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core')))
# ===============================================#


from core.dataset import ClinicalDataset
from core.logisticregression import LogisticRegressionModel

def train_and_save(csv_path="data/dataset.csv", model_path="logistic_model.pkl"):
    # Charger les données
    dataset = ClinicalDataset(csv_path)
    X_train, X_test, y_train, y_test = dataset.load_and_prepare()

    # Créer le modèle
    model = LogisticRegressionModel()
    model.train(X_train, y_train)

    # Sauvegarder
    model.save(model_path)
    return model, X_test, y_test

if __name__ == "__main__":
    train_and_save()