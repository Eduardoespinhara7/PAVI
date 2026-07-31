import math

def f(x):
    return math.exp(x)

def riemann(f, a, b, n):
    
    dx = (b - a)/n
    soma = 0
    for i in range(n):
        x = a + i * dx
        soma += f(x)
    return soma * dx

a = 0
b = 1

valor_exato = math.e - 1

valores_n = [10, 100, 1000]

print(f"{'n':<6}{'Valor Aproximado':<22}{'Valor Exato':<20}{'Erro Absoluto'}")

for n in valores_n:
    resultado = riemann(f, a, b, n)
    erro = abs(valor_exato - resultado)

    print(f"{n:<6}{resultado:<22.10f}{valor_exato:<20.10f}{erro:.10f}")