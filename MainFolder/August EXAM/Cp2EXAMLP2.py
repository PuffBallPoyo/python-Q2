#1.
#A
nb_dons = int (input("Combien de dons effectués ?"))
#B
montant_récolté = float (input("Total montant récolté ?"))
#C
objectif_initial_atteint = montant_récolté >=500000
#D
montant_moyen_dons = montant_récolté/nb_dons
#2.
#A
objectif_atteint = montant_récolté >= 500000
if not objectif_atteint :
  print ("Montant insuffisant")
elif objectif_atteint and montant_récolté< 600000 :
  print ("Une seule contrepartie : les bâtiments !")
else:
  print("Plusieurs contrepartie")
#B
montant_valide = float(input("Entrez un montant entre 5 et 5000 euros"))
while (montant_valide < 5 or montant_valide >5000):
  print ("Le montant doit être compris entre 5 et 5000 euros")
  montant_valide = float(input("Entrez un montant entre 5 et 5000euros"))
