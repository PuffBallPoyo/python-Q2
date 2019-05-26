#Script qui permet de faire une liste de courses grâce aux entrées de l'utilisateur

liste_produits = []
liste_quantité = []

#Simulation de DO WHILE sur python
produit = input('De quoi avez-vous besoin? (Tapez "fini" pour quitter) : ')

while produit != 'fini' : #Affecte un produit et un quantité à leur listes
    liste_produits.append(produit)
    quantité = input('De quelle quantité avez-vous besoin? : ')
    liste_quantité.append(quantité)
    produit = input('De quoi avez-vous besoin? (Tapez "fini" pour quitter) : ')

#Affiche une liste de courses en itérant les deux listes simultanément
for prod,qty in zip(liste_produits,liste_quantité) :
    print(prod,':',qty)