# Sistema simple de inventario

# Diccionario para guardar productos
inventario = {}

# Bucle principal
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    # Opción 1: Agregar producto
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))

        inventario[nombre] = cantidad
        print("Producto agregado correctamente.")

    # Opción 2: Mostrar inventario
    elif opcion == "2":
        print("\nInventario actual:")
        for producto, cantidad in inventario.items():
            print(producto, ":", cantidad)

    # Opción 3: Salir del programa
    elif opcion == "3":
        print("Programa finalizado.")
        break

    # Si escribe otra cosa
    else:
        print("Opción incorrecta, intenta de nuevo.")
