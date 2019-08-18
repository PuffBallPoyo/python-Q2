#Écrivez le script qui, après avoir demandé et obtenu deux nombres entiers, numérateur
#et dénominateur d'une fraction, affiche le résultat.

num = int(input("Tape le numerateur : "))
denom = int(input("Tape le denominateur : "))

while denom == 0 :
    print("Division par 0 impossible, réessayez.")
    denom = int(input("Tape le denominateur : "))

print("Numerateur : ",num,)
print("Denominateur : ",denom,)
print(num,"/",denom," = ",round(float(num/denom),2)," = ",int(num/denom)," reste ",num%denom,sep="")
#sep="" function removes every space on a "" when they are preceded/followed by a variable input