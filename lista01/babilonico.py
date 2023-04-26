print("Insira n: ", end='')
n = int(input())

print("Insira o palpite inicial: ", end='')
x = int(input())

eps = 1e-9

e = (n - (x*x))/(2*x)

while abs(e) > eps:
    print(x)
    x += e
    e = (n - (x*x))/(2*x)

print("\nValor final:", x)