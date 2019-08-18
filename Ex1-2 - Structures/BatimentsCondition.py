#Script qui permet de demander et de récupérer les valeurs des trois variables
#utilisées ci-dessus, et ensuite de vérifier si les bâtiments peuvent être construits en
#utilisant différentes conditions.

nb_batiments = int(input("Nombre de batiments : "))
ressources_necessaires = int(input("Nombre de ressources necessaires : "))
ressources_disponibles = int(input("Nombre de ressources disponibles : "))

#bloc de conditions
nb_batiments_valides = nb_batiments < 16 and nb_batiments > 0 #Renvoie True si nb_batiments remplit la condition
ressources_insuffisantes = (nb_batiments * ressources_necessaires) > ressources_disponibles #Renvoie True si la condition est remplie
peut_construire = ressources_insuffisantes == False and nb_batiments_valides == True #La même

if ressources_insuffisantes == True : 
    print("Vous n'avez pas assez de ressources !")
    print("Il vous faut",(nb_batiments*ressources_necessaires)-ressources_disponibles,"ressources en plus pour construire les bâtiments")
elif ressources_insuffisantes == False:
    print("Vous avez assez de ressources")

if peut_construire == True : 
    print("Vous pouvez construire les bâtiments ^^")
elif peut_construire == False :
    print("On peut pas construire les bâtiments D:")
    if nb_batiments_valides == False :
        print("Nombre de bâtiments invalide")
