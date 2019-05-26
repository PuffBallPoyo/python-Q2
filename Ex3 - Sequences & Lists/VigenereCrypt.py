#Script qui permet de chiffrer un message entré par l'utilisateur grâce à la méthode de Vigènere

base_text = input("Tapez votre texte : ")
base_key = input("Tapez votre clé de chiffrage : ")

int_text = []
int_key = []
crypt_text = []
keyCount = 0

#Transforme les strings(lettres minuscules) en valeurs ASCII 
for i in base_text.lower() :
    int_text.append(ord(i))

for i in base_key.lower() : 
    int_key.append(ord(i))

for valueInt in int_text :
    if valueInt == 32 : #Garde les espaces (32 en ASCII) inchangés dans le texte chiffré
        crypt_text.append(32)
    else :
        #Itère la liste 'int_key' jusqu'a ce que le message soit totalement chiffré
        if keyCount < len(int_key)-1 : 
            crypt_text.append((valueInt-97)+(int_key[keyCount]-97)+97)
            keyCount+=1
        elif keyCount == len(int_key)-1 : #Si on arrive au bout de la liste 'int_key' on recommence à itérer dès le début
            crypt_text.append((valueInt-97)+(int_key[keyCount]-97)+97)
            keyCount=0
#On utilise cette méthode car for n'itere pas plusieurs fois une même liste

for i in crypt_text : #Affiche le message chiffré
    if i > 122 : #Réduit la valeur des caractères ASCII en dehors des lettres minuscules (97-122)
        i = i-26
    print(chr(i),end='') #Affiche les valeurs ASCII en caractères minuscules