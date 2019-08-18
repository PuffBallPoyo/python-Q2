import random
nb_à_trouver = random.randint (1,10)
print ("Trouver un nombre entre 1 et 10. Vous avez 3 chances")
i=0
nombre_lu = int(input("Entrez un nombre : "))
while (i<2):
    if nombre_lu == nb_à_trouver:
        print ("Trouvé !")
        i = 2
    else:
        print ("Raté...")
        nombre_lu = int(input("Entrez un nombre : "))
        i+=1
print ("Le nombre à trouver était " + str (nb_à_trouver))
