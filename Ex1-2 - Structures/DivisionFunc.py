#Écrivez le script qui, après avoir demandé et obtenu deux nombres entiers, numérateur
#et dénominateur d'une fraction, affiche le résultat.
def lis_num_denom ():
    num = int(input("Tape le numerateur : "))
    denom = int(input("Tape le denominateur : "))
    while denom == 0 :
        print("Division par 0 impossible, réessayez.")
        denom = int(input("Tape le denominateur : "))
    return (num,denom)

def affiche_res(nbs) : 
    print("Numerateur : ",nbs[0])
    print("Denominateur : ",nbs[1])
    print(nbs[0],"/",nbs[1]," = ",round(float(nbs[0]/nbs[1]),2)," = ",int(nbs[0]/nbs[1])," reste ",nbs[0]%nbs[1],sep="")
    #sep="" function removes every space on a "" when they are preceded/followed by a variable input

nb = lis_num_denom()
affiche_res(nb)