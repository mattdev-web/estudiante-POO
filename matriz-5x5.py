# Crear matriz vacía de 5x5
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Llenar la matriz con datos ingresados por el usuario
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        matriz[i][j] = valor

# Mostrar la matriz en forma de tabla (5 filas x 5 columnas)
print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()

