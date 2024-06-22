def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
numero = 5
print("El factorial del numero : "+str(numero)+" es : "+str(factorial(numero)))
