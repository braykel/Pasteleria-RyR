
#Bucles

"""numero = 1 
while numero <= 5:
    print(numero) #1
    numero = numero + 1"""

"""contador = 0

while contador < 5:
    print("Hola")
    contador += 1"""


#Acumulador

# 1 + 2 +3 +4 +5

"""numero = 1
suma =0

while numero <= 5:
    suma = suma + numero 
    numero = numero + 1

print(f"La suma total es {suma}")"""


#Utilicen un ciclo while para sumar todos los numeros desde 1 hasta 10.
#Al finalizar muestren el resultado utilizando una f-string
"""numero = 1
suma = 0

while numero <= 10:
    suma +=  numero
    numero += 1

print(f"La suma toda de 1 a 10 es '{suma}' ")""" 






"""cantidad_a_sumar = 1
resultado = 0

while cantidad_a_sumar <= 10:
    resultado += cantidad_a_sumar  
    cantidad_a_sumar += 1      

print(f"La suma de todos los números desde 1 hasta 10 es: {resultado}")"""

#Recordatorio de break, continue, pass

"""numero = 1

while numero <= 10:

    if numero == 5:
        break
    print(numero)
    numero += 1"""

#============================
"""numero = 1

while numero <= 10:

    if numero == 5:
        continue
    print(numero)
    numero += 1"""
#================================
"""numero = 1

while numero <= 10:

    if numero == 5:
        pass
    print(numero)
    numero += 1"""

#Iteracion = numero de vueltas

#Tema: bucle for

"""nombre = "dario","elias","josias","yordan"
for letra in nombre:
    print(letra)"""
    
    
"""for letra in "SOL":
    print(letra)"""

#Iterables = elementos que se pueden recorrer

# colores = ["rojo", "azul", "verde"]

# for color in colores:
#     print(color)


#Creen una lista llamada lenguajes con tres lenguajes de programacion y utilicen
#un ciclo for para mostrar cada lenguaje por separado.
#Agregale un mismo mensaje personalizado a cada lenguaje impreso en pantalla.
"""lenguaje = ["C#", "Rubi", "C++"]

for lenguajes in lenguaje:
    
    print(f" los lenuages mas faciles son {lenguajes}")"""



"""lenguaje = ["C#", "Rubi", "C++"]

for lenguajes in lenguaje:
    print(lenguajes)
    
    match lenguajes:   
        case "C#":
            print("fue mi primero en aprender")
        case "Rubi":
            print("dice que es facil con tu ex")
        case _:
            print("es dificil de aprender")"""


"""lenguaje =["Python", "Pascal","C++"]

for i in lenguaje:


    if i == "Python":
        print("Que bonito")

    elif i == "Pascal":
        print("Lindo")

    else:
        print("Fuerte")"""



"""lenguajes =["Python", "Pascal","C++"]

for lenguaje in lenguajes:

    match lenguaje:

        case "Python":
            print("Excelente sintaxis")

        case "Pascal":
            print("Lenguaje old school")

        case _:
            print("El padre")"""


#Range ()

# range() - nos permite representar una secuencia de numeros que for puede recorrer



"""for numero in range(1,9):
    print(numero)"""

#Utiliza range() para mostrar los numeros desde 0 hasta el 7
    

"""for numero in range(0,7):
    print(numero)"""           

#Range(inicio,fin)

"""for numero in range (10,20):
    print(numero)"""

"""inicio = 1
fin = 6 (pero no muestra el 6)"""

"""inicio = 12
fin=20

for numero in range(inicio,fin):
    print(numero)
"""

#range (inicio,fin,paso)

"""for numero in range(0,11,2):
    print(numero)"""

#inicio = 0
#fin = 11
#paso = 2"""



"""for numero in range(10,0,-1):
    print(numero)"""


#Muestren utilizando range() los numeros desde 5 hasta 50 con paso 5
for i in range(5, 51, 5):
    print(f"numero: {i} ")
# for numero in range(5, 51, 5):
#     print(f"Número: {numero}")