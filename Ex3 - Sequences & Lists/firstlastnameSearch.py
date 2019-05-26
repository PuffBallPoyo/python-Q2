#Prend en entrée le nom des étudiants et renvoie une liste d'étudiants n'ayant pas été cités

firstname = ['Anne', 'Bastien', 'Cécile', 'Didier', 'Bastien','Cécile']
lastname = ['Smal','Bodart','Pirotte','Valentin','Boldart','Poireau']

search = []

#Simulation d'un DO WHILE sur python
inputname = input("Nom de l'élève (Entrez Q pour terminer): ")
while inputname != 'Q' :
    search.append(inputname)
    inputname = input("Nom de l'élève (Entrez Q pour terminer): ")

for i,j in zip (firstname,lastname) : #Affiche la liste d'étudiants qui n'ont pas été cités
    if search.count(i) <= 0 : 
        print(i,j,"n'a pas été cité(e)")
