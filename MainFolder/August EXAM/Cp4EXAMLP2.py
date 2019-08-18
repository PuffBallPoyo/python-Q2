#1
def case_nouvelle_bombe (jA):
    return (jA["case"])
#2
def dégâts (bombe,joueur):
    if bombe [0] == joueur ["case"][0] or bombe [1] == joueur ["case"][1]:
        joueur ["pv"] -= 1
   	return (joueur)
#3
def afficher_récap (joueur1, joueur2):
    print (joueur1["nom"],joueur1["pv"],joueur2["nom"],joueur2["pv"])
