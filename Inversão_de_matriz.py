import numpy as np

def criar_matriz(ordem):
    nova_matriz = np.zeros((ordem, ordem))

    for i in range(ordem):
        for j in range(ordem):
            if i == j:
                nova_matriz[i][j] = 1
            elif i < j:
                nova_matriz[i][j] = (i+j)/(2*ordem)
            else:
                nova_matriz[i][j] = (i-j) /ordem
    return nova_matriz

def testar_matriz(matriz_gerada, matriz_teste):
    if np.array_eqal(matriz_gerada,matriz_teste):
        print("Matriz gerada é igual a matriz teste")
    else:
        print("A matriz gerada é diferente da matriz teste")
    
matriz_teste = np.array([[1,  0,   1,  2, -1]
                         [0, -1, 1/2,  2,  0]
                         [3,  2,  -1,  4,  0]
                         [2, -2, 1/2, 5/8, 1]
                         [-1, 0,   2,  -3, 4]])
ordem = 5
matriz_resultante = criar_matriz(ordem)
print("Matriz resultante: ")
print(matriz_resultante)

print("\n Testando a matriz resultante: ")
testar_matriz(matriz_resultante, matriz_teste)
