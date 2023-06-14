import numpy as np
import sys

def gauss(M, pivotamento = 0):
    n = M.shape[0]
    
    # pivotamento parcial
    if(pivotamento == 1):
        for i in range(n):
            max = abs(M[i][i])
            max_index = i

            for j in range(i+1, n):
                if(abs(M[j][i]) > max):
                    max = abs(M[j][i])
                    max_index = j

            if(max_index != i):
                M[[i, max_index]] = M[[max_index, i]]
 
    for i in range(n):
        piv = M[i][i]

        for j in range(n):
            if(i != j and M[j][i] != 0):
                m = (M[j][i]/piv)

                for k in range(i, n+1):
                    M[j][k] = M[j][k] - m*M[i][k]

        M[i] = (M[i]/piv)

    return M

def refinamento(M, x_barra):
    # separa matriz A e vetor b
    A = np.copy(M[:, :-1])
    b = np.copy(M[:, -1])

    # calcula vetor residuo
    r = b - (A @ x_barra)

    # adiciona vetor residuo como ultima coluna da matriz A
    A = np.c_[A, r]
    
    # resolve sistema linear Ay = r
    gauss(A, 0)
    
    # vetor solucao do sistema linear
    y = np.copy(A[:, -1])

    # recalcula x_barra
    x_barra = x_barra + y

    return [x_barra, r]


arq = open(sys.argv[1])

qnt_refinamentos = int(sys.argv[2])

pivotamento = int(sys.argv[3])

lines = arq.readlines()

A = np.array([[float(x) for x in line.split(' ')] for line in lines[1:]])

Acopy = np.copy(A)

gauss(A, pivotamento)
x_barra = np.copy(A[:, -1])

print("\nVetor solução inicial: ")
print(x_barra)

print("\n -------> Aplicando refinamento ", qnt_refinamentos, " vezes ", "com" if pivotamento == 1 else "sem", " pivotamento <-------")

for i in range(qnt_refinamentos):
    [x_barra, r] = refinamento(Acopy, x_barra)
    print("\nNorma do vetor residuo ", i+1, ": ", np.linalg.norm(r))
    
    if(i > 0):
        print("Diferença entre as normas dos vetores residuos ", i+1, " e ", i, ": ", np.linalg.norm(r) - np.linalg.norm(r_ant))
    
    r_ant = np.copy(r)
    #print("Vetor solução após refinamento ", i+1, ": ")
    #print(x_barra)




