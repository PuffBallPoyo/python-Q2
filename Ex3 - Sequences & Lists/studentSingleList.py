#Prend en entrée le nom des étudiants et renvoie une liste d'étudiants n'ayant pas été cités

etudiants = [('Anne','Smal'),('Bastien','Bodart'),('Pirotte','Cecile')]

#Simulation d'un DO WHILE sur python
nomEtu = input("Rentrez le nom d'un étudiant (Tapez q pour terminer): ")

while nomEtu != 'q' :
    for nom in etudiants : #Itère tous les éléments dans la liste 'etudiants'
        if nomEtu == nom[0] : #Rentre dans la condition si 'nomEtu' correspond au premier élément de la tuple
            etudiants.remove(nom) #Retire le tuple de la liste
    nomEtu = input("Rentrez le nom d'un étudiant (Tapez q pour terminer): ")

for nom,prénom in etudiants : #Itère les deux éléments de chaque tuple dans 'etudiants'
    print(nom,prénom,"n'a pas été cité(e)") 