firstname = ['Anne', 'Bastien', 'Cécile', 'Didier', 'Bastien','Cécile']
lastname = ['Smal','Bodart','Pirotte','Valentin','Boldart','Poireau']

search = []
i = 0

while True :
    inputname = input("Nom de l'élève (Entrez Q pour terminer): ")
    search.append(inputname)
    if search[i] == 'q' or search[i] == 'Q' : 
        del search[i]
        break
    i+=1

for i,j in zip (firstname,lastname) : 
    if search.count(i) <= 0 : 
        print(i,j,"n'a pas été cité(e)")
