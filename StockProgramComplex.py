# Simple programme qui permet de gerer un stock de produits
# Vous pouvez voir le stock, ajouter ou supprimer des produits

class StockManager:
    def __init__(self):
        self.__stock = {}

    def getStock(self):
        return self.__stock
    
    def ajouterAuStock(self, nomDuProduit, quantite):
        if nomDuProduit in self.__stock: # produit existant
            self.__stock[nomDuProduit] = self.__stock[nomDuProduit] + int(quantite) 
        else: # nouveau produit
            self.__stock[nomDuProduit] = int(quantite)

    def supprimerDuStock(self, nomDuProduit, quantite):
        suppressionReussie = False

        if nomDuProduit in self.__stock:
            self.__stock[nomDuProduit] = self.__stock[nomDuProduit] - int(quantite)
            suppressionReussie = True

        return suppressionReussie

class StockUI:
    def __init__(self):
            self.__stockManager = StockManager()
    def executerCommande(self, commande):
        quitterProgramme = False

        if commande == '1':
            print(f"Voici votre stock: \n {self.__stockManager.getStock()}")
        elif commande == '2':
            nouveauProduit = input("\nQue voulez vous ajouter au stock ? \n")
            quantiteNouveauProduit = input(f"\nCombien de {nouveauProduit} voulez-vous ajouter ? \n")
            self.__stockManager.ajouterAuStock(nouveauProduit, quantiteNouveauProduit)
            print(f"{quantiteNouveauProduit} {nouveauProduit} ont ete ajoutes au stock")
        elif commande == '3':
            print(f"Voici votre stock: \n {self.__stockManager.getStock()}")
            produitASupprimer = input("\nQue voulez vous supprimer du stock ?")
            quantiteASupprimer = input("\nCombien voulez-vous en supprimer ?")

            suppressionReussie = self.__stockManager.supprimerDuStock(produitASupprimer, quantiteASupprimer)
            if suppressionReussie:
                print(f"{quantiteASupprimer} {produitASupprimer} ont ete supprimes")
                print(f"Il reste desormais {self.__stock.get(produitASupprimer, 0)} {produitASupprimer}")
            else:
                print("Le produit n'est pas en stock, rien n'a ete supprime")
        elif commande == '4':
            print("Merci d'avoir utilise le stock manager !")
            quitterProgramme = True
        
        return quitterProgramme

if __name__ == "__main__":
    print("Logiciel de stock démarré !")
    stockUI = StockUI()
    quitterProgramme = False

    while not quitterProgramme:
        print("\nListe des commandes possibles : 1 = Montrer stock, 2 = Ajouter un produit au stock, 3 = Supprimer un produit du stock, 4 = Quitter le programme \n")
        nouvelleCommande = input("\nQue voulez-vous faire ?\n")
        try:
            quitterProgramme = stockUI.executerCommande(nouvelleCommande)
        except Exception as e:
            print(f"Une erreur est survenue : {repr(e)}")
            print()
            print("Veuillez reessayer")
        