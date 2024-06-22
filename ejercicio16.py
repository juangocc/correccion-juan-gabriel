def calcular_promedio(numeros):
    total = sum(numeros)
    return total / len(numeros)

calificaciones = [85, 92, 78, 91, 88]
print("El promedio de las calificaciones es:", calcular_promedio(calificaciones))
