class StockManager:
    def __init__(self):
        self.__stock = {}

    def montrerStock(self):
        return self.__stock
    
    def ajouterAuStock(self, nomDuProduit, quantite):
        if nomDuProduit in self.__stock:
            self.__stock[nomDuProduit] = self.__stock[nomDuProduit] + quantite
        else:
            self.__stock[nomDuProduit] = quantite      

    def supprimerDuStock(self, nomDuProduit, quantite):
        if nomDuProduit in self.__stock:
            self.__stock[nomDuProduit] = self.__stock[nomDuProduit] - quantite

    def executerCommande(self, commande):
        quitterProgramme = False

        if commande == 1:
            print("Voici votre stock: ")
            self.montrerStock()
        elif commande == 2:
            print("Que voulez vous ajouter au stock ?")
            nouveauProduit = input()
            print(f"Quelle quantité de {nouveauProduit} voulez-vous ajouter ?")
            quantiteNouveauProduit = input()
            self.ajouterAuStock(nouveauProduit, quantiteNouveauProduit)
        elif commande == 3:
            print("Voici ce que vous avez en stock: ")
            self.montrerStock()
            produitASupprimer = input("Que voulez vous supprimer du stock ?")
            quantiteASupprimer = input("Combien voulez-vous en supprimer ?")

            self.supprimerDuStock(produitASupprimer, quantiteASupprimer)
        elif commande == 4:
            quitterProgramme = True
        
        return quitterProgramme


if __name__ == "__main__":
    print("Logiciel de stock démarré !")
    stockManager = StockManager()
    quitterProgramme = False

    while not quitterProgramme:
        print("Liste des commandes possibles : 1 = Montrer stock, 2 = Ajouter un produit au stock, 3 = Supprimer un produit du stock, 4 = Quitter le programme")
        nouvelleCommande = input("Que voulez-vous faire ?")
        
        quitterProgramme = stockManager.executerCommande(nouvelleCommande)