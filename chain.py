import hashlib
import json
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


# ===============================
#   ÉTAPE 1 : Classe Block
# ===============================

class Block:
    def __init__(self, data, previous_hash="0"):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    # ===============================
    #   ÉTAPE 2 : Méthode SHA256
    # ===============================
    def calculate_hash(self):
        block_string = (
            str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    # ===============================
    #   ÉTAPE 7 : Mine Block
    # ===============================
    def mine_block(self, difficulty):
        prefix = "0" * difficulty
        while self.hash[:difficulty] != prefix:
            self.nonce += 1
            self.hash = self.calculate_hash()


# ===============================
#   BLOCKCHAIN CLASS
# ===============================

class Blockchain:
    difficulty = 4  # nombre de zéros requis

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    # Ajouter un bloc + minage
    def add_block(self, data):
        new_block = Block(data, self.get_last_block().hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    # ===============================
    #   ÉTAPE 6 : Validation
    # ===============================
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev = self.chain[i - 1]
            block = self.chain[i]

            # Hash recalculé correct ?
            if block.hash != block.calculate_hash():
                return False

            # Lien correct ?
            if block.previous_hash != prev.hash:
                return False

            # Preuve de travail ?
            if not block.hash.startswith("0" * self.difficulty):
                return False

        return True

    def to_json(self):
        return json.dumps(
            [block.__dict__ for block in self.chain],
            indent=4
        )


# ===============================
#   INTERFACE TKINTER
# ===============================

class BlockchainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mini Blockchain - Python")
        self.blockchain = Blockchain()

        # Champ d'entrée
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)

        # Bouton "Ajouter bloc"
        self.btn_add = tk.Button(master, text="Ajouter un Bloc (miner)", command=self.add_block)
        self.btn_add.pack(pady=5)

        # Bouton "Vérifier Blockchain"
        self.btn_check = tk.Button(master, text="Vérifier la Blockchain", command=self.check_chain)
        self.btn_check.pack(pady=5)

        # Zone affichage JSON
        self.text_area = ScrolledText(master, width=80, height=25)
        self.text_area.pack(pady=10)

        self.refresh_display()

    def add_block(self):
        data = self.entry.get()
        if data.strip() == "":
            data = "Bloc sans données"

        self.blockchain.add_block(data)
        self.entry.delete(0, tk.END)
        self.refresh_display()

    def check_chain(self):
        valid = self.blockchain.is_chain_valid()
        if valid:
            result = "✔️ Blockchain valide"
        else:
            result = "❌ Blockchain corrompue"
        self.text_area.insert(tk.END, "\n\n" + result)

    def refresh_display(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.blockchain.to_json())


# ===============================
#   LANCEMENT APP
# ===============================
root = tk.Tk()
app = BlockchainApp(root)
root.mainloop()