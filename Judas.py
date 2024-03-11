def soma (*valor):
    r = 0
    for i in valores:
        r += i
    return r

def exibeforma(a,b,c):
    print("1. valor = {} ".format(a))
    print("2. valor = {} ".format(b))
    print("3. valor = {} ".format(c))

def returnMult (x,y):
    ad = x + y
    su = x - y
    mu = x * y
    dv = x / y
    return(ad,su,mu,dv)

#soma -----

print(soma(3,9))
print(soma(1,2,3,4))

#--- empacotamento ---
L = [31,77,193]
exibeforma(*L)

#------0 retorna multiplos valores -------
a = 4
b = 6
s = returnMult(a,b)
print("soma {}".format(s))
