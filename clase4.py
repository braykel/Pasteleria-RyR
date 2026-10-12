# TEMA: PRESEDENCIA
# print(2 + 3 ** 2)
# Orden mental:
# parentesis-potencia-multiplicacion-division-division entera y modulo
# suma y resta
# comparadores como: == / != / > /</ >= / <=
#IMPORTANCIA DE LOS PARENTESIS
#Le dice a Python que ejecutar primero
#print((2 + 3)* 4)



#OPERADORES DE ASIGNACIÓN AUMENTADA

a = 18
#print(a == 18)

# +=  -=  *=  /=

x = 10
x += 5
#print(x)


# Esto es lo que soliamos hacer: # b = b - 3
# Esto es lo que hacemos ahora 
b = 20
b -= 3
#print(b)


c = 8
c *= 2
#print(c)

r = 10
r /= 2
#print(r)

## ? TE DEBO ESTA EXPLICACION
p = 10
p //= 3
#print(p)


#OPERADORES LÓGICOS
#and , or  y not

#Operador logico True
edad = 20
tiene_entrada = True
#print(edad >= 18 and tiene_entrada)


edad2 = 20
tiene_entrada2 = False
#print(edad2 >= 18 and tiene_entrada2)
#===================================
#  MAPA MENTAL DE TRUE - FALSE
#===================================

#/////// OPERAADOR LOGICO AND////

# True and True - True
# True and False - False 
# False and True - False
# False and False - False 

#//////Operador logico OR /////

es_feriado = False
es_fin_de_semana = True
#print(es_feriado or es_fin_de_semana)

# True or True - True
# True or False - True
# False or True - True
# False or False - False


# /////////OPERADOR LOGICO NOT/////

#activo = True
#print(not activo)

#activo = False
#print(not activo)

#\\\\\\\\\OPERADORES DE PERTENENCIA\\\\\
#in | not in.

#======Operador in=====
curso = "Python"
#print("Ptn" in curso) # SI ESTA EN LA VARIABLE LAS LETRAS
#print("Java" in curso) # NO ESTA EN LA VARIABLE LAS LETRAS

#notas = [10,15,20]
#print(15 in notas)
#print(22 in notas)

#======OPERADOR NOT IN=======

notas = [10, 15 , 20]
#print(18 not in notas)
#print(15 not in notas)


#FUNCION INPUT + conversion de dato en linea

#num1 = int(input("Ingresa primero numero: "))
#num2 = int(input("Ingresa segundo numero: "))

#suma = num1 + num2
#print(suma)


#Comillas simples
curso = 'Python'
#print(curso)

#Comillas dobles

curso = "Python"
#print(curso)

#Mensajes impresos con comillas dentro de print
#print("Me llamo Jaime")
#print('Me llamo "Ana"')
#print("Me llamo 'Ana'")

#COMILLAS TRIPELS

aviso = """ Bievenidos
al curso
de Python"""

#print(aviso)

#TEMA: CADENAS VACIAS

vacio = "     "
otro = ''
#print(vacio)
#print(otro)
#print(len(vacio))
#print(type(vacio))

#Manera diferente de imprimir con saltos de linea
#print("Hola\n a todos")

#REPETICION DE STRINGS
#print("Ja" * 4)

#======LEN()====== - Funcion incorporada de Python

#texto = "Casa"
#print(len(texto))

#///////INDICES en Python//////
texto = "Python"
#print(texto[0])
#print(texto[4])


#/////////INDICE NEGATIVOS EN Python///////

texto = "Python"
#print(texto[-1])
#print(texto[-6])



#EJEMPLO EN CLASE
#El sistema te pide tu nombre
#Luego, imprimes en pantalla la cantidad de caracteres de tu nombre len()
#Finalmente, imprimes un caracter de tu nombre por su indice
#Usa f-strings

# usuario = input("ingrese su nombre: ")
# print(f"tu nombre tiene", len(usuario) , "caracteres")
# print(f" hola {usuario} el primer indice es:", usuario[0], "y el cuarto indice es:",  usuario[4])

#METODOS DE STRINGS
#Accion que afecta al string

#Ojo!
#La mayoria de estos metodos no cambian al string original
#si no que devuelven un resultado nuevo. Si lo queremos conservar
#lo guardamos en una nueva variable


#METODO UPPER
#No afecta a la variable con string original, solo imprime
texto = "hola"
#print(texto.upper())
#print(texto)


# Aquí si afecta por que se está reasignando 
texto = "hola"
texto = texto.upper()
#print(texto)


#METODO LOWER
#NO reasigna, solo imprime
casa = "VERDE"
#print(casa.lower())
#print(casa)

#Si reasigna
casa = "VERDE"
casa_reasignada = casa.lower()
#print(casa_reasignada)


#METODO CAPITALIZE()
#Capitalize deja la primera letra en mayuscula y el resto en miniscula
#print("hola mundo".capitalize())
#print("hOLA".capitalize())

#METODO STRIP
#Quita espacios en blanco al inicio y al final

#texto = "   Ana   "
#print(texto)
#print(texto.strip())
#print(len(texto))
#print(len(texto.strip()))


 #upper
 #lower
 #strip
 #capitalize
 
# usuario = input("\ningrese su nombre: ").upper()
# apellido = input("\ningrese su apellido: ").lower()
# edad = input("\ningrese su edad: ").capitalize()

# genero = input("\ningrese su  genero: ").strip()

# print(f"""
#       su nombre es: {usuario}
#       su apellido es: {apellido}
#       su edad es: {edad}
#       su  genero es: {genero}
      
#       """)


# Solicita al usuario que ingrese su nombre completo con espacios al inicio y al final.

# Muestra el nombre en mayúsculas utilizando upper().

# Muestra el nombre en minúsculas utilizando lower().

# Elimina los espacios innecesarios al inicio y al final con strip().

# Presenta el nombre con la primera letra en mayúscula y el resto en minúscula usando capitalize().

usuario = input("ingrese su nombre completo con espacio al inicio y al final: ")
print(usuario.lower())
print(usuario.upper())
print(usuario.strip())
print(usuario.capitalize())

print(f"hola {usuario} tienes:", {len(usuario)},  "letras")