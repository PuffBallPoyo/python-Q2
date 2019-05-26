#Écrivez le script qui permet de remplir une liste de courses :
#Dans un premier temps, demandez à l’utilisateur de rentrer ce dont il a besoin ainsi
#que la quantité jusqu’à ce qu’il rentre « fini ». Affichez ensuite sa liste

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