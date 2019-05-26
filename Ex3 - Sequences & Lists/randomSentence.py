#Écrivez un script qui génère aléatoirement des phrases en utilisant des listes de mots prédéfinis.

import random

sujet = [ 'mon chat', 'le pape', 'Johnny', 'Eden Hazard', 'un serpent', 'un magicien', 'mon voisin']
verbe= ['chanteront', 'joueront', 'danseront', 'travailleront', 'feront un marathon']
temps = ['Aujourd’hui', 'Dans cent ans', 'Demain', 'Quand les poules auront des dents']
lieu = ['à Bruxelles', 'à l’école', 'au magasin', 'à la mer', 'chez moi', 'ici']
objet = ['une balle', 'un tuba', 'un ananas', 'un sac à main', 'des palmes', 'de l’or']

print(random.choice(temps) ,end=" ")
print(random.choice(sujet) ,end=" et ")
print(random.choice(sujet) ,end=" ")
print(random.choice(verbe) ,end=" avec ")
print(random.choice(objet) ,end=" ")
print(random.choice(lieu) ,end=".")

#end permet de remplacer le retour à la ligne d'un print par un caractère ou string de son choix