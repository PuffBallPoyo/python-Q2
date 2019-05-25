#Écrivez le script qui demande une température en Fahrenheit, et qui l’imprime en
#Celsius selon la formule suivante : 5/9 * (fahr – 32). 

fahr = float(input("Temperature en fahrenheit : "))
print("Température :",fahr,"(fahr) =",round((fahr-32)*5/9,2),"(celsius)")