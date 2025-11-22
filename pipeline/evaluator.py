from utils.metrics import Metrics
import numpy as np
import pandas as pd

class Evaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, X_test, y_test, threshold=0.5):
        # Prédictions
        if hasattr(self.model, "predict_proba"):
            y_prob = self.model.predict_proba(X_test)[:, 1]
            y_pred = (y_prob >= threshold).astype(int)
        else:
            y_pred = self.model.predict(X_test)

        # Calcul metrics via la classe Metrics
        metrics = Metrics(y_test, y_pred)
        results = {
            "accuracy": metrics.accuracy(),
            "confusion_matrix": metrics.confusion_matrix(),
            "classification_report": metrics.classification_report()
        }
        return results

    def print_results(self, results):
        print(f"\n Accuracy : {results['accuracy']:.3f}")
        print("\nMatrice de confusion :\n", results['confusion_matrix'])
        print("\nRapport de classification :\n", results['classification_report']) 