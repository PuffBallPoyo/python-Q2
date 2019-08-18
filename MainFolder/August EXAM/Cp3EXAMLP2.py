#1.
#A
listevilles = [("Bruxelles", "Belgique"), ( "Paris", "France"), ( "Namur", "Belgique")]
#B
technique =    {"AU" : (70,36,27),
                "TI" : (79,39,44),
                "IR" : (184,110,0),
                "IG" : (119,55,54)}
#C
voyelle = ("a","A","e","E","i","I","o","O","u","U","y","Y")
#2
lettre = "Lettre aléatoire"
est_voyelle = lettre in voyelle
#3
montant = []
som = 0
for elem in montant :
    som+=elem
mont_moy = som / len (montant)
#4
nom = []
first_partie = nom[0:3]
prenom = []
second_partie = prenom [0:2]
mail = first_partie + second_partie +"@henallux.be"
#5
semaine : []
jour_hors_weekend = semaine [1:6]
for elem in jour_hors_weekend :
    print (elem [0:3])
#6
familles = {}
for nom,compo in familles.items() :
    if compo["enfants"] == [] :
        print (nom)
