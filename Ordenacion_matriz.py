# Matriz 3x3 (segunda fila está desordenada)
matriz = [
    [9, 2, 7],
    [5, 1, 4],   # ← esta la vamos a ordenar
    [3, 8, 6]
]

fila_a_ordenar = 1  # segunda fila (índice 1)

print("Matriz original:")
for f in matriz:
    print(f)

# Bubble Sort SOLO en la fila indicada
n = len(matriz[fila_a_ordenar])
for i in range(n):
    for j in range(0, n - i - 1):
        if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
            matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = \
            matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]

print("\nFila ordenada (solo la seleccionada):")
print(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for f in matriz:
    print(f)
