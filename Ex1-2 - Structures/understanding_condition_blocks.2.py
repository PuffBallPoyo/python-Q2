prix_repas = float(input("Prix du repas : "))
nb_repas = int(input("Nombre de repas : "))
prix_total = nb_repas * prix_repas

#bloc de condition
if nb_repas >= 10 : 
    print("Reduction pour 10 repas ! ")
    prix_total *= 0.9
    print("À payer : ",prix_total,"euros")
#Réduction de 10%!