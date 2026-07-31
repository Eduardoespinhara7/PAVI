import math

def f(x):
    return math.sin(x)

def trapezio_composto(f, a, b, n):
    dx = (b-a)/n
    soma = 0
    for i in range(n):
        x_i = a + i * dx
        x_ip1 = a + (i+1) * dx

        soma += f(x_i) + f(x_ip1)
    return soma * (dx/2)
a = 0
b = math.pi
n_valores = [10,20,100]
valor_exato = 2


print("n\tAproximação\tValor Exato\t\tErro Absoluto")

for n in n_valores:
    resultado = trapezio_composto(f, a, b, n)
    erro = abs(valor_exato - resultado)
    print(f"{n}\t{resultado:.10f}\t{valor_exato:.10f}\t\t{erro:.10f}")

