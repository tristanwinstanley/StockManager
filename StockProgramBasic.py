# Simple programme qui permet de gerer un stock de produits
# Vous pouvez voir le stock, ajouter ou supprimer des produits

#Extensions:
#Ajouter prix aux produits
#Fonctionnalite pour appliquer des soldes, par exemple, le prix de chaque produit diminue de 20%
#Refactorer code: ajouter fonctions et une classe pour rendre le code plus clair et lisible
if __name__ == "__main__":
    print("Logiciel de stock démarré !")
    stock = {}
    quitterProgramme = False

    while not quitterProgramme:
        print("\nListe des commandes possibles : 1 = Montrer stock, 2 = Ajouter un produit au stock, 3 = Supprimer un produit du stock, 4 = Quitter le programme \n")
        nouvelleCommande = input("\nQue voulez-vous faire ?\n")
        try:
            if nouvelleCommande == '1':
                print(f"Voici votre stock: \n {stock}")
            elif nouvelleCommande == '2':
                nouveauProduit = input("\nQue voulez vous ajouter au stock ? \n")
                quantiteNouveauProduit = input(f"\nCombien de {nouveauProduit} voulez-vous ajouter ? \n")
                if nouveauProduit in stock: # produit existant
                    stock[nouveauProduit] = stock[nouveauProduit] + int(quantiteNouveauProduit) 
                else: # nouveau produit
                    stock[nouveauProduit] = int(quantiteNouveauProduit)
                print(f"{quantiteNouveauProduit} {nouveauProduit} ont ete ajoutes au stock")
            elif nouvelleCommande == '3':
                print(f"Voici votre stock: \n {stock}")
                produitASupprimer = input("\nQue voulez vous supprimer du stock ?")
                quantiteASupprimer = input("\nCombien voulez-vous en supprimer ?")
                # A FAIRE: enlever produit du stock

            elif nouvelleCommande == '4':
                print("Merci d'avoir utilise le stock manager !")
                quitterProgramme = True
        except Exception as e:
            print(f"Une erreur est survenue : {repr(e)}")
            print()
            print("Veuillez reessayer")