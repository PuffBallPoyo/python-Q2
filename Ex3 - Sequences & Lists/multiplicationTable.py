#Affiche la table de multiplication d'un nombre entré au clavier

nb = int(input("Tapez un nombre pour en afficher la table de multiplication:"))

#Crée un range(ou liste) qui contient les caractères qui se trouvent entre 'nb' et 'nb*10' avec un écart de 'nb' à chaque fois
#Ex : si nb = 10, alors range affècte les valeurs qui se trouve entre 10 et 100 , avec un écart de 10 à chaque fois
table = range(nb, (nb*10)+1, nb) 

for i in table :
    print(nb ,'*' ,table.index(i)+1, '=', i,) #Imprime la table de multiplication
    #index trouve la position dans laquelle se trouve la valeur