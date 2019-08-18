#Custom exercise
#Script qui permet de faire passer une commande Otacos et qui permet d'afficher le prix de chaque commande, il est ensuite

order_finished = False
order = {
        "Size" : "",
        "Meat" : "",
        "Sauce" : "",
        "Suppl" : "",
        "Drink" : ""
}

while order_finished != True :
    suppl = []
    ch = ''
    i=0
    print("Bienvenu chez Otacos!")
    print("Veuillez composer votre Otacos.")
    order['Size'] = input("Quelle taille voulez-vous? 'M','L','XL' ou 'XXL' \n")
    order['Meat']= (input("Quelle viande voulez-vous? (Choisissez deux fois) \n'Poulet','Nuggets','Haché,'Cordon bleu','Merguez'\n"),input())
    order['Sauce']= (input("Quelle sauce voulez-vous? (Choisissez deux fois) \n'Mayo','Ketchup','Barbecue','Biggy','Curry'\n"),input())
    while ch != 'fini' :
        ch = input("Quels suppléments voulez-vous? 'Cheddar','Raclette','Chèvre','Oeuf','Champignons'\n(Tapez 'fini' lorsque vous avez fini)\n")
        suppl.append(ch)
        i+=1
    suppl.remove('fini')
    order['Suppl'] = suppl
    order['Drink'] = input("Quelle boisson voulez vous ?\n")

    print("Résumé de votre commande")
    for itemtype,content in order.items() :
        print(itemtype,':',content)
    ch = input("La commande est elle exacte? Oui/Non\n")
    if ch == 'Oui' or ch == 'oui' :
        order_finished = True
        print("Merci d'avoir commandé chez Otacos!")
    elif ch == 'Non' or ch == 'non' : 
        print("Veuillez recommencer...")