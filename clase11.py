#TUPLAS EN PYTHON

#Consultando cantidad elementos que contiene la tupla

#horario = ("Lunes","Martes","Miercoles","Jueves", "Viernes","Sabaso","Domingo")
#print(len(horario))

#consultado elemento en la tupla
#print("Viernes" in horario)

#Count() en tupla

notas = (18,16,18, 15,18)
#print(notas.count(18))

#index() en tupla

horario = ("Lunes", "Miercoles", "Viernes")
#print(horario.index("Miercoles"))

#Convirtiendo una tupla en lista

"""dias = list(horario)
dias.append("Sabado")
#print(dias)

#cambiando lista a tupla 
horario = tuple(dias)"""
#print(horario)


#Tupla con lista

alumno = ("Ana", ["Python", "Java"])
#intentando modificar la tupla con el indice 1
#print(alumno[1])
#alumno[1] = ["Python"]
#intentando modificar la lista como elemento de la tupla
#alumno[1].append("C#")
#print(alumno)

#DICCIONARIOS EN listas
#ejemplo de consulta de dato a una sola persona
datos_ana = ("Peruana", 25, "Python", True)
#print(datos_ana[2])


#Un diccionario guarda informacion utilizando pares clave : valor

alumno ={
    "nombre" : "Ana", 
    "edad" : 25 , 
    "curso" : "Python" ,
    "sexo" : "Masculino",
    "estatura" : 1.70,
    "activo" : True
}
#print(alumno["activo"])
#print(alumno["estatura"])

#metodo get para pedir informacion de un posible None

"""print(alumno.get("Correo", "No registrado"))
print(alumno.get("Cel", "no esta numero del cel"))"""

#Modificar valores en el diccionario

alumno ={
    "nombre" : "Ana", 
    "edad" : 25 , 
    "curso" : "Python" , 
    
}

alumno["edad"] = 26
alumno["curso"] = "C#"
#print(alumno)

#Agregando nuevas claves

alumno["correo"] = "ana@gmail.com"
alumno["telefono"] = 963770296
#print(alumno)


#update() en diccionarios

alumno.update({
    "edad" : 26,
    "curso" : "Python Avanzado",
    "sexo": "femenino"
})

#print(alumno)
#las claves no se pueden repetir, en todo caso se reasigna
alumno = {
    "nombre" : "Ana",
    "nombre" : "Marta"
}


#Los valores si se pueden repetir

alumno = {
    "curso_principal" : "Python",
    "curso_Secundario" : "Python"
}

#print(alumno)

#Un diccionario puede contener diferentes tipos de datos

alumno = {
    "nombre": "Ana",
    "edad" : 25,
    "promedio" : 17.5,
    "curso" : "Html",
    "activo" : True
}

#print(alumno)

#agregando mas valores a una clave
alumnos = {
    "nombre" : "Ana",
    "edad ": 25,
    "cursos": ["Python", "Java","CSS","SQL"]
}

alumnos["cursos"].append("C#")
#print(alumnos)

#utilizando una tupla en diccionario
alumnos = {
    "nombre" : "Ana",
    "edad ": 25,
    "cursos": ["Python", "Java"],
    "horario" : ("lunes", "miercoles", "viernes","Domingo")
}

#print(alumnos)

#Eliminado clave y valor con pop
alumnos = {
    "nombre" : "Ana",
    "edad ": 25,
    "telefono" : "9999999"
}

telefono_eliminado = alumnos.pop("telefono")
#print(telefono_eliminado)

#consultando las claves del diccionario alumnos
# para ver clave
"""print(alumnos.keys())
#para ver valor
print(alumnos.values())"""

#diccionarios ANIDADOS
"""codigo = "A0054"
num1 = input("ingrese la clave: ")
num2 = input("ingrese el valor: ")"""

alumnos = {
    "A001": {
        "nombre" : "Ana",
        "edad" : 25,
        "curso": "python"
    },

    "A002": {
        "nombre" : "Luis",
        "edad" : 35,
        "curso": "Java"       
    },
    "A003": {
        "nombre" : "Dario",
        "edad" : 18,
        "curso" : "Html"
    },
    "A004": {
        "nombre" : "Elias",
        "edad" : 21,
        "curso" : "Css"
    },
    
    #codigo : {
        #num1 : num2
    #}

}

#est = alumnos["A003"]
#print(f"Nombre: {est['nombre']}, Edad: {est['edad ']}, Curso: {est['curso']}")


#Accediendo a un diccionario anidado

#print(alumnos["A003"]["curso"])


#CONJUNTOS
#un conjunto ignora valores duplicados
asistentes = {"Ana", "Luis", "Carlos", "Ana", "Luis"}
#print("Ana" in asistentes)


#print(asistentes)


#conjuntos vacios con set()

asistentes = set()

#add()

asistentes = {"Ana", "Luis", "carlos"}

#para agregar un conjunto
asistentes.add("Dario")
#print(asistentes)

#update() para agregar mas elementos

asistentes.update(["Marta", "Pedro"])
#print(asistentes)

#remove() para eliminar

asistentes.remove("carlos")
#print(asistentes)

#discard() eliminar un elemento que no exite, no rompe el codigo
#si lo encuentra elimina 
asistentes.discard("Carlos")
#print(asistentes)


#Union de conjuntos

clase_python  = {"Ana", "Luis", "Carlos","Elias"}

clase_java = {"ana", "Marta", "Pedro"}

test = clase_python.union(clase_java)
#print(test)




#Estructuras de datos combinadas
#listas dentro de una lista
alumnos = [
    ["Ana", 25],
    ["Luis", 30],
    ["Carlos", 28],
    ["Dario", 24]
]

#print(alumnos[0][1])

#Lista de diccionarios


alumnos = [
    {"nombre": "Ana", "edad" : 25},
    {"nombre": "Luis", "edad" : 30},
    {"nombre": "Carlos", "edad" : 28},
    {"nombre": "Elias", "edad": 12},
]


#print(alumnos[3]["edad"])


#Diccionario de listas

curso = {
    "alumnos" : ["Ana", "Luis", "Carlos"],
    "notas" : [18, 16, 17],
    "dias" : ["lunes", "miercoles", "viernes"],
    "cursos" : ["C#","Java","Python"]
}


#print(curso["cursos"][0])

#print(test1)


#Errores con try y except

"""try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("debes ingresar un numero valido")
print("yupi pasamos")"""

try:
    edad = int(input("Ingresa tu edad: "))
    if edad > 0:
        print("Edad registrada correctamente.")
    else:
        print("La edad debe ser mayor que cero.")

except ValueError, KeyError:
    print("Debes ingresar un numero valido.")







