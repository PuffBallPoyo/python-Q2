familles = {
    "Dupond" : {"papa" : "Bernard",
                "maman": "Isabelle",
                "enfants" :["Tom","Alice"],
                "animaux" : 2},
    "Marchal" : {"papa" : "Albert",
                "maman": "Madelaine",
                "enfants" :["Hugo"],
                "animaux" : 0},
    "Dubois" : {"papa" : "Louis",
                "maman": "Alice",
                "enfants" :[],
                "animaux" : 1},
}
print ("Ces familles n'ont pas d'enfant :")
for nom,compo in familles.items() :
    if compo["enfants"] == [] :
        print (nom)
print("Quelle famille a le plus d'animaux?")
anmax = [0,""]
for nom,compo in familles.items() :
    if compo["animaux"] > anmax[0] : 
        anmax = [compo["animaux"],nom]
print("La famille",anmax[1],"possède",anmax[0],"animaux.")