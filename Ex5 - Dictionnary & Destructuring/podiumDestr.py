liste_coureurs = ['Bob','Lucas','Michel']
#Fonction qui affiche un podium selon la liste 'liste_coureurs'
def afficher_podium(liste) :
    i = 1
    for nom in liste :
        print(i,"-",nom)
        i+=1

afficher_podium(liste_coureurs)

#Même fonction mais en utilisant la destructuration (pas de [])
def afficher_podium_destr(liste) : 
    premier,deuxieme,troisieme = liste
    print("1 -",premier)
    print("2 -",deuxieme)
    print("3 -",troisieme)

afficher_podium_destr(liste_coureurs)

#Fonction qui retourne tous sauf le dernier élément d'une liste en entrée de fonction
def qualifiés(liste) :
    del liste[-1] #Efface le dernier élément de la liste
    return liste

print("Les qualifiés sont : ")
for qualifiés in qualifiés(liste_coureurs) :
    print(qualifiés)

#Même fonction mais en utilisant la destructuration (pas de [])
def qualifiés_struct (liste) :
    *qualifiés, disqualifiés = liste #Affecte le dernier élément de la liste à une variable
    return liste

print("Les qualifiés sont : ")
for qualifiés in qualifiés_struct(liste_coureurs) :
    print(qualifiés)