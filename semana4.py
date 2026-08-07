def f(x):
    return x**3
def simpson_composto(f, a, b, n):
    if n % 2 != 0:
        print("n deve ser par")
        return None
    dx = (b-a) / n

    soma = f(a) + f(b)
    for i in range(1, n):
        x = a + i * dx

        if i % 2 == 0:
            soma += 2 * f(x)
        else:
            soma += 4 * f(x)

    return (dx/ 3 )  * soma
a = 0
b = 1

valor_exato = 0.25

n_valores = [10,20,100]

print("n\tValor Aproximado\tValor Exato\tErro Absoluto")

for n in n_valores:
    resultado = simpson_composto(f, a, b, n)
    erro = abs(valor_exato - resultado)
    print(f"{n}\t{resultado:.10f}\t{valor_exato:.10f}\t{erro:.10f}")