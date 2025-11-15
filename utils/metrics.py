# ===============================================
# File: metrics.py
# Description: Classe pour calculer les métriques
# ===============================================

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class Metrics:
    def __init__(self, y_true, y_pred):
        """
        Initialise avec les labels réels et prédits.
        """
        self.y_true = y_true
        self.y_pred = y_pred

    def accuracy(self):
        return accuracy_score(self.y_true, self.y_pred)

    def confusion_matrix(self):
        return confusion_matrix(self.y_true, self.y_pred)

    def classification_report(self):
        return classification_report(self.y_true, self.y_pred, digits=3)