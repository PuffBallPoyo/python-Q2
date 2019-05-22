def damage(x,y) :
    return(x*y)

#x = int(input('Dégats : '))
#y = float(input('Modificateur : '))
#i = int(input('Nombre de fois à afficher : '))

print('before call')
x = damage(10,1)
print(x*x*x)
print('after call')