elminster = ["Elminster", "Humain", "Magicien", 10, [13, 18, 24, 24, 18, 17]]
caracteristiquesbase = ['Nom','Race','Classe','Niveau']
caracteristiquesrpg = ['Force','Dextérité','Constitution','Intelligence','Sagesse','Charisme']
i=0
j=0

for value in elminster :
        print(caracteristiquesbase[i] ,':',value)
        i+=1
        if i > 3 : break

for value,stat in zip(elminster[4],caracteristiquesrpg) :
        print(stat ,':',value)
