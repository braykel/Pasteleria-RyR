#===============================
# CLASE 2 DE PYTHON
#================================

#OPERADORES DE COMPARARACION

# edad = 20
# print(edad == 20)
# print(edad == 18)
# print(edad != 18)
# print(edad >18)
# print(edad <18)
# print(edad >= 18)
# print(edad <= 18)


# print("Ana" == "Ana")

# print("Ana" == "ana")

#VALORES LOGICO
# edad = 20                                                                                                                                   
# print(True and True)
# print(True and False)
# print(True or False)
# print(False or False)
# print(edad >= 18 and edad <65)
# print(edad < 18 or adad > 65)


#CONDICION


# edad = 20

# if edad >= 18:
#     print("mayor")

# else:
#     print("menor")
    
#==ejemplo 1
# nota = 15

# if nota >= 18:
#     print("exelente")
    
# elif nota >= 13:
#     print("aprovado")
    
# elif nota >= 10:
#     print("suficiente")
# else:
#     print("desaprobado")


#PEDIR DATO CON INPUT

# numero = input("ingrese el numero ")

# print(f"el numero es {numero}")



# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# total = num1 + num2 

# print(f"el numero es {total}")

# usauario = (input("ingrese su nombre: "))
# n1 = int(input("ingresee el primer numero: "))
# n2 = int(input("ingrese el segudo numero: "))

# total = n1 * n2
# print(f"Hola {usauario} su resultado es: {total}")


#   BUCLE WHILE


# contador = 3

# while contador > 0:
    
    
#     print(f"se contar {contador} vueltas")
#     contador = contador -1
# print("fin del bucle")

# num = int(input("ingrese un numero: "))

# while 0 < num:
#     print(f"tu numero ingresado es {num}")
#     num = num -1 
    
# print("fin del programa")



#=====================
# CALCULADORA EN PYTHON
#=====================



while True:
    
    print("========================")
    print(" CALCULADORA EN PYHON")
    print("=========================")
    
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Divicion")
    print("5. Salir")
    
    
    opcion = input("ingrese la opcion: ")
    if opcion == "1":
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero:"))
        suma = num1 + num2
        print(f"La suma es: {suma}")
        
    if opcion == "2":
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero:"))
            resta = num1 - num2
            print(f"La resta es: {resta}")
            
    elif opcion == "3":
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero:"))
            multi = num1 * num2
            print(f"La multiplicacion es: {multi}")
            
    elif opcion == "4":
            num1 = int(input("ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero:"))
            division = num1 / num2
            print(f"La division es: {division}")
    elif opcion == "5":
        break
    else:
        print("opcion invalida")
        break
        
print("fin del programa")
    