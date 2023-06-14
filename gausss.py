import numpy as np
import sys

def gauss(M):
    n = M.shape[0]
    
    for i in range(n):
        piv = M[i][i]

        for j in range(n):
            if(i != j and M[j][i] != 0):
                m = (M[j][i]/piv)

                for k in range(i, n+1):
                    M[j][k] = M[j][k] - m*M[i][k]

        M[i] = (M[i]/piv)

    return M

def refinamento(M, b):
    x_barra = M.copy(M[:, -1])
    A = M.copy(M[:, :-1])
    r = b - (A @ x_barra)

        

    return 0


arq = open(sys.argv[1])
lines = arq.readlines()

A = np.array([[float(x) for x in line.split(' ')] for line in lines[1:]])
Acopy = np.copy(A)

gauss(A)

B = np.copy(A[:, -1])

print("Vetor solução: ")
print(B)

#print("\n\nVerificando os resultados...")
#n = Acopy.shape[0]
#for i in range(n):
#	var = 0.0
#	for j in range(n):
#		var += Acopy[i][j] * B[j]
#	print(var)
        
print("\n\nMatriz resultante: ")
print(A)