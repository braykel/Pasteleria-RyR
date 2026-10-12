#Tema: operador ternario

#ejemplo de estructura condicional clasica
# edad = 20 

# if edad >= 18:
#     mensaje = "Mayor de edad"
# else:
#     mensaje = "Menor de edad"

# print(mensaje)


#ejemplo de operador ternario

edad = 20

mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

#print(mensaje)
#Otro ejemplo de operador ternario
nota = 20
estado = "Aprobado" if nota >= 11 else "Desaprobado" 
#print(estado)




#Tema: Match

# print("""
#       1. Consultar saldo
#       2. Depositar
#       3. Retirar
#       4. Salir
#       """)

# print("Ingresa la opcion: ")
# opcion = 2

# if opcion == 1:
#     print("Consultar saldo")

# elif opcion == 2:
#     print("Depositar")

# elif opcion == 3:
#     print("Retirar")
# elif opcion == 4:
#     print("Salir")
# else:
#     print("opcion invalida")

#Ejemplo de match

# opcion = 2

# match opcion:

#    case 1:
#        print("Consultar saldo")
#    case 2:
#        print("Depositar")

#    case 3:
#        print("Retirar")

#    case _:
#        print("Opcion invalida")

#//CALCULADORA
# while True:
#     print("=== CALCULADORA ===")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Salir")

#     opcion = int(input("Elige una opción: "))

#     match opcion:
#         case 1:
#             a = float(input("Ingresa el primer número: "))
#             b = float(input("Ingresa el segundo número: "))
#             print(f"Resultado: {a + b}")
#         case 2:
#             a = float(input("Ingresa el primer número: "))
#             b = float(input("Ingresa el segundo número: "))
#             print(f"Resultado: {a - b}")
#         case 3:
#             a = float(input("Ingresa el primer número: "))
#             b = float(input("Ingresa el segundo número: "))
#             print(f"Resultado: {a * b}")
#         case 4:
#             a = float(input("Ingresa el primer número: "))
#             b = float(input("Ingresa el segundo número: "))
#             if b != 0:
#                 print(f"Resultado: {a / b}")
#             else:
#                 print("Error: división entre cero")
#         case 5:
#             print("Saliendo de la calculadora...")
#         case _:
#             print("Opción inválida")



#////Tema : Bucle While/////

#print("Hola")
#print("Hola")
#print("Hola")
#print("Hola")
#print("Hola")

# numero = 1
# while numero <=5:
#     print(numero)
#     numero = numero + 1
#Ejercicio clase
#Operador ternario

#Estas programando el sistema de una escuela.
# Tienes la nota de un alumno 
#el cual sera un numero del 1 al 10
# y necesitas decidir si aprobo o reprobó

#- Si la nota es 6 o mas, la variable 
# resultado debe guardar el texto "Aprobado"
#- Si la nota es menor a 6, la variable
# resultado debe guardar el texto "Reprobado"
#ejemplo de operador ternario

# edad = 20
# mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
#print(mensaje)

# usuario = input("ingrese su nombre del alumno: ")
# nota = int(input("ingrese su nota del 1 al 10: "))


# nota = "Aprobado" if nota >= 6 else "Desaprobado"

# print(f"""
#        hola {usuario}  tu estas : '{nota}' en el  curo java
#        """)


#Programar un bucle con el uso de while con contador 
#Ejemplo de while:

#while numero <= 5:
#    print(numero)
#    numero = numero + 1 #Un contador no necesariamente puede aumentar en 1, podria ser2
    #o 3 o 4 o 5. Tambien podria disminuir -1

# usuario = input("ingrese su nombre: ")
# dias = 0
# while dias < 7:
#     dias = dias + 1
#     print(f" la semana tiene {dias}")
    
    
# print(f" hola {usuario} las semanas tiene {dias} dias")

# contador = 5

# while contador >= 1:
#     print(contador)
#     contador -= 1 

# total =  0

# contador = 1
# while contador <= 3:
#     numero = float(input("Ingrese un numero: "))
#     total += numero
    
#     contador += 1
# print(F"el total es {total}")

#///////Tema break//////

# numero = 1

# while numero < 10:
#     print(numero)

#     if numero == 5:
#         break

#     numero += 1

#////////////////////////////
# numero = 0

# while numero < 5:
#    numero += 1

#    if numero == 3:
#        continue

#    print(numero)

#///////////////////////////
# numero = 1

# while numero <= 3:
#     if numero == 2:
#         pass

#     print(numero)
#     numero += 1


#break - rompe el bucle
#continue - salta la iteracion
#pass - le dice a python "oye aqui no hay nada por el momento"

