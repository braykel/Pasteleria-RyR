#TEMA: SLICING

#texto = "programacion"


#texto[inicio:fin]
#print(texto[:5]) #progr

#Utilizando un paso en slicing
#texto[inicio:fin:paso]

#texto = "programacion"
#print(texto[0:8:2])



#Tema: Continuando con metodos de string

#metodo .title()

#Sirve para colocar la primera letra de cada palabra en mayuscula

# texto = "python es un lenguaje de programación"
# print("Mensaje normal: ", texto)
# print("Mensaje modificado: ",texto.title())

#Tambien funciona de la siguiente manera
#textoo = "pYThON ES GeNIaL"
#print(textoo.title())

#Metodo capitalize()

#mensaje = "mensaje DE la nacion"
#print(mensaje.capitalize())

#Tema: Metodo strip()

#mensaje = "    hola    "
#print(mensaje.strip())

#En este caso, strip() elimina los signos de los extremos
#texto = "!!!Hola!!!"
#print(texto)
#print(texto.strip("!"))

#Strip en este caso no elimina los signos del medio
#texto = "Hola!!! Mundo"
#print(texto)
#print(texto.strip("!"))


#Tema: .rstrip()
#rtrip() trabaja directamente en el extremo derecho
#texto = "Hola      "
#print(texto.rstrip())


#texto = "Hola!!!"
#print(texto)
#print(texto.rstrip("!"))


#TEMA: Metodo .Replace()
#Esto es la estructura de replace
#texto.replace("buscar", "reemplazar")

#texto = "Me gusta Python"
#print(texto)
#print(texto.replace("Python", "Java"))
#Replace tambien reemplaza todas las apariciones encontradas y reemplaza letras
#texto = "banana"
#print(texto.replace("a", "o"))


#TEMA: Metodo find()

#texto = "Hola mundo"
#print(texto.find("mundo"))

#Python mustra el primer match (1)
#texto = "Ptythtont"
#print(texto.find("t"))


#TEMA: Metodo .count()

#texto = "banana"
#print(texto.count("a"))

#print(texto.count("na"))

#texto = "Python esdivertido, Python es util"
#print(texto.count("Python"))
#print(texto.count("python"))


#Tema: Metodo .startswith() #para comprobar los primero cadenas del caracterer

#texto = "Python es facil"
#print(texto.startswith("Python"))

#print(texto.startswith("P"))
#print(texto.startswith("Pyt"))
#print(texto.startswith(" "))
#print(texto.startswith("facil",5))


#TEMA: endswith() #conprueba la final de la variable

archivo = "documento.pdf"
print(archivo.endswith(".pdf"))

#Ejercicio
#El usuario te pide una oracion con mas de 7 palabras en MAYUSCULA
#Tienes que imprimir en pantalla, los resultados con:
#.count() / .replace() / .startswith() / .strip() / .title()
#usa variables e imprimelas con f-strings 


# usuario = input("ingrese 7 palabras en MAYUSCULA: ")


# print( f"""
      
#       la oracion tiene {usuario.count("A")} LA LETRA 'A'
#       la oracion se remplaza {usuario.replace("HOLA", "PYTHON")}
#       la oracion contiene la letra 'P' {usuario.startswith("P")}
#       la oracion con espacios vacios y sucios {usuario.strip("!")}
#       el titulo de la oracion es:   {usuario.title()}
      
#       """)




#TEMA: CONCEPTO CONDICIONAL

#La nota es mayor a 11?
#Si la respuesta es si: "Aprobado"
#Si la respuesta no: "Desaprobado"



edad = 20
#print(edad >= 18) #True


edad = 17
#print(edad == 18)



#TEMA: if

# if edad == 18:
#     print("Es igual a 18")

# else:     
#     print("Es menor a 18")



















