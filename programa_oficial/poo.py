

class Alumno:
    def __init__(self, nombre, edad, curso,deuda):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.deuda = deuda


    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Curso: {self.curso}")
        print(f"Deuda: {self.deuda}")


    def pagar(self,monto):
        self.deuda = self.deuda - monto



alumno1 = Alumno("Carlos", 22, "Python", 300)
alumno2 = Alumno("Ana", 25, "Java", 500)
alumno3 = Alumno("Luis", 20, "Python", 150)

alumno2.pagar(200)
alumno2.mostrar_datos()






