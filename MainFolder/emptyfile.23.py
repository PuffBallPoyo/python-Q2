noms = input("Entrez vos prénoms et votre nom : ")
liste_noms = noms.split(" ")

prénom,*_,nom = liste_noms

print("Bienvenue",prénom,nom)