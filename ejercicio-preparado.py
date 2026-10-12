# TUPLA: información fija del banco
banco = ("Banco Perú", "PEN", "Perú")

# DICCIONARIO: información del cliente
cliente = {
    "nombre": "Carlos",
    "saldo": 1500.00,
    "activo": True
}

# CONJUNTO: productos únicos del cliente
productos = {"Cuenta de Ahorros", "Tarjeta de Débito", "Yape", "Plin"}

# LISTA: historial de movimientos
# Se carga automáticamente desde el archivo si existe
try:
    with open("movimientos.txt", "r", encoding="utf-8") as archivo:
        movimientos = [linea.strip() for linea in archivo.readlines()]
except FileNotFoundError:
    movimientos = []

# Función para registrar movimiento en lista y archivo
def registrar_movimiento(texto):
    movimientos.append(texto)
    with open("movimientos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")

while True:
    print("\n===== SISTEMA BANCARIO =====")
    print(f"Banco: {banco[0]}")
    print(f"Cliente: {cliente['nombre']}")

    print("\n1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Ver productos")
    print("5. Agregar producto")
    print("6. Ver historial de movimientos")
    print("7. Salir")

    opcion = input("\nSeleccione una opción: ").strip()

    # CONSULTAR SALDO
    if opcion == "1":
        print(f"\nSaldo disponible: S/ {cliente['saldo']:.2f}")

    # DEPOSITAR
    elif opcion == "2":
        while True:
            try:
                deposito = float(input("Ingrese monto a depositar: S/ "))
                if deposito <= 0:
                    print("El monto debe ser mayor a 0.")
                    continue
                cliente["saldo"] += deposito
                registrar_movimiento(f"Depósito: S/ {deposito:.2f}")
                print("Depósito realizado correctamente.")
                print(f"Nuevo saldo: S/ {cliente['saldo']:.2f}")
                break
            except ValueError:
                print("Ingrese solamente números.")

    # RETIRAR
    elif opcion == "3":
        while True:
            try:
                retiro = float(input("Ingrese monto a retirar: S/ "))
                if retiro <= 0:
                    print("El monto debe ser mayor a 0.")
                    continue
                if retiro > cliente["saldo"]:
                    print("Saldo insuficiente.")
                    continue
                cliente["saldo"] -= retiro
                registrar_movimiento(f"Retiro: S/ {retiro:.2f}")
                print("Retiro realizado correctamente.")
                print(f"Nuevo saldo: S/ {cliente['saldo']:.2f}")
                break
            except ValueError:
                print("Ingrese solamente números.")

    # VER PRODUCTOS
    elif opcion == "4":
        print("\n=== PRODUCTOS CONTRATADOS ===")
        for producto in productos:
            print(f"- {producto}")

    # AGREGAR PRODUCTO
    elif opcion == "5":
        producto = input("Ingrese el producto que desea contratar: ").strip().title()
        if producto == "":
            print("El nombre del producto no puede estar vacío.")
        elif producto in productos:
            print("El cliente ya tiene este producto.")
        else:
            productos.add(producto)
            registrar_movimiento(f"Producto agregado: {producto}")
            print(f"{producto} agregado correctamente.")

    # VER HISTORIAL DE MOVIMIENTOS
    elif opcion == "6":
        print("\n=== HISTORIAL DE MOVIMIENTOS ===")
        if not movimientos:
            print("No hay movimientos registrados.")
        else:
            for i, mov in enumerate(movimientos, start=1):
                print(f"{i}. {mov}")

    # SALIR
    elif opcion == "7":
        print("\nGracias por utilizar el sistema.")
        break

    # OPCIÓN INVÁLIDA
    else:
        print("Opción incorrecta. Seleccione del 1 al 7.")
