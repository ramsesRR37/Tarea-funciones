def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    else:
        return numeros_ordenados[medio]

def calcular_moda(numeros):
    frecuencia = {}
    for num in numeros:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    
    max_frecuencia = max(frecuencia.values())
    modas = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    return modas

numeros = []

n=int(input("indica la cantidad de numeros a ingresar: "))
for i in range (n):
    num=int(input(f"Numero # {i+1}: "))
    numeros.append(num)


media = calcular_media(numeros)
mediana = calcular_mediana(numeros)
moda = calcular_moda(numeros)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")