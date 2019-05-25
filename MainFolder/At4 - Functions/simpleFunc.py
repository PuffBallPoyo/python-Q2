def damage(x,y) :
    return(x*y)

#x = int(input('Dégats : '))
#y = float(input('Modificateur : '))
#i = int(input('Nombre de fois à afficher : '))

print('before call')
res = damage(int(input ("x : " )),float(input("y : ")))
print(res*res*res)
print('after call')