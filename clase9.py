#LISTA EN PYTHON

#Colecciones y creaccion de lista
#Ejemplo de lista
nombres = ["Ana", "Luis", "Carlos"]
#Una lista puede estar vacia y se crea con corchetes
nombre = []
#Una lista puede tener mezclar tipos de datos
datos = ["Carlos", 35 , 1.75 , True]

#Modificacion de lista

"""ombres = ["Ana", "Luis", "Carlos","Dario"]
nombres[3] = "Yordan"
print(nombres)"""

#Crear una lista llamada productos que contengan 5 elementos
#Mostrar en pantalla la lista
#Luego modificar la lista con algun nuevo elemento
#Mostrar pantalla la nueva lista




"""materiales  = ["cuaderno","lapizero","borrador","tajador","pintura"]

print(materiales)

materiales[0] = "Corrector"
materiales[4] = "Pinsel"

print(f"las nuevas listas actualizados son: '{materiales}' ")"""

"""Productos = ["guitas", "baterias", "microfonos", "teclados","trompeta"]
print(f"La lista de productos es: {Productos}")
Productos[0] = "violin"
print(f"La lista de productos modificada es: {Productos}")


print("-"*30)
productos = ["PAN" ,"QUESO" ,"LECHE", "HUEVO" ,"ATUN"]
print(productos)
productos[0] = "PESCADO"
print(productos)"""



#Agregar elementos a la lista
#Metodos de lista

#=========metodo .append()========

#Agrega un elemento al final de la lista
"""nombres = ["ana", "Luis"]
print(f"Lista actual: {nombres}")
nombres.append("Carlos")
nombres.append("Dario")

print(f"Lista actualizada: {nombres}")"""




#============== metodo .insert()============
#Agregar un elemento segun el indice
"""nombres = ["Ana", "Carlos"]

nombres.insert(1, "Luis")
nombres.insert(3, "Braykel")

print(nombres)"""



#==========metodo .extend()===========
#Agregar o acoplar una lista entera en otra
"""grupo1 = ["Ana", "Luis", "Maria", "Jose","Dario"]
grupo2 = ["Carlos", "Rosa", "Esther","Braykel"]

grupo1.extend(grupo2)
print(grupo1)"""

#=========================================================
#append() - agregar un elemento al final de la lista
#insert() - agregar un elemento en una posición (indice)
#extend() - agregar varios elementos en uno

#=============================================================
#Eliminando elementos
#Metodo .remove()
#Elimina un elemento directamente por su valor
"""nombres = ["Ana", "Luis", "Carlos","Josias","Dario"]
nombres.remove("Josias")
print(nombres)"""

#Ejercicio de clase:
#Crea una lista con 5 elementos y agregar al final un sexto elemento
#Despues agrega algun otro elemento por su indice 
#Finalmente elimina el cuarto valor
#append, insert, remove

"""colores = ["Rojo","Azul","Blanco","Morado","Verde"]

colores.append("Celeste")

colores.insert(2, "Amarillo")

colores.remove("Morado")

print(colores)"""



#Metodo .pop()
#Si no le agregar un valor, elimina el ultimo elemento de la lista y devuelve su valor
"""nombres = ["Ana", "Luis", "Carlitos"]

eliminado = nombres.pop()
print(nombres)
print(f"Elemento eliminado {eliminado}")"""


#Metodo .clear()

"""nombres = ["Ana", "Luis", "Carlitos","Yordan"]
nombres.clear()
print(nombres)"""


#BUSCAR Y CONTADOR CON METODOS DE LISTA
#metodo .index()


"""nombres = ["Ana", "Luis", "Carlitos"]
pos = nombres.index("Luis")
print(f"La posicion es {pos}")"""



#Metodo .count()

#Indica cuantas veces aparece un valor
"""notas = [15,18,15,12,15,12]
valor = notas.count(12)
print(f" el total de numero almacenados de 12 son {valor} ")
print(notas.count(15))"""


#Metodo .sort()
#Ordena de manera ascendente
"""numeros = [40,10,30,20,15,45]
numeros.sort()
print(numeros)

#Ordena de manera descendente
numeros = [40,10,30,20,60,50]
numeros.sort(reverse=True)
print(numeros)"""


#Metodo .reverse()

"""numeros = [10,30,20,50,40,70,60]
numeros.reverse()
print(numeros)"""


#Hay metodos que retornan un valor como resultado,
# a esos metodos se les asigna una variable
#para poteriormente usarlos segun la necesidad: === pop, .count, .index =====

#Luego hay metodos que no retornan un valor como 
# resultado, solo accionan: ====.append. .remove .reverse, .sort, etc======



#Metodo .sorted()

"""numeros = [30, 10, 20,50,40]

ordenados = sorted(numeros)
print(f"Lista original: {numeros}")
print(f"Lista actualizada: {ordenados}")"""


#Comprobando elementos
#Operador in

"""lenguajes = ["Python", "Java", "C++","C#","Rubi"]

print("Rubi" in lenguajes)"""

#Ejercicio de clase
#numeros = [50,20,40,10,30]
#Ordena la lista de menor a mayor sin modificar la lista original y comprueba
#si el numero 40 existe

"""numeros = [50,20,40,10,30]
ordenado = sorted(numeros)

print(f" la lista ordenado {ordenado}")

print(f"¿existe el numero 40? {40 in numeros}")"""
#==================================================================

"""numeros = [50, 20, 40, 10, 30]
ordenados = sorted(numeros)

print(f"Lista original: {numeros}")
print(f"Lista ordenada: {ordenados}")
print(f"¿Existe el número '40' en la lista? {40 in numeros}")"""


#not in

"""lenguajes = ["python", "Java","Html"]
print("C++" not in lenguajes)"""


#Funciones utiles para listas

#funcion len()
#Cuenta los elementos de una lista
"""nombres = ["Ana", "Pepe", "Luis", "Carlos","Dario","Josias"]
print(len(nombres))"""


#sum()
#Suma los elementos

"""notas = [15,18,17,15,32,3]
suma = sum(notas)
print(suma)"""


#min()
#Retorna el valor mas pequeño
"""notas = [15,18,17,10]
print(min(notas))"""


#funcion max()
#Te devuelve el valor mas grande
"""notas = [15,18,17,20]
maximo = max(notas)
print(maximo)"""



#Ejercicio: Inventario básico:

productos = []

while True:
    print("==== INVENTARIO BÁSICO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Cantidad de producto")
    print("5. Vaciar inventario")
    print("6. Salir")

    opcion = input("Elige una opcion: ").strip()
    
    if opcion ==  "1":
        producto = input("Ingrese el producto: ").strip().lower()

        if producto == "":
            print("No puedes ingresar un producto vacio.")
            continue

        if producto in productos:
            print("Ese producto ya existe.")


        productos.append(producto)
        print(f"{producto.title()} fue agregado al inventario.")

    elif opcion == "2":
        producto = input("Producto que deseas eliminar: ").strip().lower()

        if producto not in productos:
            print("Ese producto no existe en el inventario")
            continue

        productos.remove(producto)
        print(f"{producto.title()} fue eliminado con exito!.")

    elif opcion == "3":
        producto = input("Producto que deseas buscar: ").strip().lower()

        if producto in productos:
            print(f"{producto.title()} si está disponible")

        else:
            print(f"{producto.title()} no está registrado")

    elif opcion == "4":
        print(f"Actualmente tienes {len(productos)} productos registrados.")

    elif opcion == "5":
        print("Seguro de eliminar?")
        opcion_seguro = input("Si/no").strip().lower()

        if opcion_seguro == "si":
            productos.clear()
            print("El inventario quedó vacio.")

        else:
            print("Jaja miedoso")
            continue

    elif opcion == "6":
        print("Programa finalizado")
        break

    else:
        print("Opcion incorrecta. ")


