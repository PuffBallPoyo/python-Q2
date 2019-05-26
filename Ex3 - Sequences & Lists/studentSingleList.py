etudiants = [('Anne','Smal'),('Bastien','Bodart'),('Pirotte','Cecile')]


nomEtu = input("Rentrez le nom d'un étudiant (Tapez q pour terminer): ")

while nomEtu != 'q' :
    for nom in etudiants :
        if nomEtu == nom[0] :
            etudiants.remove(nom)
    nomEtu = input("Rentrez le nom d'un étudiant (Tapez q pour terminer): ")


for nom,prénom in etudiants : 
    print(nom,prénom,"n'a pas été cité(e)") 