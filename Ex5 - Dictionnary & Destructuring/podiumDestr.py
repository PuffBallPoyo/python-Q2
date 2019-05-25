def afficher_podium(liste) :
    i = 1
    for nom in liste :
        print(i,"-",nom)
        i+=1

liste_coureurs = ['Bob','Lucas','Michel']
afficher_podium(liste_coureurs)

def afficher_podium_destr(liste) : 
    premier,deuxieme,troisieme = liste
    print("1 -",premier)
    print("2 -",deuxieme)
    print("3 -",troisieme)

afficher_podium_destr(liste_coureurs)

def qualifiés(liste) :
    del liste[-1]
    return liste

print("Les qualifiés sont : ")
for qualifiés in qualifiés(liste_coureurs) :
    print(qualifiés)

def qualifiés_struct (liste) :
    *qualifiés, disqualifiés = liste
    return liste

print("Les qualifiés sont : ")
for qualifiés in qualifiés_struct(liste_coureurs) :
    print(qualifiés)