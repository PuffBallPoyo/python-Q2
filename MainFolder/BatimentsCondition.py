nb_batiments = int(input("Nombre de batiments : "))
ressources_necessaires = int(input("Nombre de ressources necessaires : "))
ressources_disponibles = int(input("Nombre de ressources disponibles : "))

nb_batimens_valides = nb_batiments < 16 and nb_batiments > 0
ressources_insuffisantes = (nb_batiments * ressources_necessaires) > ressources_disponibles 
peut_construire = ressources_insuffisantes == False and nb_batimens_valides == True

if ressources_insuffisantes == True : 
    print("Vous n'avez pas assez de ressources !")
    print("Il vous faut",(nb_batiments*ressources_necessaires)-ressources_disponibles,"ressources en plus pour construire les bâtiments")
elif ressources_insuffisantes == False:
    print("Vous avez assez de ressources")

if peut_construire == True :
    print("Vous pouvez construire les bâtiments ^^")
elif peut_construire == False :
    print("On peut pas contruire les bâtiments D:")
    if nb_batimens_valides == False :
        print("Nombre de bâtiments invalide")
