import matplotlib.pyplot as plt
import numpy as np

def f(x): # funcao: sen(x) + x
    return np.sin(x) + x

def df(x): # primeira derivada: cos(x) + 1
    return np.cos(x) + 1

def ddf(x): # segunda derivada: -sen(x)
    return np.sin(x) * -1

def poli_taylor(a, x): # polinomio de taylor de ordem 2
    return f(a) + df(a)*(x - a) + ddf(a)*((x-a)**2)/2 

x = np.linspace(2, 6, 10000)

ponto = 4
delta = 1.5

plt.plot(x, f(x), color='orange', label="f(x) = sen(x) + x") # função sen(x) + x

poli = lambda x : poli_taylor(ponto, x) # polinomio de taylor no ponto 

plt.plot(x, poli(x), label="p2 de taylor") # plota o polinomio no ponto

x1 = ponto - delta # ponto proximo à esquerda
x2 = ponto + delta # ponto proximo à direta

plt.scatter([x1, x2], [poli(x1), poli(x2)]) # plota os dois pontos no polinomio
plt.scatter([x1, x2], [f(x1), f(x2)], color='orange') # plota os dois pontos na funcao

plt.plot([x1, x1], [poli(x1), f(x1)], linestyle='dashed', color='k') # distancia entre (x1, p(x1)) e (x1, f(x1))
plt.plot([x2, x2], [poli(x2), f(x2)], linestyle='dashed', color='k') # distancia entre (x2, p(x2)) e (x2, f(x2))

plt.legend() # coloca nome nos negocio
plt.show() # faz magica