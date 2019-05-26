#Écrivez le script qui permet d’afficher la table de multiplication d’un nombre entré
#au clavier… sans utiliser de while !

nb = int(input("Tapez un nombre pour en afficher la table de multiplication:"))

table = range(nb, (nb*10)+1, nb)

for i in table :
    print(nb ,'*' ,table.index(i)+1, '=', i,)