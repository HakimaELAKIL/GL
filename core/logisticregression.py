# ===============================================
# File: LogisticRegressionModel.py
# Description: Classe LogisticRegression héritée de Model
# ===============================================

from sklearn.linear_model import LogisticRegression
from model import Model

class LogisticRegressionModel(Model):
    def __init__(self, **kwargs):
        """
        Initialise un modèle de régression logistique.
        kwargs : arguments passés à sklearn.linear_model.LogisticRegression
        """
        lr_model = LogisticRegression(**kwargs)
        super().__init__(lr_model)