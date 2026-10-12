# Solicita al usuario tres datos:

# Su nombre completo.

# Su edad.

# Si tiene carné universitario (si/no).

# Evalúa las siguientes condiciones en orden:

# Condición principal (if): Si el estudiante tiene carné universitario
# y su edad es mayor o igual a 18, muestra un mensaje indicando 
# que puede acceder a la biblioteca universitaria.

# Condición alternativa (elif): Si no cumple lo anterior pero su
# edad es exactamente 17 o su nombre es 
# "Ana", muestra un mensaje indicando que se le otorga acceso especial.

# Caso por defecto (else): Si no cumple ninguna de las co
# ndiciones anteriores, muestra un mensaje indicando que no tiene acceso.

# Usa f-strings para personalizar los mensajes de salida con el nombre y la edad del estudiante.

usuario = input("infrese su nombre completo: ").capitalize()
edad = int(input("ingrese su edad: "))
carned_universitario = input("¿Tiene carned universitario? (si/no)")

if carned_universitario == "si" and edad >= 18:
    print(f"hola {usuario} puedes acceder a la bibilioteca universitaria ")
elif edad == 17 or usuario == "Ana":

    print(f"hola {usuario} se te otorgara algo especial")
else:
    print(f"hola {usuario} no tienes acceso ")



