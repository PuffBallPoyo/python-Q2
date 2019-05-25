#Dans le cadre d’un jeu de stratégie, on désire savoir s’il est possible de construire des
#nouveaux bâtiments. Connaissant le nombre de bâtiments à construire nb_batiments,
#les ressources nécessaires à la construction d’un bâtiment ressources_necessaires et
#les ressources disponibles ressources_disponibles, écrivez les instructions
#(1 instruction par variable) permettant de déclarer et d’initialiser les variables
#suivantes :

#• nb_batiments_valide, qui indique si le nombre de bâtiments est compris entre 1 et
#15 ;
#• ressources_insuffisantes, qui indique si les ressources disponibles ne sont pas
#suffisantes à la construction des bâtiments ;
#• peut_construire, qui indique si la construction est réalisable, c’est-à-dire que le
#nombres de bâtiments à construire est valide et que les ressources sont suffisantes.

#Écrivez le script qui permet de demander et de récupérer les valeurs des trois variables
#utilisées ci-dessus, et ensuite de vérifier si les bâtiments peuvent être construits en
#réutilisant les différentes instructions que vous avez écrites ci-avant.

nb_batiments = int(input("Nombre de batiments : "))
ressources_necessaires = int(input("Nombre de ressources necessaires : "))
ressources_disponibles = int(input("Nombre de ressources disponibles : "))

#bloc de conditions
nb_batimens_valides = nb_batiments < 16 and nb_batiments > 0 #Renvoie True si nb_batiments remplit la condition
ressources_insuffisantes = (nb_batiments * ressources_necessaires) > ressources_disponibles #Renvoie True si la condition est remplie
peut_construire = ressources_insuffisantes == False and nb_batimens_valides == True #La même

if ressources_insuffisantes == True : 
    print("Vous n'avez pas assez de ressources !")
    print("Il vous faut",(nb_batiments*ressources_necessaires)-ressources_disponibles,"ressources en plus pour construire les bâtiments")
elif ressources_insuffisantes == False:
    print("Vous avez assez de ressources")

if peut_construire == True :
    print("Vous pouvez construire les bâtiments ^^")
elif peut_construire == False :
    print("On peut pas construire les bâtiments D:")
    if nb_batimens_valides == False :
        print("Nombre de bâtiments invalide")
