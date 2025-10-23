if __name__ == "__main__":
    print("Logiciel de stock démarré !")
    finish = False
    inv = {}
    while not finish:
        print("\nListe des commandes possibles : 1 = Montrer stock, 2 = Ajouter un produit au stock, 3 = Supprimer un produit du stock, 4 = Quitter le programme \n")
        cmd = input("\nQue voulez-vous faire ?\n")
        try:
            if cmd == '1':
                print(f"Voici votre stock: \n {inv}")
            elif cmd == '2':
                p = input("\nQue voulez vous ajouter au stock ? \n")
                qte = input(f"\nCombien de {p} voulez-vous ajouter ? \n")
                if p in inv:
                    inv[p] = inv[p] + int(qte) 
                else:
                    inv[p] = int(qte)
                print(f"{qte} {p} ont ete ajoutes au stock")
            elif cmd == '3':
                prod = input("\nQue voulez vous supprimer du stock ?")
                qte = input("\nCombien voulez-vous en supprimer ?")

                if prod in inv:
                    inv[prod] = inv[prod] - int(qte)
                    print(f"{qte} {prod} ont ete supprimes")
                    print(f"Il reste desormais {inv.get(prod, 0)} {prod}")
                else:
                    print("Le produit n'est pas en stock, rien n'a ete supprime")
            elif cmd == '4':
                print("Merci d'avoir utilise le stock manager !")
                finish = True
        except Exception as e:
            print(f"Une erreur est survenue : {repr(e)}")
            print()
            print("Veuillez reessayer")
        