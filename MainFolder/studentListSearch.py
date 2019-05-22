name = ['Anne', 'Bastien', 'Cécile', 'Didier', 'Zoé']
search = []
i = 0

while True :
    inputname = input("Nom de l'élève (Entrez Q pour terminer): ")
    search.append(inputname)
    print(search[i])
    if search[i] == 'q' or search[i] == 'Q' : 
        del search[i]
        break
    i+=1


for i in name : 
    if search.count(i) <= 0 : 
        print(i,"n'a pas été cité(e)")
