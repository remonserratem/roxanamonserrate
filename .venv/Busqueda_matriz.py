# Programa 1: Búsqueda en Arreglo Multidimensional

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):       # recorrer filas
        for j in range(len(matriz[i])): # recorrer columnas
            if matriz[i][j] == valor:
                return i, j
    return None

# Valor a buscar
valor_buscado = 5

resultado = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: Fila {resultado[0]}, Columna {resultado[1]}")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz.")
