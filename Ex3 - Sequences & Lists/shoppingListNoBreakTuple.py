#Script qui permet de faire une liste de courses grâce aux entrées de l'utilisateur

liste_produits = []

#Simulation de DO WHILE sur python
produit = input('De quoi avez-vous besoin? (Tapez "fini" pour quitter) : ')

while produit != 'fini' : #Affecte un produit et un quantité à la liste 'liste_produit' sous forme de tuple
    quantité = input('De quelle quantité avez-vous besoin? : ')
    liste_produits.append((produit,quantité))
    produit = input('De quoi avez-vous besoin? (Tapez "fini" pour quitter) : ')

#Affiche une liste de courses en itérant les tuples de 'liste_produits'
for prod,qty in liste_produits :
    print(prod,':',qty)