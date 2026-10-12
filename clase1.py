
#/// PRINT() = IMPRIME MENSAJE EN PANTALLA////
#print("Hola")
#print("Bienvenidos al curso")

#IMPRIMIR TIPO DATOS

#print(10)
#print(3.5)
#print(2 + 3)

#IMPRIMIR MUCHOS VALORES
#print("Edad:", 18)
#print("Nota: ", 8.5 , "Aprobado: ", True )

#///ESTO ES UN COMENTARIO///
#desde aqui y sirve para documentar codigo dentro del codigo


"""
ESTO ES
UN COMENTARIO
CON MUCHOS SALTOS DE LINEA
"""


#Python distingue entre Mayusculas y Minculas
#print() no es lo mismo que Print() / Print() está mal escrito

#edad = 18
#print(Edad) #Esto no funciona (nameError) por que la variable edad está en minuscula




#///INDENTACIÓN///
#EJEMPLO DE INTENDACION
#edad = 20

#if edad >= 18:
#    print("Es mayor de edad")
#    print("Puede entrar")


#print("Fin del programa")




#///DATOS, VALORES, Y TIPOS///
#Que es un dato?
#"Ana" - Es un dato de texto
#18 - es un dato numérico 
#True - es un dato de verdader o falso

#print(18) - 18 es un valor
#print("Ana") - "Ana" es un valor

#LITERALES

#print(20) #literal entero
#print(3.5) #literal decimal
#print("hola") #literal de texto
#print("True") #literal de booleano
#print(None) #literal de ausencia de valor



#///TIPOS DE DATOS///

#int - entero
#print(10)
#print(-3)
#print(0)

#float - decimal 
#print(8.5)
#print(19.50)
#print(0.5)

#str - texto
#print("Ana")
#print("Lima")
#print("18")


#bool - True / False (Verdadero o Falso)

#Bool solo admite 2 valores: True y False (Valor booleano)


#NONE - AUSENCIA DE VALOR

#print(None) 


#//// FUNCION TYPE ////

#print(type(10))
#print(type(8.5))
#print(type("Ana"))
#print(type(True))
#print(type(None))


#//DIFERENCIA ENTRE TIPOS//

#10 es int
#10.0 es float
#"10" es str

#print(10 + 5) #Nos da 15 por que es una suma numerica
#print("10" + "5") #105 por que está uniendo textos
#print("10" + 5) #TypeError

#print(True) - Esto es un tipo de dato booleano
#print("True") - Esto es un tipo de dato texto
#print(type(True)) - con type() confirmamos el tipo de dato de cada uno
#print(type("True"))



#/// CONVERSIÓN DE TIPOS DE DATOS ///


#int() Convierte a entero 
#float() Convierte a decimal
#str(19) Convierte a texto
#bool() Convierte a verdadero o falso 

#print(int("18")) - Convierte a 18 en entero
#print(float("8.5")) Convierte a 8.5 a decimal
#print(type(str(20))) Convierte a 20 en texto y te arroja su tipo de dato
#print(type(int(8.9))) Convierte a 8.9 a entero y te arrija su tipo de dato





#/// VARIABLES //

#Una variable tambien  puede guardar datos
#primera_edad = 15
#segunda_edad = primera_edad
#print(segunda_edad)

#Asignacion de valores a variables
#nombre = "Ana"
#nota = 8.5
#activo = True


#REASIGNACIÓN

#edad = 18
#print(edad)

#edad = 19
#print(edad)



#/// REGLAS PARA NOMBRES ///

#Nombres valido e invalidos

#Variables con nombres validos

#edad = 18
#edad2 = 20
#_nota = 8.5
#nombre_completo = "Manuel Navarro"
#nombreCompleto = "Jazmin"



#print(edad)
#print(edad2)
#print(_nota)
#print(nombre_completo)
#print(nombreCompleto)


#Variables con nombres invalidos

#2edad = 18
#nombre completo = "Sarita"
#total-final = "100"
#Llamar a tus variables de manera correcta, Mayuscula / Minuscula
#Edad = 20
#edad = 19
#print(edad)
#print(Edad)

#BUENAS PRACTICAS PARA CREAR VARIABLES - SNAKE CASE

#nombre_completo = "Manuel"
#precio_final = 120.5
#es_mayor = True
#if_entonces = "Hola"


#BUENAS PRACTICAS PARA VARIABLES: EVITAR PALABRAS RESERVADAS

#if = "hola"
#else = "hola"
#while = "hola"
#return = "hola"
#True = "hola"


#///OPERADORES DE COMPARACIÓN //

#a = 5

#print(5 == 5) #5 es igual a 5? True
#print(5 != 3) # 5 es disntito a 3? True
#print(5 > 3) # 5 es mayor a 3? True
#print(5 < 3) # 5 es menor a 3? False
#print(5 >= 3) # 5 es mayor o igual a 3? True
#print(5 <= 3) # 5 es menor o igual a 3? False




























