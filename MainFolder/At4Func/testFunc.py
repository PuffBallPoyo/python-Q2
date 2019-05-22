# Exemple_5
a = 10
def affiche_a():
    global a
    a = 20
    print("Dans la fonction :", a)

affiche_a()
print("Hors de la fonction :", a)
