#Tema Funciones
#ejemplo contidiano
"""nombre = input("Ingresa tu nombre: ")
print(f"hola , {nombre}")"""


#Creando primera funcion

"""def saludar():
    print("Hola")
    print("Bienvenido al sistema")

saludar()

saludar()"""

#Funciones con parametro
#Parametro es la variable que colocas al definir una funcion el cual espera informacion
#Argumeto es la informacion que pasas al parametro
"""def saludar(nombre,apellido): #nombres es el parametro
    print(f"hola {nombre} tu apellido es {apellido} ")

saludar("Teresa", "Perez")  #Teresa es el argumento"""


#Funciones con 2 parametros
#Importante, respetar posicion al momento de pasar los argumentos
"""def presentar(nombre,edad):
    print(f"hola, soy {nombre} y tengo {edad} años")

presentar("Elias", 21)"""


#Argumentos por nombre

"""def presentar(nombre,edad,nota):
    print(f"hola, soy {nombre} y tengo {edad} años y tengo de nota {nota}")

presentar("Carlos", 30,20)
presentar(nota=20, edad=30, nombre="Carlos")"""


#Funcion con return

"""def sumar(a,b):
    resultado = a + b
    return resultado

suma = sumar(10,5)
print(suma)"""

#o tambien hacer return directamente con print sin almacenar en variable
#print(sumar(5,70))


#Return termina la funcion
"""def ejemplo():
    print("Inicio")
    return
    print("Final")

ejemplo()"""




"""def verificar_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

resultado = verificar_edad(20)
print(resultado)"""



"""def verificar_edad(edad): 
    if edad >= 18:
        return "Mayor de edad"

    return "Menor de edad"
resul = verificar_edad(10)
print(resul)"""


# parametro con Funciones y valores predeterminado

"""def saludar(nombre="Usuario"):
    print(f"Hola {nombre}")

saludar("Carlos")
saludar()"""


#Crea una funcion con 3 parametros que imprima en pantalla un mensaje personalizado
#con el nombre del usuario, la de edad del usuario y el pais del usuario.
#Los datos deben ser proporcionados por el usuario, NO LITERALES.

"""def usuario(nombre, edad, pais, mascota):
    return f" hola  tu nombre es {nombre} y tienes {edad} años tu paies es {pais} y tienes de mascota un {mascota}"
nombre = input("ingrese su nombre: ")
edad  = int(input("ingrese su edad: "))
pais = input("ingrese su pais: ")
mascota = input("nombre de su masconta: ")
datos_personales = usuario(nombre, edad, pais, mascota)
print(datos_personales)"""
    


"""def datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    pais = input("Ingrese su país: ")
    
    print(f"Hola {nombre}, tengo {edad} años y soy de {pais}")


datos()"""


#Variables dentro de una funcion
#solo existen dentro de la funcion y se le conoce como variable local

"""def calcular():  #variable local
    numero = 10
    print(numero)
    
calcular()"""


#Variables fuera de una funcion y se le conoce como variable global

"""nombre = "Carlos"

def saludar():
    print(nombre)

saludar()"""


#Funcion que llama a otra funcion 

"""def sumar(a,b):
    return a + b
def restar(a,b):
    return a - b

def mostrar_resultado():
    resultado = sumar(10,5)
    resultado1 = restar(10,2)
    print(f"El resultado es {resultado} y la resta es {resultado1}")

mostrar_resultado()"""


#Separando responsabilidades en funciones

"""def calcular_total(precio,cantidad):
    return precio * cantidad

def mostrar_compra(nombre,precio,cantidad,pago):
    
    total = calcular_total(precio,cantidad)
    print(f"Cliente: {nombre}")
    print(f"Total: S/{total}")
    vuelto = saldo_actual(pago, total)
    
    print(f"pago: {pago} y tiene vuelto de {vuelto}")
    
def saldo_actual(pago, total):
    return pago - total 


mostrar_compra("elias", 20, 3, 200)"""

"""def calcular_total(precio, cantidad):
    return precio * cantidad

def mostrar_compra(nombre, precio, cantidad, pago):
    total = calcular_total(precio, cantidad)
    print(f"Cliente: {nombre}")
    print(f"Total: S/{total}")
    vuelto = saldo_actual(pago, total)
    print(f"Pagó: S/{pago} y tiene vuelto de S/{vuelto}")

def saldo_actual(pago, total):
    return pago - total

# Pedimos los datos al usuario
nombre = input("Ingrese su nombre: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
pago = float(input("Ingrese el monto con el que paga: "))

# Llamamos a la función con los datos ingresados
mostrar_compra(nombre, precio, cantidad, pago)"""




#Funciones anidadas

"""def principal():

    def mensaje(nom):
        return f"Hola desde la funcion interna {nom} xd "
    nose = mensaje("yordan")
    print(nose)   
    
principal()"""


#Ejercicio del profesor:
#Banco básico con validaciones



saldo = 1000.00
movimientos = []

def pedir_nombre():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío")
            continue

        if not nombre.replace(" ","").isalpha():
            print("El nombre solo debe contener letras.")
            continue

        return nombre.title()

def mostrar_menu():
    print("="*40)
    print("        BANCO PYTHON     ")
    print("="*40)
    
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Ver movimientos")
    print("5. Transferir")
    print("6. Últimos movimientos")
    print("7. Calcular interés")
    print("8. Cambiar nombre")
    print("9. Salir")
    print("="*40)

def pausar():
    input("\nPresiona Enter para volver al menú...")

def pedir_monto(mensaje):
    while True:
        entrada = input(mensaje).strip()

        if entrada.lower() == "cancelar":
            return None

        try:
            monto = float(entrada)

            if monto <= 0:
                print("El monto debe ser mayor que cero")
                continue

            return monto

        except ValueError:
            print("Ingresa monto válido por ejemplo: 150 o 150.50")

def mostrar_saldo(nombre,saldo):
    print(f"\n{nombre}, tu saldo actual es S/{saldo:.2f}")

def depositar(saldo):
    print("\n ==DEPÓSITO==")
    print("Escribe 'cancelar' para regresar al menú.")

    monto = pedir_monto("Monto a depositar: S/")

    if monto is None:
        print("Depósito cancelado.")
        return saldo

    saldo += monto
    movimientos.append(f"Depósito de S/{monto:.2f}")

    print("\nDepósito realizado correctamente.")
    print(f"Nuevo saldo: S/{saldo:.2f}")
    return saldo

def retirar(saldo):
    print("\n ==RETIRO==")
    print("Escribe 'cancelar' para regresar al menú.")

    while True:
        monto = pedir_monto("Monto a retirar: S/")

        if monto is None:
            print("Retiro cancelado")
            return saldo

        if monto > saldo:
            print(f"Saldo insuficiente. Actualmente tienes S/{saldo:.2f}")
            continue

        saldo -= monto
        movimientos.append(f"Retiro de S/{monto:.2f}")

        print("\nRetiro realizado correctamente.")
        print(f"Nuevo saldo: S/{saldo:.2f}")
        return saldo

def mostrar_movimientos():
    print("==MOVIMIENTOS==")
    if len(movimientos) == 0:
        print("Todavía no tienes movimientos.")
        return 
    
    for i, movimiento in enumerate(movimientos, start=1):
        print(f"{i}. {movimiento}")

def transferir(saldo):
    print("\n ==TRANSFERENCIA==")
    print("Escribe 'cancelar' para regresar al menú.")

    destinatario = input("Ingresa el nombre del destinatario: ").strip()
    monto = pedir_monto("Monto a transferir: S/")

    if monto is None:
        print("Transferencia cancelada.")
        return saldo

    if monto > saldo:
        print(f"Saldo insuficiente. Actualmente tienes S/{saldo:.2f}")
        return saldo

    saldo -= monto
    movimientos.append(f"Transferencia de S/{monto:.2f} a {destinatario}")
    print(f"\nTransferencia realizada correctamente a {destinatario}.")
    print(f"Nuevo saldo: S/{saldo:.2f}")
    return saldo

def ultimos_movimientos():
    print("==ÚLTIMOS MOVIMIENTOS==")
    if len(movimientos) == 0:
        print("Todavía no tienes movimientos.")
        return
    for i, movimiento in enumerate(movimientos[-5:], start=1):
        print(f"{i}. {movimiento}")

def calcular_interes(saldo, tasa=0.05):
    interes = saldo * tasa
    print(f"\nInterés generado al {tasa*100:.0f}%: S/{interes:.2f}")
    saldo += interes
    movimientos.append(f"Interés aplicado de S/{interes:.2f}")
    return saldo

def cambiar_nombre():
    nuevo_nombre = pedir_nombre()
    print(f"Nombre actualizado correctamente a {nuevo_nombre}")
    return nuevo_nombre

def confirmar_salida():
    while True:
        respuesta = input("¿Seguro que deseas salir? (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Escribe solamente 's' o 'n'.")

# Programa principal
nombre = pedir_nombre()
print(f"\nBienvenido al Banco Python, {nombre}.")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        mostrar_saldo(nombre, saldo)
        pausar()
    elif opcion == "2":
        saldo = depositar(saldo)
        pausar()
    elif opcion == "3":
        saldo = retirar(saldo)
        pausar()
    elif opcion == "4":
        mostrar_movimientos()
        pausar()
    elif opcion == "5":
        saldo = transferir(saldo)
        pausar()
    elif opcion == "6":
        ultimos_movimientos()
        pausar()
    elif opcion == "7":
        saldo = calcular_interes(saldo)
        pausar()
    elif opcion == "8":
        nombre = cambiar_nombre()
        pausar()
    elif opcion == "9":
        if confirmar_salida():
            print(f"Hasta luego, {nombre}")
            break
        print("Regresando al menú...")
    else:
        print("Opción incorrecta, selecciona del 1 al 9")
        pausar()
