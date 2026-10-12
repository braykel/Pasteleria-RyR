usuario = input("Ingrese su nommbre: ").title()
dinero = float(input(f"Hola, {usuario} indique el dinero que lleva: "))
DINERO_INICIAL = dinero
total = 0
pedido = []

torta_tres_leches = 80.99
torta_chocolate = 90.85
torta_vainilla = 75.87

inca_cola_3L = 13.58
coca_cola_3L = 12.54
pepsi_3L = 9.99

try:
    with open("registros.txt", "r", encoding="utf-8") as archivo:
        registros = [linea.strip() for linea in archivo.readlines()]
except FileNotFoundError:
    registros = []

def registrar_registros(texto):
    registros.append(texto)
    with open("registros.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")
        
        
print("======= Pastelería R & R=========\n")

while True:
    print(f"1. Torta tres leches - $/{torta_tres_leches}")
    print(f"2. Torta chocolate - $/{torta_chocolate}")
    print(f"3. Torta vainilla - $/{torta_vainilla}")
    
    opciones = int(input(f"hola {usuario} ingresa la opcion 1 a 3: \n"))
    
    match opciones:
        case 1:
            print(f"Ha elegido la torta tres leches.\n Total a pagar $/ {torta_tres_leches}")
            dinero -= torta_tres_leches
            total += torta_tres_leches
            pedido.append(f"Torta tres leches - $/ {torta_tres_leches}")
            registrar_registros(f"{usuario} compró Torta tres leches - Total: $/{total} - Vuelto: $/{round(dinero,2)}")
            break
        case 2:
            print(f"Ha elegido la torta chocolate.\n Total a pagar $/ {torta_chocolate}")
            dinero -= torta_chocolate
            total += torta_chocolate
            pedido.append(f"Torta chocolate - $/ {torta_chocolate}")
            registrar_registros(f"{usuario} compró Torta Chocolate - Total: $/{total} - Vuelto: $/{round(dinero,2)}")
            break
        case 3:
            print(f"Ha elegido la torta vainilla.\n Total a pagar $/ {torta_vainilla}")
            dinero -= torta_vainilla
            total += torta_vainilla
            pedido.append(f"Torta vainilla - $/ {torta_vainilla}")
            registrar_registros(f"{usuario} compró Torta Vainilla - Total: $/{total} - Vuelto: $/{round(dinero,2)}")
            break
        case _:
            print(f"Opcion incorrecta , Seleciona una opción del 1 al 3")

while True:
    print("===BEBIDAD EXTRAS====")
    print(f"1. Inca Cola")
    print(f"2. Coca Cola")
    print(f"3. Pepsi")
    print(f"4. No añadir nada extra y pagarr.")
    
    opciones = int(input(f"{usuario} Si deseas algo de bebida extra: \n"))

    match opciones:
        case 1:
            print(f"Ha elegido Inca Cola.\n Total a pagar $/ {inca_cola_3L}")
            dinero -= inca_cola_3L
            total += inca_cola_3L
            print(f"Total a pagar: $/{total}")
            print(f"le quedan $/{round(dinero,2)}")
            pedido.append(f"Inca Cola - $/ {inca_cola_3L}")
            registrar_registros(f"{usuario} añadió Inca Cola - Total: $/{total} - Vuelto: $/{round(dinero,2)}")

        case 2:
            print(f"Ha elegido Coca Cola.\n Total a pagar $/ {coca_cola_3L}")
            dinero -= coca_cola_3L
            total += coca_cola_3L
            print(f"Total a pagar: $/{total}")
            print(f"le quedan $/{round(dinero,2)}")
            pedido.append(f"Coca Cola - $/ {coca_cola_3L}")
            registrar_registros(f"{usuario} añadió Coca Cola - Total: $/{total} - Vuelto: $/{round(dinero,2)}")
        case 3:
            print(f"Ha elegido Pepsi.\n Total a pagar $/ {pepsi_3L}")
            dinero -= pepsi_3L
            total += pepsi_3L
            print(f"Total a pagar: $/{total}")
            print(f"le quedan $/{round(dinero,2)}")
            pedido.append(f"Pepsi - $/ {pepsi_3L}")
            registrar_registros(f"{usuario} añadió Pepsi - Total: $/{total} - Vuelto: $/{round(dinero,2)}")
        case 4:
            print("De acuerdo. no se añade nada extra.")
            break
        case _:
            print(f"Opcion incorrecta, selecionar una opcion del 1 al 4.")
            
if total <= DINERO_INICIAL:
    print("\n=== SU PEDIDO  =====")
    
    for x in pedido:
        
        print(f"-> {x} <-")
        
    print(f" El total de su pedido es $/{total}")
    print(f"Su vuelto: $/{round(dinero,2)}") 
    print("\n ¡BUEN PROVECHO!")
    
    resumen = f"{usuario} compró: {', '.join(pedido)} | Total: $/{total} | Vuelto: $/{round(dinero,2)}"
    registrar_registros(resumen)
else:
    print(f"{usuario} No le llega el dinero para todo su pedido, por favor vuelve a empezar.")