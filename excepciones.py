# =========================================================================
# 1. ERROR DE VALOR (ValueError)
# =========================================================================
try:
    # Intentamos convertir texto puro en un número entero
    numero = int("tres")
except ValueError:
    print(" ValueError: No puedes convertir texto con letras a un número.")

# =========================================================================
# 2. ERROR DE TIPO (TypeError)
# =========================================================================
try:
    # Intentamos sumar un número entero con un texto
    resultado = 5 + "10"
except TypeError:
    print(" TypeError: No puedes sumar números y texto directamente.")

# =========================================================================
# 3. ERROR DE DIVISIÓN POR CERO (ZeroDivisionError)
# =========================================================================
try:
    # Intentamos dividir entre cero
    calculo = 100 / 0
except ZeroDivisionError:
    print(" ZeroDivisionError: Matemáticamente no se puede dividir entre cero.")

# =========================================================================
# 4. ERROR DE ÍNDICE EN LISTAS (IndexError)
# =========================================================================
try:
    lista = ["manzana", "pera"]
    # Intentamos pedir el tercer elemento (índice 2), pero solo hay índices 0 y 1
    elemento = lista[2]
except IndexError:
    print(" IndexError: Estás buscando una posición que no existe en la lista.")

# =========================================================================
# 5. ERROR DE CLAVE EN DICCIONARIOS (KeyError)
# =========================================================================
try:
    usuario = {"nombre": "Lucas"}
    # Intentamos buscar una clave que no definimos
    edad = usuario["edad"]
except KeyError:
    print(" KeyError: Esa clave o dato no existe en el diccionario.")

# =========================================================================
# 6. ERROR DE NOMBRE (NameError)
# =========================================================================
try:
    # Intentamos usar una variable que jamás hemos creado
    print(mi_variable_secreta)
except NameError:
    print(" NameError: Estás llamando a una variable que no ha sido declarada.")

# =========================================================================
# 7. ERROR DE ATRIBUTO (AttributeError)
# =========================================================================
try:
    texto = "Hola"
    # Intentamos usar '.append()', pero eso solo existe en listas, no en textos
    texto.append(" Mundo")
except AttributeError:
    print(" AttributeError: Ese tipo de dato no tiene el método que intentas usar.")

# =========================================================================
# 8. ERROR DE ARCHIVO NO ENCONTRADO (FileNotFoundError)
# =========================================================================
try:
    # Intentamos abrir un archivo que no existe en el sistema
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print(" FileNotFoundError: El archivo que intentas abrir no existe.")

# =========================================================================
# 9. ERROR DE IMPORTACIÓN (ImportError / ModuleNotFoundError)
# =========================================================================
try:
    # Intentamos importar un módulo que no está instalado
    import modulo_inexistente
except ImportError:
    print(" ImportError: El módulo que intentas importar no existe o no está instalado.")

# =========================================================================
# 10. ERROR DE INDENTACIÓN (IndentationError)
# =========================================================================
try:
    # Simulamos una mala indentación usando exec con código mal formateado
    exec("if True:\nprint('Hola')")
except IndentationError:
    print(" IndentationError: La indentación del código es incorrecta.")

# =========================================================================
# 11. ERROR DE SINTAXIS (SyntaxError)
# =========================================================================
try:
    # Simulamos un error de sintaxis usando exec con código inválido
    exec("if True print('Hola')")
except SyntaxError:
    print(" SyntaxError: La sintaxis del código es incorrecta.")

# =========================================================================
# 12. ERROR DE DESBORDAMIENTO (OverflowError)
# =========================================================================
try:
    # Intentamos calcular un número demasiado grande para ser representado
    import math
    resultado = math.exp(1000)
except OverflowError:
    print(" OverflowError: El número resultante es demasiado grande para representarlo.")

# =========================================================================
# 13. ERROR DE RECURSIÓN INFINITA (RecursionError)
# =========================================================================
try:
    # Definimos una función que se llama a sí misma sin fin
    def recursion_infinita():
        return recursion_infinita()
    recursion_infinita()
except RecursionError:
    print(" RecursionError: La función se llamó a sí misma demasiadas veces.")

# =========================================================================
# 14. ERROR DE MEMORIA (MemoryError)
# =========================================================================
try:
    # Intentamos crear una lista gigantesca que supera la memoria disponible
    lista_gigante = [0] * (10**12)
except MemoryError:
    print(" MemoryError: No hay suficiente memoria para completar la operación.")

# =========================================================================
# 15. ERROR DE CONVERSIÓN DE TIPO (TypeError en iteración)
# =========================================================================
try:
    # Intentamos iterar sobre un número entero, lo cual no es iterable
    for i in 5:
        pass
except TypeError:
    print(" TypeError: No puedes iterar sobre un número entero.")

# =========================================================================
# 16. ERROR DE OPERACIÓN NO SOPORTADA (NotImplementedError)
# =========================================================================
try:
    # Simulamos un método abstracto que no ha sido implementado
    raise NotImplementedError("Este método aún no está implementado")
except NotImplementedError:
    print(" NotImplementedError: El método aún no ha sido implementado.")

# =========================================================================
# 17. ERROR DE ASSERT (AssertionError)
# =========================================================================
try:
    # Verificamos una condición que es falsa
    assert 2 + 2 == 5, "Las matemáticas están mal"
except AssertionError:
    print(" AssertionError: La condición evaluada resultó ser falsa.")

# =========================================================================
# 18. ERROR DE TECLADO INTERRUMPIDO (KeyboardInterrupt)
# =========================================================================
# NOTA: Este error ocurre cuando el usuario presiona Ctrl+C.
# No se puede simular fácilmente sin intervención del usuario, pero así se captura:
try:
    # Aquí iría un bucle infinito que el usuario podría interrumpir
    pass
except KeyboardInterrupt:
    print(" KeyboardInterrupt: El usuario interrumpió la ejecución del programa.")

# =========================================================================
# 19. ERROR DE TIEMPO DE ESPERA (TimeoutError)
# =========================================================================
try:
    # Simulamos una operación que tarda demasiado tiempo
    import socket
    socket.setdefaulttimeout(0.001)
    socket.create_connection(("10.255.255.1", 80))
except TimeoutError:
    print(" TimeoutError: La operación tardó demasiado tiempo en completarse.")

# =========================================================================
# 20. ERROR DE CONEXIÓN (ConnectionError)
# =========================================================================
try:
    # Intentamos conectarnos a un servidor que no existe
    import socket
    socket.create_connection(("servidor_inexistente_12345.com", 80))
except ConnectionError:
    print(" ConnectionError: No se pudo establecer la conexión con el servidor.")

# =========================================================================
# 21. ERROR DE UNICODE (UnicodeDecodeError)
# =========================================================================
try:
    # Intentamos decodificar bytes que no son válidos en UTF-8
    bytes_invalidos = b"\xff\xfe\x00"
    texto = bytes_invalidos.decode("utf-8")
except UnicodeDecodeError:
    print(" UnicodeDecodeError: No se pudo decodificar el texto con esa codificación.")

# =========================================================================
# 22. ERROR DE LLAVE DUPLICADA (KeyError en diccionario al eliminar)
# =========================================================================
try:
    # Intentamos eliminar una clave que no existe en el diccionario
    diccionario = {"a": 1, "b": 2}
    del diccionario["c"]
except KeyError:
    print(" KeyError: La clave que intentas eliminar no existe en el diccionario.")

# =========================================================================
# 23. ERROR DE ATRIBUTO EN MÓDULO (AttributeError en módulo)
# =========================================================================
try:
    # Intentamos acceder a un atributo que no existe en un módulo
    import math
    math.funcion_inexistente()
except AttributeError:
    print(" AttributeError: El módulo no tiene ese atributo o función.")

# =========================================================================
# 24. ERROR DE TIPO EN LLAMADA (TypeError por argumentos incorrectos)
# =========================================================================
try:
    # Intentamos llamar a una función con un número incorrecto de argumentos
    def saludar(nombre):
        return f"Hola, {nombre}"
    saludar("Lucas", "Extra")
except TypeError:
    print(" TypeError: La función recibió un número incorrecto de argumentos.")

# =========================================================================
# 25. ERROR DE VALOR EN DESEMPAQUETADO (ValueError en unpacking)
# =========================================================================
try:
    # Intentamos desempaquetar una tupla con menos elementos de los esperados
    a, b, c = (1, 2)
except ValueError:
    print(" ValueError: No hay suficientes valores para desempaquetar.")

# =========================================================================
# 26. ERROR DE ÍNDICE EN STRING (IndexError en cadena)
# =========================================================================
try:
    # Intentamos acceder a un índice que no existe en una cadena
    texto = "Hola"
    letra = texto[10]
except IndexError:
    print(" IndexError: El índice está fuera del rango de la cadena.")

# =========================================================================
# 27. ERROR DE DIVISIÓN ENTERA POR CERO (ZeroDivisionError en //)
# =========================================================================
try:
    # Intentamos una división entera entre cero
    resultado = 100 // 0
except ZeroDivisionError:
    print(" ZeroDivisionError: No se puede hacer división entera entre cero.")

# =========================================================================
# 28. ERROR DE MÓDULO POR CERO (ZeroDivisionError en %)
# =========================================================================
try:
    # Intentamos calcular el módulo entre cero
    resultado = 100 % 0
except ZeroDivisionError:
    print(" ZeroDivisionError: No se puede calcular el módulo entre cero.")

# =========================================================================
# 29. ERROR DE CONVERSIÓN A ENTERO (ValueError en int)
# =========================================================================
try:
    # Intentamos convertir un texto decimal a entero
    numero = int("3.14")
except ValueError:
    print(" ValueError: No puedes convertir un texto decimal a entero directamente.")

# =========================================================================
# 30. ERROR DE CONVERSIÓN A FLOTANTE (ValueError en float)
# =========================================================================
try:
    # Intentamos convertir un texto no numérico a flotante
    numero = float("abc")
except ValueError:
    print(" ValueError: No puedes convertir un texto no numérico a flotante.")