import math as m
#funcao f(x) da qual vamos extrair as raizes
def f(x):
    return x - 8*x/m.sqrt(400 - x*x) - 8*x/m.sqrt(900 - x*x) 

#metodo da bissecao
def bissecao(a, b):
    eps = 0.001

    m = (a + b)/2.0
    while abs(f(m)) >= eps: 
        if(f(m)*f(a) < 0):
            b = m
        else:
            a = m
        m = (a + b)/2.0
    return m

def regulaFalsi(x0, x1):
    eps = 0.001

    x = x1 - ((f(x1)*(x1 - x0))/(f(x1) - f(x0)))

    while abs(f(x)) >= eps:
        if(f(x)*f(x1) < 0):
            x = x1 - ((f(x1)*(x1 - x))/(f(x1) - f(x)))
        else:
            x = x - ((f(x)*(x - x0))/(f(x) - f(x0)))
        
    return x

# questao 4
print("Bissecao:")
print(bissecao(1, 19))
print("Regula Falsi:")
print(regulaFalsi(1, 19))