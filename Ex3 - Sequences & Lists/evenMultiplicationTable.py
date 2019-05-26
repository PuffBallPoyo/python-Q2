#Script qui permet d'afficher les tables de multiplication des
#nombres pairs se trouvant entre deux nombres entrés par l'utilisateur

nb1 = int(input("Tapez deux nombres pour en afficher les table de multiplication des nombres pairs:"))
nb2 = int(input())

#Vérifie la parité de chaque nombre entré
if nb1 % 2 == 0 and nb2 % 2 == 0 :
        evenRange = range(nb1,nb2,2) #Cherche des numéros pairs entre 'nb1' et 'nb2'
elif nb1 % 2 == 0 and nb2 % 2 != 0 :
        evenRange = range(nb1,nb2+1,2)
elif nb1 % 2 != 0 and nb2 % 2 == 0 :
        evenRange = range(nb1-1,nb2,2) #On met -1 pour pouvoir afficher le premier
elif nb1 % 2 != 0 and nb2 % 2 != 0 :
        evenRange = range(nb1-1,nb2+1,2)

for i in evenRange[1:len(evenRange)] : #Ignore le premier élément de 'evenRange' pour correspondre à l'énoncé
    table = range(i, (i*10)+1, i) #Genère une table de multiplication et l'affecte à la liste 'table'
    for j in table :
        print(int(j/(table.index(j)+1)) ,'*' ,table.index(j)+1, '=', j,) #Affiche la table de multiplication
