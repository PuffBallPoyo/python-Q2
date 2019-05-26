#Script qui permet de faire une liste de courses grâce aux entrées de l'utilisateur

liste_courses = {}

print("Tapez 'fini' lorsque vous avez fini")

#Simulation de DO WHILE sur python
produit = input("De quel produit avez-vous besoin? ")
while produit != 'fini' :
    quantité = int(input("De quel quantité avez-vous besoin? "))
    if produit in liste_courses : #Si le produit entré à déja été affecté dans le dico, il ajoute simplement la quantité
        quantité += liste_courses[produit]
    liste_courses[produit] = quantité
    produit = input("De quel produit avez-vous besoin? ")

for key in liste_courses : #Affiche la liste de courses en itérant chaque élément ainsi que sa clé
    print(key, ":",liste_courses[key])