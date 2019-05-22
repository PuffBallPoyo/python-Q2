nb1 = int(input("Tapez deux nombres pour en afficher les table de multiplication des nombres pairs:"))
nb2 = int(input())

evenRange = range(nb1,nb2,2) #Finds even numbers between nb1 and nb2


for i in evenRange[1:len(evenRange)] :
    table = range(i, (i*10)+1, i) #Makes a multiplication table of an element in evenRange
    for j in table :
        print(int(j/(table.index(j)+1)) ,'*' ,table.index(j)+1, '=', j,) #Prints the multiplication table