# Diccionario para guardar contactos
contactos = {}

# Función para agregar contacto
def agregar_contacto(nombre, numero):
    contactos[nombre] = numero
    print("Contacto agregado correctamente.")

# Función para mostrar contactos
def mostrar_contactos():
    if len(contactos) == 0:
        print("No hay contactos guardados.")
    else:
        print("Lista de contactos:")
        for nombre, numero in contactos.items():
            print(nombre, ":", numero)

# Función para buscar contacto
def buscar_contacto(nombre):
    if nombre in contactos:
        print("Número de", nombre, ":", contactos[nombre])
    else:
        print("Contacto no encontrado.")

# Función para eliminar contacto
def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado.")
    else:
        print("Contacto no existe.")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        numero = input("Ingresa el número: ")
        agregar_contacto(nombre, numero)

    elif opcion == "2":
        mostrar_contactos()

    elif opcion == "3":
        nombre = input("Ingresa el nombre a buscar: ")
        buscar_contacto(nombre)

    elif opcion == "4":
        nombre = input("Ingresa el nombre a eliminar: ")
        eliminar_contacto(nombre)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")