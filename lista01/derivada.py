import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x*x

def df(x):
    return 2*x

def reta_tangente(a, x):
    return f(a) + df(a) * (x - a) 

x = np.linspace(0, 10, 100)

ponto = 5
delta = 2

plt.plot(x, f(x), color='orange') # função x^2 
plt.scatter([ponto], [f(ponto)], color='orange') # plota o ponto

tang = lambda x : reta_tangente(ponto, x) # reta tangente ao ponto 

plt.plot(x, tang(x)) # plota a reta tangente

p1 = ponto - delta # ponto proximo à esquerda
p2 = ponto + delta # ponto proximo à direta
plt.scatter([p1, p2], [tang(p1), tang(p2)]) # plota os dois pontos

plt.show() # faz magica