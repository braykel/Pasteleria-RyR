#Tema: Condiciones Multiples

#edad = 20
#tiene_entrada = False

#if edad >= 18 and tiene_entrada:
#    print("Puede ingresar a la discoteca")
#else:
#    print("No puedes ingresar a la disco" )

edad = 30
tiene_entrada = False

#if edad >= 18 or tiene_entrada:
#    print("Puede ingresar a la discoteca")
#else:
#    print("No puedes ingresar a la disco" )


#Escribe un programa que solicite al usuario 3 datos
#Su nombre, su nota y si se encuentra matriculado (si/no)

#El sistema debe evaluar las siguientes condiciones en orden
#utilizando if, elif, else, operadores logicos (and , or) y f-string
#para los mensajes de salida

#1. Condicion principal (if): Si el estudiante está matriculado Y su
#nota es mayor o igual a 14, se muestra un mensaje felicitandolo por
#aprobar con excelencia

#2. Condicion alternativa (elif): Si no cumple con lo anterior pero
#su nota es exactamente 11 o su nombre es 'Carlos', se le otorgará
#acceso de excepsión

#3. Caso por defecto (else): Si no cumple ninguna de las condiciones
#anteriores, se le denegará el acceso informandole que no cumple los
#requisitos.

#Solicitar datos al usuario
# nombre = input("Ingrese su nombre: ").strip().lower()
# nota = float(input("Ingrese su nota: "))
# matriculado = input("¿Está matriculado? (si/no): ").strip().lower()


# if matriculado == "si" and nota >= 14:
#     print(f" Felicidades {nombre}, aprobaste con excelencia con una nota de {nota}.")
# elif nota == 11 or nombre == "carlos":
#     print(f" Acceso de excepción otorgado a {nombre}, tu nota es {nota}.")
# else:
#     print(f"Lo siento {nombre}, no cumples con los requisitos para aprobar. Tu nota es {nota}.")


#////NOT//////


#not # Invierte un valor booleano
#Si tenemos True, not true = False
#Si tenemos False, not False = True

# print(not True)
# print(not False)


# bloqueado = False #not transforma a un True

# if not bloqueado: #true
#     print("Puede continuar")


# edad = 20
# tiene_entrada = True
# bloqueado = False

# if edad >= 18 and tiene_entrada and not bloqueado:
#     print("Puede ingresar")

# es_admin = True
# es_moderador = False
# bloqueado = False


# if (es_admin or es_moderador) and not bloqueado:
#     print("Tiene acceso")

#///CONDICIONES ANIDADAS/////


#if anidado
# edad = 20
# tiene_entrada = True

# if edad >= 18:
#     print("Edad valida")

#     if tiene_entrada:
#         print("puede ingresar")

# edad = 20
# tiene_entrada = False

# if edad >= 18 and not tiene_entrada:
#     print("puede ingresar")
#     else:
#         print("Necesita una entrada")

#else: 
#    print("no cumple la edad minima")

#EJEMPLO:

# if edad >= 18:
#     if tiene_entrada:
#         print("Puede ingresar")
#     else:
#         print("Tiene la edad correcta, pero necesita entrada")

# else:
#     print("No cumple con la edad minima")



edad = 20

if edad >= 18:
    mensaje = "mayor de edad"

else:
    mensaje = "Menor de edad"


print(mensaje)





