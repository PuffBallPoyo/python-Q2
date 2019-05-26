#Recherche un nom sur une liste et affiche le nombre de fois que ce nom à été trouvé

name = ['Anne', 'Bastien', 'Cécile', 'Didier', 'Zoé']
search = input("Tapez le nom recherché : ")

if name.count(search) >= 1 : 
    print("Nous avons trouvé",search,name.count(search),"fois")