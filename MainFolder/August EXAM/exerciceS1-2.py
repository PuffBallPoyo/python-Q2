#Exercice 8
#Écrivez un script qui permet de faire deviner un nombre fixé par le programmeur.
import random
#Pour nombre aléatoire(random.randint(1,10))
sp_nb = 1337 
tries = 1
print("Devinez un nombre fixe.")
print("(Vous avez",11-tries,"essai(s))")
nb_user = int(input("Essayez de deviner ce nombre :"))
nb_found = nb_user == sp_nb

while nb_found != True :
    if tries < 10 :
        if nb_user < sp_nb :
            print("Votre nombre est trop petit")
            tries+=1
            print("(Il vous reste",11-tries,"essai(s))")
            nb_user = int(input("Réessayez :"))
        elif nb_user > sp_nb :
            print("Votre nombre est trop grand")
            tries+=1
            print("(Il vous reste",11-tries,"essai(s))")
            nb_user = int(input("Réessayez :"))
        elif nb_user == sp_nb :
            break
    if tries >= 10 :
        print("Le nombre correct est",sp_nb)
        break

if tries > 1 and tries < 10:
    print("Vous avez trouvé le numéro correct en",tries,"essais !")
elif tries == 1 :
    print("Vous avez trouvé le numéro du premier coup!")