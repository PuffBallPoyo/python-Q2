#Prend en entrée plusieurs noms et prénoms et affiche seulement 
#le premier et le dernier nom en utilisant la destructuration

noms = input("Entrez vos prénoms et votre nom : ")
liste_noms = noms.split(" ") #Sépare un string et met chaque élément dans une liste

prénom,*_,nom = liste_noms #Affecte le premier nom et le dernier nom de la liste et affecte le reste à une variable facultative

print("Bienvenue",prénom,nom)