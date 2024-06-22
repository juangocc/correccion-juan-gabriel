def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        print(palabra, "es un palíndromo")
    else:
        print(palabra, "no es un palíndromo")

es_palindromo("radar")
