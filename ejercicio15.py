def contar_vocales(palabra):
    vocales = "aeiou"
    count = 0
    for letra in palabra:
        if letra.lower() in vocales:
            count += 1
    return count

print("La palabra 'Python' tiene", contar_vocales("Python"), "vocales.")
