#Écrivez le script qui permet de chiffrer une chaine de caractères obtenue de l’utilisateur
#par rapport à une clé de chiffrement (également obtenue) en utilisant le chiffrement de Vigenère

base_text = input("Tapez votre texte : ")
base_key = input("Tapez votre clé de chiffrage : ")

int_text = []
int_key = []
crypt_text = []
i = 0 
j = 0

for i in base_text :
    int_text.append(ord(i))

for i in base_key : 
    int_key.append(ord(i))

print(int_text)
print(int_key)

for i in int_text :
    if i == 32 :
        crypt_text.append(32)
    else :
        if j < len(int_key)-1 :
            crypt_text.append((i-97)+(int_key[j]-97)+97)
            j=j+1
        elif j == len(int_key)-1 : 
            crypt_text.append((i-97)+(int_key[j]-97)+97)
            j=0
print(crypt_text)

for i in crypt_text :
    if i > 122 :
        i = i-26
    print(chr(i),end='')