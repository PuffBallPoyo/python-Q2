#Script qui permet de de souhaiter la bienvenue à la personne en 
#citant uniquement son premier prénom et son nom de famille.

noms = input("Entrez vos prénoms et votre nom : ")
liste_noms = noms.split(" ")

prénom,*_,nom = liste_noms

print("Bienvenue",prénom,nom)