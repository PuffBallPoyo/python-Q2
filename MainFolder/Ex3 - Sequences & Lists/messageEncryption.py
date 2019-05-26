#Script qui permet de chiffrer un message en replaçant les mots dans 
#un sens spécifique grâce au slicing

message = "Je voudrais crypter ce message sans me casser la tête !"
crypté_1 = message[::2]
print(crypté_1)
crypté_2 = message[1::2]
print(crypté_2)
i=0
while i < (len(message)/2)-1 : #Avoid out of range index
    print(crypté_1[i],end ="")
    print(crypté_2[i],end ="")
    i+=1