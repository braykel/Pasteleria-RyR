import os
import sys
import time
from datetime import datetime

# ==========================================================
# CONSTANTES DE CONFIGURACION
# ==========================================================
SALDO_INICIAL = 1000.00
LIMITE_RETIRO_DIARIO = 500.00
MONTO_MINIMO_DEPOSITO = 1.00
MONTO_MINIMO_RETIRO = 1.00
MONTO_MINIMO_TRANSFERENCIA = 1.00
HISTORIAL_MAXIMO = 100
TASA_INTERES_ANUAL = 0.02
COMISION_TRANSFERENCIA = 0.50

# ==========================================================
# CODIGOS DE COLOR ANSI
# ==========================================================
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
FONDO_VERDE = "\033[42m"
FONDO_ROJO = "\033[41m"
FONDO_AMARILLO = "\033[43m"

# ==========================================================
# ESTADO GLOBAL
# ==========================================================
saldo = SALDO_INICIAL
movimientos = []
datos_usuario = {
    "nombre": "",
    "numero_cuenta": "",
    "fecha_apertura": "",
    "tipo_cuenta": "Ahorros"
}


# ==========================================================
# UTILIDADES DE INTERFAZ
# ==========================================================
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def color(texto, codigo):
    return f"{codigo}{texto}{RESET}"


def imprimir_linea(caracter="=", longitud=60, codigo=CIAN):
    print(color(caracter * longitud, codigo))


def imprimir_titulo(titulo, codigo=CIAN):
    imprimir_linea("=", 60, codigo)
    print(color(f"{titulo.center(60)}", codigo + NEGRITA))
    imprimir_linea("=", 60, codigo)


def imprimir_exito(mensaje):
    print(color(f"[OK] {mensaje}", VERDE + NEGRITA))


def imprimir_error(mensaje):
    print(color(f"[ERROR] {mensaje}", ROJO + NEGRITA))


def imprimir_advertencia(mensaje):
    print(color(f"[AVISO] {mensaje}", AMARILLO + NEGRITA))


def imprimir_info(mensaje):
    print(color(f"[INFO] {mensaje}", CIAN))


def pausar():
    input(color("\nPresiona Enter para volver al menu...", AMARILLO))


def animacion_carga(mensaje="Procesando", duracion=1.0):
    print(color(f"\n{mensaje}", CIAN), end="")
    for _ in range(3):
        time.sleep(duracion / 3)
        print(color(".", CIAN), end="", flush=True)
    print()


# ==========================================================
# VALIDACIONES
# ==========================================================
def pedir_nombre():
    while True:
        nombre = input(color("Ingresa tu nombre: ", CIAN)).strip()

        if nombre == "":
            imprimir_error("El nombre no puede estar vacio")
            continue

        if not nombre.replace(" ", "").isalpha():
            imprimir_error("El nombre solo debe contener letras.")
            continue

        return nombre.title()


def pedir_monto(mensaje, monto_minimo=0.01):
    while True:
        entrada = input(color(mensaje, CIAN)).strip()

        if entrada.lower() == "cancelar":
            return None

        try:
            monto = float(entrada)

            if monto <= 0:
                imprimir_error("El monto debe ser mayor que cero")
                continue

            if monto < monto_minimo:
                imprimir_error(f"El monto minimo es S/{monto_minimo:.2f}")
                continue

            return monto

        except ValueError:
            imprimir_error("Ingresa un monto valido, por ejemplo: 150 o 150.50")


def pedir_numero_cuenta():
    while True:
        numero = input(color("Ingresa el numero de cuenta destino (10 digitos): ", CIAN)).strip()

        if numero.lower() == "cancelar":
            return None

        if not numero.isdigit():
            imprimir_error("El numero de cuenta solo debe contener digitos.")
            continue

        if len(numero) != 10:
            imprimir_error("El numero de cuenta debe tener exactamente 10 digitos.")
            continue

        return numero


def confirmar_accion(mensaje):
    while True:
        respuesta = input(color(f"{mensaje} (s/n): ", AMARILLO)).strip().lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            imprimir_error("Escribe solamente 's' o 'n'.")


# ==========================================================
# GENERADORES DE DATOS
# ==========================================================
def generar_numero_cuenta():
    import random
    return "".join(str(random.randint(0, 9)) for _ in range(10))


def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def obtener_solo_fecha():
    return datetime.now().strftime("%d/%m/%Y")


# ==========================================================
# REGISTRO DE MOVIMIENTOS
# ==========================================================
def registrar_movimiento(tipo, monto, saldo_resultante, detalle=""):
    movimiento = {
        "tipo": tipo,
        "monto": monto,
        "saldo_resultante": saldo_resultante,
        "fecha": obtener_fecha_actual(),
        "detalle": detalle
    }
    movimientos.append(movimiento)

    if len(movimientos) > HISTORIAL_MAXIMO:
        movimientos.pop(0)


def calcular_retirado_hoy():
    total = 0.0
    fecha_hoy = obtener_solo_fecha()

    for movimiento in movimientos:
        if movimiento["tipo"] == "Retiro" and movimiento["fecha"].startswith(fecha_hoy):
            total += movimiento["monto"]

    return total


def calcular_total_depositado():
    total = 0.0
    for movimiento in movimientos:
        if movimiento["tipo"] == "Deposito":
            total += movimiento["monto"]
    return total


def calcular_total_retirado():
    total = 0.0
    for movimiento in movimientos:
        if movimiento["tipo"] == "Retiro":
            total += movimiento["monto"]
    return total


def calcular_promedio_movimientos():
    if len(movimientos) == 0:
        return 0.0
    total = sum(m["monto"] for m in movimientos)
    return total / len(movimientos)


# ==========================================================
# MENU PRINCIPAL
# ==========================================================
def mostrar_menu():
    limpiar_pantalla()
    imprimir_titulo("BANCO PYTHON - CAJERO AUTOMATICO", AZUL)
    print(color(f"  Usuario: {datos_usuario['nombre']}", VERDE))
    print(color(f"  Cuenta : {datos_usuario['numero_cuenta']}", VERDE))
    print(color(f"  Fecha  : {obtener_fecha_actual()}", VERDE))
    imprimir_linea("-", 60, CIAN)

    opciones = [
        ("1", "Ver saldo"),
        ("2", "Depositar"),
        ("3", "Retirar"),
        ("4", "Transferir"),
        ("5", "Ver movimientos"),
        ("6", "Ver resumen de cuenta"),
        ("7", "Consultar limite de retiro"),
        ("8", "Simular interes anual"),
        ("9", "Cambiar tipo de cuenta"),
        ("10", "Salir")
    ]

    for codigo, descripcion in opciones:
        print(color(f"  {codigo:>2}. {descripcion}", BLANCO))

    imprimir_linea("=", 60, AZUL)


# ==========================================================
# OPERACIONES BANCARIAS
# ==========================================================
def mostrar_saldo(nombre, saldo_actual):
    limpiar_pantalla()
    imprimir_titulo("CONSULTA DE SALDO", VERDE)
    print(color(f"\n  Titular       : {nombre}", BLANCO))
    print(color(f"  Cuenta        : {datos_usuario['numero_cuenta']}", BLANCO))
    print(color(f"  Tipo de cuenta: {datos_usuario['tipo_cuenta']}", BLANCO))
    imprimir_linea("-", 60, VERDE)
    print(color(f"  SALDO ACTUAL  : S/{saldo_actual:.2f}", VERDE + NEGRITA))
    imprimir_linea("=", 60, VERDE)


def depositar(saldo_actual):
    limpiar_pantalla()
    imprimir_titulo("DEPOSITO", AZUL)
    imprimir_info(f"Monto minimo: S/{MONTO_MINIMO_DEPOSITO:.2f}")
    imprimir_info("Escribe 'cancelar' para regresar al menu.")

    monto = pedir_monto("Monto a depositar: S/", MONTO_MINIMO_DEPOSITO)

    if monto is None:
        imprimir_advertencia("Deposito cancelado.")
        return saldo_actual

    animacion_carga("Procesando deposito")

    saldo_actual += monto
    registrar_movimiento("Deposito", monto, saldo_actual, "Deposito en ventanilla")

    imprimir_exito("Deposito realizado correctamente.")
    print(color(f"  Nuevo saldo: S/{saldo_actual:.2f}", VERDE + NEGRITA))

    return saldo_actual


def retirar(saldo_actual):
    limpiar_pantalla()
    imprimir_titulo("RETIRO", AMARILLO)
    imprimir_info(f"Monto minimo: S/{MONTO_MINIMO_RETIRO:.2f}")
    imprimir_info(f"Limite diario: S/{LIMITE_RETIRO_DIARIO:.2f}")
    imprimir_info("Escribe 'cancelar' para regresar al menu.")

    retirado_hoy = calcular_retirado_hoy()

    while True:
        monto = pedir_monto("Monto a retirar: S/", MONTO_MINIMO_RETIRO)

        if monto is None:
            imprimir_advertencia("Retiro cancelado")
            return saldo_actual

        if monto > saldo_actual:
            imprimir_error("Saldo insuficiente")
            print(color(f"  Actualmente tienes S/{saldo_actual:.2f}", ROJO))
            continue

        if retirado_hoy + monto > LIMITE_RETIRO_DIARIO:
            disponible = LIMITE_RETIRO_DIARIO - retirado_hoy
            imprimir_error("Excede el limite diario de retiro.")
            print(color(f"  Disponible hoy: S/{disponible:.2f}", AMARILLO))
            continue

        if not confirmar_accion(f"Confirmas retirar S/{monto:.2f}?"):
            imprimir_advertencia("Retiro cancelado por el usuario.")
            return saldo_actual

        animacion_carga("Procesando retiro")

        saldo_actual -= monto
        registrar_movimiento("Retiro", monto, saldo_actual, "Retiro en cajero")

        imprimir_exito("Retiro realizado correctamente.")
        print(color(f"  Nuevo saldo: S/{saldo_actual:.2f}", VERDE + NEGRITA))

        return saldo_actual


def transferir(saldo_actual):
    limpiar_pantalla()
    imprimir_titulo("TRANSFERENCIA", MAGENTA)
    imprimir_info(f"Monto minimo: S/{MONTO_MINIMO_TRANSFERENCIA:.2f}")
    imprimir_info(f"Comision por transferencia: S/{COMISION_TRANSFERENCIA:.2f}")
    imprimir_info("Escribe 'cancelar' para regresar al menu.")

    numero_cuenta = pedir_numero_cuenta()

    if numero_cuenta is None:
        imprimir_advertencia("Transferencia cancelada.")
        return saldo_actual

    if numero_cuenta == datos_usuario["numero_cuenta"]:
        imprimir_error("No puedes transferir a tu propia cuenta.")
        return saldo_actual

    monto = pedir_monto("Monto a transferir: S/", MONTO_MINIMO_TRANSFERENCIA)

    if monto is None:
        imprimir_advertencia("Transferencia cancelada.")
        return saldo_actual

    total_debitar = monto + COMISION_TRANSFERENCIA

    if total_debitar > saldo_actual:
        imprimir_error("Saldo insuficiente para cubrir el monto y la comision.")
        print(color(f"  Requerido: S/{total_debitar:.2f}", ROJO))
        print(color(f"  Disponible: S/{saldo_actual:.2f}", ROJO))
        return saldo_actual

    if not confirmar_accion(
        f"Confirmas transferir S/{monto:.2f} a la cuenta {numero_cuenta}?"
    ):
        imprimir_advertencia("Transferencia cancelada por el usuario.")
        return saldo_actual

    animacion_carga("Procesando transferencia")

    saldo_actual -= total_debitar
    registrar_movimiento(
        "Transferencia",
        monto,
        saldo_actual,
        f"Transferencia a cuenta {numero_cuenta} (comision S/{COMISION_TRANSFERENCIA:.2f})"
    )

    imprimir_exito("Transferencia realizada correctamente.")
    print(color(f"  Nuevo saldo: S/{saldo_actual:.2f}", VERDE + NEGRITA))

    return saldo_actual


def simular_interes(saldo_actual):
    limpiar_pantalla()
    imprimir_titulo("SIMULACION DE INTERES ANUAL", VERDE)
    imprimir_info(f"Tasa de interes anual: {TASA_INTERES_ANUAL * 100:.2f}%")
    imprimir_info(f"Saldo actual: S/{saldo_actual:.2f}")

    interes = saldo_actual * TASA_INTERES_ANUAL
    saldo_proyectado = saldo_actual + interes

    imprimir_linea("-", 60, VERDE)
    print(color(f"  Interes ganado en un anio: S/{interes:.2f}", VERDE))
    print(color(f"  Saldo proyectado: S/{saldo_proyectado:.2f}", VERDE + NEGRITA))
    imprimir_linea("=", 60, VERDE)

    if confirmar_accion("Deseas aplicar el interes a tu saldo ahora?"):
        animacion_carga("Aplicando interes")

        saldo_actual += interes
        registrar_movimiento(
            "Interes",
            interes,
            saldo_actual,
            f"Interes anual aplicado ({TASA_INTERES_ANUAL * 100:.2f}%)"
        )

        imprimir_exito("Interes aplicado correctamente.")
        print(color(f"  Nuevo saldo: S/{saldo_actual:.2f}", VERDE + NEGRITA))
    else:
        imprimir_info("No se aplico el interes.")

    return saldo_actual


def cambiar_tipo_cuenta():
    limpiar_pantalla()
    imprimir_titulo("CAMBIAR TIPO DE CUENTA", MAGENTA)
    print(color("  1. Ahorros", BLANCO))
    print(color("  2. Corriente", BLANCO))
    print(color("  3. Empresarial", BLANCO))

    opcion = input(color("\nSelecciona el tipo de cuenta: ", CIAN)).strip()

    tipos = {
        "1": "Ahorros",
        "2": "Corriente",
        "3": "Empresarial"
    }

    if opcion not in tipos:
        imprimir_error("Opcion incorrecta.")
        return

    datos_usuario["tipo_cuenta"] = tipos[opcion]
    imprimir_exito(f"Tipo de cuenta actualizado a: {tipos[opcion]}")


# ==========================================================
# REPORTES
# ==========================================================
def mostrar_movimientos():
    limpiar_pantalla()
    imprimir_titulo("HISTORIAL DE MOVIMIENTOS", CIAN)

    if len(movimientos) == 0:
        imprimir_advertencia("Todavia no tienes movimientos.")
        return

    print(color(f"  Total de movimientos: {len(movimientos)}", BLANCO))
    imprimir_linea("-", 60, CIAN)

    for numero, movimiento in enumerate(movimientos, start=1):
        tipo = movimiento["tipo"]
        monto = movimiento["monto"]
        saldo_res = movimiento["saldo_resultante"]
        fecha = movimiento["fecha"]
        detalle = movimiento["detalle"]

        if tipo == "Deposito" or tipo == "Interes":
            color_tipo = VERDE
        elif tipo == "Retiro":
            color_tipo = ROJO
        elif tipo == "Transferencia":
            color_tipo = MAGENTA
        else:
            color_tipo = BLANCO

        print(color(f"  {numero}. [{fecha}] {tipo}", color_tipo + NEGRITA))
        print(color(f"     Monto: S/{monto:.2f} | Saldo: S/{saldo_res:.2f}", BLANCO))
        if detalle:
            print(color(f"     Detalle: {detalle}", BLANCO))
        imprimir_linea("-", 60, CIAN)


def mostrar_resumen_cuenta(nombre, saldo_actual):
    limpiar_pantalla()
    imprimir_titulo("RESUMEN DE CUENTA", AZUL)

    retirado_hoy = calcular_retirado_hoy()
    total_depositado = calcular_total_depositado()
    total_retirado = calcular_total_retirado()
    promedio = calcular_promedio_movimientos()

    print(color(f"  Titular            : {nombre}", BLANCO))
    print(color(f"  Numero de cuenta   : {datos_usuario['numero_cuenta']}", BLANCO))
    print(color(f"  Tipo de cuenta     : {datos_usuario['tipo_cuenta']}", BLANCO))
    print(color(f"  Fecha de apertura  : {datos_usuario['fecha_apertura']}", BLANCO))
    imprimir_linea("-", 60, AZUL)
    print(color(f"  Saldo actual       : S/{saldo_actual:.2f}", VERDE + NEGRITA))
    print(color(f"  Total depositado   : S/{total_depositado:.2f}", VERDE))
    print(color(f"  Total retirado     : S/{total_retirado:.2f}", ROJO))
    print(color(f"  Promedio movim.    : S/{promedio:.2f}", CIAN))
    imprimir_linea("-", 60, AZUL)
    print(color(f"  Limite diario      : S/{LIMITE_RETIRO_DIARIO:.2f}", AMARILLO))
    print(color(f"  Retirado hoy       : S/{retirado_hoy:.2f}", AMARILLO))
    print(color(f"  Disponible hoy     : S/{LIMITE_RETIRO_DIARIO - retirado_hoy:.2f}", AMARILLO))
    imprimir_linea("-", 60, AZUL)
    print(color(f"  Total movimientos  : {len(movimientos)}", BLANCO))

    if len(movimientos) > 0:
        ultimo = movimientos[-1]
        print(color(
            f"  Ultimo movimiento  : {ultimo['tipo']} de S/{ultimo['monto']:.2f}",
            BLANCO
        ))
    else:
        print(color("  Ultimo movimiento  : No hay movimientos registrados.", BLANCO))

    imprimir_linea("=", 60, AZUL)


def consultar_limite_retiro():
    limpiar_pantalla()
    imprimir_titulo("LIMITE DE RETIRO", AMARILLO)

    retirado_hoy = calcular_retirado_hoy()
    disponible = LIMITE_RETIRO_DIARIO - retirado_hoy

    print(color(f"  Limite diario   : S/{LIMITE_RETIRO_DIARIO:.2f}", BLANCO))
    print(color(f"  Retirado hoy    : S/{retirado_hoy:.2f}", BLANCO))
    print(color(f"  Disponible hoy  : S/{disponible:.2f}", VERDE + NEGRITA))
    imprimir_linea("-", 60, AMARILLO)

    if disponible <= 0:
        imprimir_error("Ya alcanzaste el limite diario de retiro.")
    elif disponible < LIMITE_RETIRO_DIARIO * 0.2:
        imprimir_advertencia("Estas cerca del limite diario de retiro.")
    else:
        imprimir_info("Aun tienes disponible suficiente para retirar hoy.")


# ==========================================================
# FLUJO PRINCIPAL
# ==========================================================
def inicializar_cuenta():
    limpiar_pantalla()
    imprimir_titulo("APERTURA DE CUENTA - BANCO PYTHON", AZUL)

    nombre = pedir_nombre()
    datos_usuario["nombre"] = nombre
    datos_usuario["numero_cuenta"] = generar_numero_cuenta()
    datos_usuario["fecha_apertura"] = obtener_fecha_actual()

    animacion_carga("Creando cuenta")

    limpiar_pantalla()
    imprimir_titulo("CUENTA CREADA EXITOSAMENTE", VERDE)
    print(color(f"  Titular       : {nombre}", BLANCO))
    print(color(f"  Cuenta        : {datos_usuario['numero_cuenta']}", BLANCO))
    print(color(f"  Saldo inicial : S/{SALDO_INICIAL:.2f}", VERDE + NEGRITA))
    print(color(f"  Fecha apertura: {datos_usuario['fecha_apertura']}", BLANCO))
    imprimir_linea("=", 60, VERDE)
    pausar()


def main():
    global saldo

    inicializar_cuenta()

    while True:
        mostrar_menu()
        opcion = input(color("Selecciona una opcion: ", CIAN)).strip()

        if opcion == "1":
            mostrar_saldo(datos_usuario["nombre"], saldo)
            pausar()

        elif opcion == "2":
            saldo = depositar(saldo)
            pausar()

        elif opcion == "3":
            saldo = retirar(saldo)
            pausar()

        elif opcion == "4":
            saldo = transferir(saldo)
            pausar()

        elif opcion == "5":
            mostrar_movimientos()
            pausar()

        elif opcion == "6":
            mostrar_resumen_cuenta(datos_usuario["nombre"], saldo)
            pausar()

        elif opcion == "7":
            consultar_limite_retiro()
            pausar()

        elif opcion == "8":
            saldo = simular_interes(saldo)
            pausar()

        elif opcion == "9":
            cambiar_tipo_cuenta()
            pausar()

        elif opcion == "10":
            limpiar_pantalla()
            imprimir_titulo("GRACIAS POR SU PREFERENCIA", AZUL)
            print(color(f"\n  Hasta luego, {datos_usuario['nombre']}", VERDE + NEGRITA))
            print(color(f"  Cuenta: {datos_usuario['numero_cuenta']}", BLANCO))
            imprimir_linea("=", 60, AZUL)
            break

        else:
            imprimir_error("Opcion incorrecta. Selecciona del 1 al 10")
            pausar()


if __name__ == "__main__":
    main()