# Crear matriz 3x4 inicializada en 0 (asientos libres)
asientos = [[0 for j in range(4)] for i in range(3)]

while True:
    print("\n--- Reserva de Asientos ---")
    
    # Pedir datos
    f = int(input("Ingrese fila (0 a 2): "))
    c = int(input("Ingrese columna (0 a 3): "))
    
    # Validar posición
    if 0 <= f < 3 and 0 <= c < 4:
        if asientos[f][c] == 0:
            asientos[f][c] = 1
            print("Asiento reservado correctamente.")
        else:
            print("El asiento ya está reservado.")
    else:
        print("Posición inválida.")
    
    # Mostrar estado de la sala
    print("\nEstado de la sala:")
    for i in range(3):
        for j in range(4):
            print(asientos[i][j], end=" ")
        print()
    
    # Preguntar si desea continuar
    opcion = input("\n¿Desea reservar otro asiento? (s/n): ").lower()
    
    if opcion != 's':
        print("Gracias por usar el sistema de reservas ")
        break

# -- CodebyMattdev 