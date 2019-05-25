age = int(input("donne ton âge : "))
sexe = input("donne ton sexe : ")
annee = int(input("donne l'année : "))
age_majeur = age > 0 or age > 18
sexe_valide = sexe == 'M' or sexe == 'F'
annee_est_bissextyle = annee % 4 == 0 and annee % 100 != 0 or annee %400 == 0
print("sexe :", sexe_valide, "age: ",age_majeur,)
print("annee bissextyle :",annee_est_bissextyle,)