# Importation des modules tkinter et messagebox
import tkinter as tk
from tkinter import messagebox

# Définition d'une classe nommée "Puissance4"
class Puissance4:
    # Constructeur de la classe, prenant en paramètre "master" qui est la fenêtre principale
    def __init__(self, master): 
        # Conserve une référence à la fenêtre principale
        self.master = master 
        # Définition du titre de la fenêtre principale
        self.master.title("Puissance 4")  
        # Création d'un canevas pour le jeu, avec une largeur de 700 pixels, une hauteur de 600 pixels, et un fond bleu
        self.canvas = tk.Canvas(self.master, width=700, height=600, bg="blue") 
        # Package le canevas dans la fenêtre principale
        self.canvas.pack()
        # Initialise le jeu
        self.reinitialiser_partie()  

    # Fonction pour réinitialiser le jeu
    def reinitialiser_partie(self):
        # Efface le canevas
        self.canvas.delete("all")  
        # Création d'un plateau de jeu (6 lignes et 7 colonnes), toutes les cases sont vides
        self.plateau = [[0] * 7 for _ in range(6)]  
        # Le joueur 1 commence
        self.tour = 1  
        # Dessine le plateau de jeu
        self.dessiner_plateau()

    def dessiner_plateau(self):
        """Dessine le plateau de jeu"""
        # Effacer les jetons existants sur le plateau
        self.canvas.delete("jetons")
        # Parcourir chaque case du plateau
        for ligne in range(6):
            for colonne in range(7):
                # Calculer les coordonnées de la case
                x1, y1 = colonne * 100, ligne * 100
                x2, y2 = x1 + 100, y1 + 100
                # Dessiner la case
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="jetons")
                # Dessiner un jeton si nécessaire
                if self.plateau[ligne][colonne] == 1:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="red", tags="jetons")
                elif self.plateau[ligne][colonne] == 2:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="blue", tags="jetons")

    def placer_jeton(self, colonne):
        """Place un jeton dans une colonne"""
        # Parcourir chaque ligne
        for ligne in range(5, -1, -1):
            # Vérifier si la colonne est libre
            if self.plateau[ligne][colonne] == 0:
                # Placer le jeton
                self.plateau[ligne][colonne] = self.tour
                # Redessiner le plateau
                self.dessiner_plateau()
                # Vérifier si il y a un gagnant
                if self.verifier_victoire(ligne, colonne):
                    gagnant = "Joueur 1" if self.tour == 1 else "Joueur 2"
                    messagebox.showinfo("Fin de partie", f"{gagnant} remporte la partie !")
                    # Réinitialiser le jeu
                    self.reinitialiser_partie()
                # Vérifier si il y a un match nul
                elif all(self.plateau[ligne][colonne] != 0 for colonne in range(7) for ligne in range(6)):
                    messagebox.showinfo("Fin de partie", "Match nul !")
                    # Réinitialiser le jeu
                    self.reinitialiser_partie()
                else:
                    # Changer de tour
                    self.tour = 1 if self.tour == 2 else 2
                # Retourner pour empêcher de placer plusieurs jetons dans la même colonne
                return

    def verifier_victoire(self, ligne, colonne):
        """
        Vérifie si un joueur a gagné en vérifiant toutes les directions possibles:
        Horizontalement, verticalement et diagonalement.
        Retourne True si le joueur a aligné 4 jetons, False sinon.
        """
        # Directions à vérifier : horizontal, vertical, diagonale
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

        # Parcourir toutes les directions
        for d_ligne, d_colonne in directions:

            # Initialiser le compteur de jetons alignés à 1
            count = 1

            # Parcourir dans les deux sens dans la direction donnée
            for direction in (-1, 1):
                l, c = ligne + direction * d_ligne, colonne + direction * d_colonne

                # Parcourir le plateau jusqu'à ce que le joueur n'ait plus de jetons alignés
                while 0 <= l < 6 and 0 <= c < 7 and self.plateau[l][c] == self.tour:
                    count += 1
                    l, c = l + direction * d_ligne, c + direction * d_colonne

                # Si un joueur a aligné 4 jetons dans la direction donnée
                if count >= 4:
                    return True

        # Si aucun joueur n'a aligné 4 jetons dans aucune direction, la partie n'est pas gagnée
        return False

class Application:  # Classe pour l'interface graphique
    def __init__(self, root):  # Initialise l'application
        """Initialise l'application, associe un clic de souris à la fonction clic_evenement"""
        self.root = root  # Conserve une référence à la racine de l'interface
        self.jeu = Puissance4(root)  # Initialise le jeu Puissance 4
        self.root.bind("<Button-1>", self.clic_evenement)  # Association d'un clic de souris à la fonction clic_evenement

    def clic_evenement(self, event):  # Fonction appelée lorsque le joueur clique avec le bouton de la souris
        """Fonction appelée lorsque le joueur clique avec le bouton de la souris.
        Convertit la position x du clic en colonne et place un jeton dans cette colonne."""
        colonne = event.x // 100  # Convertit la position x du clic en colonne
        self.jeu.placer_jeton(colonne)  # Place un jeton dans la colonne correspondante

if __name__ == "__main__":  # Si le script est exécuté directement
    root = tk.Tk()  # Créer la racine de l'interface graphique
    app = Application(root)  # Créer une instance de la classe Application
    root.mainloop()  # Entraîner l'interface graphique en mode boucle

