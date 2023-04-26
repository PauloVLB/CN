import math as m
#funcao f(x) da qual vamos extrair as raizes
def f(x):
    return 4.21686 - 12.4577*x + 0.82*x*x + x*x*x

#1a derivada da funcao f(x)
def f1(x):
    return 3*x*x + 1.64*x - 12.4577

#metodo da bissecao
def bissecao(a, b):
    eps = 0.01

    m = (a + b)/2.0
    while abs(f(m)) >= eps: 
        if(f(m)*f(a) < 0):
            b = m
        else:
            a = m
        m = (a + b)/2.0
    return m

#metodo de Newton
def newton(x):
    eps = 0.01

    while abs(f(x)) >= eps:
        x = x - f(x)/f1(x)

    return x

#metodo da secante
def secante(x0, x1):
    eps = 0.01

    x = x1 - ((f(x1)*(x1 - x0))/(f(x1) - f(x0)))
    while abs(f(x)) >= eps:
        x0 = x1
        x1 = x
        x = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))

    return x

#metodo regula falsi
def regulaFalsi(x0, x1):
    eps = 0.01

    x = x1 - ((f(x1)*(x1 - x0))/(f(x1) - f(x0)))

    while abs(f(x)) >= eps:
        if(f(x)*f(x1) < 0):
            x = x1 - ((f(x1)*(x1 - x))/(f(x1) - f(x)))
        else:
            x = x - ((f(x)*(x - x0))/(f(x) - f(x0)))
        
    return x

#coloque em ... os valores iniciais
print("Bissecao:")
print(bissecao(-4.3, 4.0))
print("Newton:")
print(newton(1.2))
print("Secante:")
print(secante(2.8, 3.4))
print("Regula Falsi:")
print(regulaFalsi(0, 1))
