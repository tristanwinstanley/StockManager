class StockManager:
    def __init__(self):
        self.__stock = {}

    def montrerStock(self):
        print(f"Voici votre stock: \n {self.__stock}")
    
    def ajouterAuStock(self, nomDuProduit, quantite):
        if nomDuProduit in self.__stock:
            self.__stock[nomDuProduit] = self.__stock[nomDuProduit] + int(quantite) 
        else:
            self.__stock[nomDuProduit] = int(quantite) 
        print(f"{quantite} {nomDuProduit} ont ete ajoutes au stock")

    def supprimerDuStock(self, nomDuProduit, quantite):
        if nomDuProduit in self.__stock:
            self.__stock[nomDuProduit] = self.__stock[nomDuProduit] - int(quantite)
            print(f"{quantite} {nomDuProduit} ont ete supprimes")
            print(f"Il reste desormais {self.__stock.get(nomDuProduit, 0)} {nomDuProduit}")
        else:
            print("Le produit n'est pas en stock, rien n'a ete supprime")

    def executerCommande(self, commande):
        quitterProgramme = False

        if commande == '1':
            self.montrerStock()
        elif commande == '2':
            nouveauProduit = input("\nQue voulez vous ajouter au stock ? \n")
            quantiteNouveauProduit = input(f"\nCombien de {nouveauProduit} voulez-vous ajouter ? \n")
            self.ajouterAuStock(nouveauProduit, quantiteNouveauProduit)
        elif commande == '3':
            self.montrerStock()
            produitASupprimer = input("\nQue voulez vous supprimer du stock ?")
            quantiteASupprimer = input("\nCombien voulez-vous en supprimer ?")

            self.supprimerDuStock(produitASupprimer, quantiteASupprimer)
        elif commande == '4':
            print("Merci d'avoir utilise le stock manager !")
            quitterProgramme = True
        
        return quitterProgramme


if __name__ == "__main__":
    print("Logiciel de stock démarré !")
    stockManager = StockManager()
    quitterProgramme = False

    while not quitterProgramme:
        print("\nListe des commandes possibles : 1 = Montrer stock, 2 = Ajouter un produit au stock, 3 = Supprimer un produit du stock, 4 = Quitter le programme \n")
        nouvelleCommande = input("\nQue voulez-vous faire ?\n")
        
        quitterProgramme = stockManager.executerCommande(nouvelleCommande)