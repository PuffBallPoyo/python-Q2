nb = int(input("Tapez un nombre pour en afficher la table de multiplication:"))

table = range(nb, (nb*10)+1, nb)

for i in table :
    print(nb ,'*' ,table.index(i)+1, '=', i,)