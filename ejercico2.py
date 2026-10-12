RESET = "\033[0m"
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"

NEGRO = "\033[30m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[37m"

FONDO_AZUL = "\033[44m"
FONDO_CIAN = "\033[46m"


def datos(nombre, apellido, edad, pais, genero, estatura, talento):
    print(
        f"{CIAN}Hola {RESET}{NEGRITA}{BLANCO}{nombre}{RESET}{CIAN}, "
        f"sus apellidos son {RESET}{FONDO_AZUL}{BLANCO}{NEGRITA} {apellido} {RESET}{CIAN}, "
        f"tiene {RESET}{AMARILLO}{NEGRITA}{edad}{RESET}{CIAN} años "
        f"y es de {RESET}{VERDE}{NEGRITA}{pais}{RESET}{CIAN}, "
        f"su genero es {RESET}{MAGENTA}{NEGRITA}{genero}{RESET}{CIAN}, "
        f"su estatura es {RESET}{AZUL}{NEGRITA}{estatura} m{RESET}{CIAN} "
        f"y su talento oculto es {RESET}{SUBRAYADO}{AMARILLO}{talento}{RESET}{CIAN}."
    )


nombre_usuario = input(f"{CIAN}Ingrese su nombre: {RESET}")
apellido_usuario = input(f"{CIAN}Ingrese su apellido: {RESET}")
edad_usuario = int(input(f"{CIAN}Ingrese su edad: {RESET}"))
pais_usuario = input(f"{CIAN}Ingrese su pais: {RESET}")
genero_usuario = input(f"{CIAN}Masculino / Femenino: {RESET}")
estatura_usuario = float(input(f"{CIAN}Ingrese su estatura (ej: 1.75): {RESET}"))
talento_usuario = input(f"{CIAN}Cual es su talento: {RESET}")

print()
datos(
    nombre_usuario,
    apellido_usuario,
    edad_usuario,
    pais_usuario,
    genero_usuario,
    estatura_usuario,
    talento_usuario
)
print()