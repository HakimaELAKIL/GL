# ===============================================
# File: clinical_dataset.py
# Description: Classe pour charger et préparer le dataset clinique
# ===============================================

import pandas as pd
from sklearn.model_selection import train_test_split

class ClinicalDataset:
    def __init__(self, csv_path="./../data/dataset.csv", test_size=0.2, random_state=42):
        """
        Initialise la classe avec le chemin du CSV et les paramètres de split.
        
        Paramètres :
        ------------
        csv_path : str
            Chemin vers le fichier CSV contenant ['temperature', 'cough', 'infection']
        test_size : float
            Proportion du jeu de test (par défaut 0.2)
        random_state : int
            Seed pour reproductibilité
        """
        self.csv_path = csv_path
        self.test_size = test_size
        self.random_state = random_state

        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_and_prepare(self):
        """
        Charge les données depuis le CSV et effectue la séparation train/test.
        """
        data = pd.read_csv(self.csv_path)
        print(" Données chargées :", data.shape)
        print(data.head(), "\n")

        # Vérification des colonnes
        required_columns = {'temperature', 'cough', 'infection'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Le CSV doit contenir les colonnes : {required_columns}")

        # Séparation des features et target
        X = data[['temperature', 'cough']]
        y = data['infection']

        # Division train / test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )

        print(f" Jeu d'entraînement : {len(self.X_train)} échantillons")
        print(f" Jeu de test : {len(self.X_test)} échantillons")

        return self.X_train, self.X_test, self.y_train, self.y_test
        

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    dataset = ClinicalDataset()
    X_train, X_test, y_train, y_test = dataset.load_and_prepare()
