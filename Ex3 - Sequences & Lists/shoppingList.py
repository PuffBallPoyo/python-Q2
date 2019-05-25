produit = ''
quantité = 0
liste_produits = []
liste_quantité = []

while True :
    produit = input('De quoi avez-vous besoin? (Tapez "fini" pour quitter) : ')
    if produit == 'fini' : break
    liste_produits.append(produit)
    quantité = input('De quelle quantité avez-vous besoin? : ')
    liste_quantité.append(quantité)

for i,j in zip(liste_produits,liste_quantité) :
    print(i,':',j)