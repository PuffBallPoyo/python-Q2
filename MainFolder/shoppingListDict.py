liste_courses = {}

print("Tapez 'fini' lorsque vous avez fini")

produit = 'wiener'
quantité = 1337

while True :
    produit = input("De quel produit avez-vous besoin? ")
    if produit == 'fini' : break
    quantité = int(input("De quel quantité avez-vous besoin? "))
    if produit in liste_courses : 
        print(produit)
        quantité += liste_courses[produit]
    liste_courses[produit] = quantité

for key in liste_courses :
    print(key, ":",liste_courses[key])