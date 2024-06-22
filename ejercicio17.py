numero = 10
print("=== Mostrar los "+str(numero)+" numeros de la secuencia fibonacci ===")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print([fibonacci(i) for i in range(numero)])
