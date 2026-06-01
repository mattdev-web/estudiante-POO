class Estudiante:

    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")


# Creación de objetos

estudiante1 = Estudiante("Matías", 20, "Ingeniería en Software")
estudiante2 = Estudiante("Ana", 22, "Administración")

# Uso de métodos

estudiante1.presentarse()
estudiante1.estudiar()

print()

estudiante2.presentarse()
estudiante2.estudiar()