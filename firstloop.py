nb = int(input("Nombre : "))

while True : 
    nb_correct = nb >= 0 and nb < 10
    if nb_correct == True :
        print("Correct!")
        break
    elif nb_correct == False : 
        print("Erreur...")
        nb = int(input("Nombre : "))