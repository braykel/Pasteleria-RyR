
#Tema: Modulos
#Importando todo de modulo operaciones
"""import operaciones 

resultado = operaciones.sumar(10,5)
resultado_resta = operaciones.restar(10,6)
print(resultado)
print(resultado_resta)
"""

#Importando lo necesario
"""from operaciones import sumar, restar

resultado = sumar(8,4)
restas = restar(10,5)
print(resultado)
print(restas)"""


#Alias con as
"""
import operaciones as op

print(op.sumar(10,5))


"""

#colocando alias a funciones particulares de un modulo
"""from operaciones import sumar as sm

resultado = sm(10,20)
print(resultado)
"""


#Modulos estandar en Python
#Modulo math

import math
#Calculando raiz cuadrada
"""resultado = math.sqrt(25) #square root

print(resultado)"""

"""resultado = math.pow(2,3)
print(resultado)
"""

#resultado = math.pi
#resultado = math.ceil(4.2)
"""resultado = math.floor(4.9)
print(resultado)"""


import random
"""
numero = random.randint(1,10)
print(numero)
"""

"""
nombres = ["Ana", "Carlos", "Luis", "Pedro"]
ganador = random.choice(nombres)
print(ganador)
"""

#Devuelve un numero decimal entre 0 y 1
numero = random.random()
#print(numero)

from datetime import date

hoy = date.today()

print(hoy.year)


