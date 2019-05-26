#Chiffre un message en utilisant le facteur de slicing

message = "Je voudrais crypter ce message sans me casser la tête !"

crypté_1 = message[::2] #Affecte un caractère de 'message' tous les 2 caractères
print(crypté_1)
crypté_2 = message[1::2]#Affecte un caractère de 'message' tous les 2 caractères en commençant par le deuxième
print(crypté_2)

for i,j in zip(crypté_1,crypté_2) : #Itération des deux messages l'un après l'autre
    print(i,end ="")
    print(j,end ="")