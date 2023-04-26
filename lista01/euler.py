import matplotlib.pyplot as plt
import numpy as np

def f(x): # funcao: x * cos(x) + 1
    return x * np.cos(x) + 1

def df(x): # primeira derivada: cos(x) - x * sen(x)
    return np.cos(x) - x * np.sin(x)

def reta_tangente(a, x, ff):
    return ff + df(a) * (x - a)

x = np.linspace(-1, 10, 10000)
plt.plot(x, f(x), label="f(x) = xcos(x) + 1") # função sen(x) + x

xi = 0
yi = 1
delta = 0.1

while xi <= 6:
    yi = reta_tangente(xi, xi + delta, yi)
    plt.scatter([xi], [yi], color='orange')
    xi += delta

    

plt.legend() # coloca nome nos negocio
plt.show() # faz magica