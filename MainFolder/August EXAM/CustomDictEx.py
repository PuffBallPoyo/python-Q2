#Custom exercise
#Script qui permet d'afficher une liste avec les initiales des participants d'un jeu et qui permet de modifier le score de chaque joueur

playerlist = {'Anne': 0, 'Bastien': 0, 'Cécile': 0, 'Didier': 0,'Zoé': 0 }
ch = "null"
while ch != "end" : 
    print("Type 'list' to show the list of players and their scores")
    print("Type 'mod' to change a player's score")
    print("Type 'end' to terminate the program")
    ch = input("/")
    if ch == "list" : 
        for name,score in playerlist.items() :
            print(name[:2],score)
        input("Press enter to continue...")
    elif ch == "mod" :
        print("Which player do you want to modify? (Type their name)")
        for name in playerlist :
            print(name)
        ch = input("/")
        print("You are modifying ",ch,"'s score",sep="")
        playerlist[ch] = int(input("New score : \n"))
