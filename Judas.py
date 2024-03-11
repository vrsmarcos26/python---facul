#empacotamento e desempacotamento de parametros

def soma (*valor): #funções -----
    r = 0
    for i in valor:
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

#----- FATORIAL -----

def fatorial (n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)

def somaLista(L): # ------= soma a lista de forma recursiva------
    print (L)
    if L ==[]:
        return 0
    else:
        return L[0] + somaLista(L[1:])

#DocString 
x = 10
print()

def escopo():
    y = x * 2
    print("x global existe fora da funcao {}")


#soma ----

print(soma(3,9))
print(soma(1,2,3,4))

#--- empacotamento ---
L = [31,77,193]
exibeforma(*L)



#------0 retorna multiplos valores -------
a = 4
b = 6
s = returnMult(a,b)
print("Resultados {}".format(s))

print(fatorial(5))
l = [1,2,3,4,5,6,7,8,9]
print(somaLista(l))
