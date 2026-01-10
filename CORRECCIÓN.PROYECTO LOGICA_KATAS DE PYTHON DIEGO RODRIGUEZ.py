#1. Función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra
def contar_frecuencia_letras(cadena):
    # Convertir a minúsculas
    cadena_procesada = cadena.lower()
    
    # Diccionario para almacenar las frecuencias
    frecuencias = {}
    
    # Iterar sobre cada carácter en la cadena
    for letra in cadena_procesada:
        # Ignorar espacios
        if letra != ' ':
            # Contar la letra en el diccionario
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    
    # Ordenar el diccionario alfabéticamente
    frecuencias = dict(sorted(frecuencias.items()))
    
    return frecuencias

if __name__ == "__main__":
    # Prueba 1
    resultado1 = contar_frecuencia_letras("Me llamo Diego Rodriguez")
    print(f"Entrada: 'Me llamo Diego Rodriguez'")
    print(f"Resultado: {resultado1}\n")

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# Función que duplica un número
def duplicar(numero):
    """Duplica un número recibido como parámetro."""
    return numero * 2


# Lista original de números
numeros = [2, 7, 25, 48, 51, 67, 89, 102]

# Usar map() para aplicar la función duplicar a cada elemento
numeros_duplicados = list(map(duplicar, numeros))

# Mostrar resultados
print(f"Lista duplicada: {numeros_duplicados}")

#3. Función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    """
    Filtra palabras que contengan una palabra objetivo.
    
    Args:
        lista_palabras (list): Lista de palabras a buscar.
        palabra_objetivo (str): Palabra que debe estar contenida.
    
    Returns:
        list: Lista de palabras que contienen la palabra objetivo.
    """
    palabras_filtradas = []
    
    # Iterar sobre cada palabra en la lista
    for palabra in lista_palabras:
        # Convertir a minúsculas para comparación sin importar mayúsculas
        if palabra_objetivo.lower() in palabra.lower():
            palabras_filtradas.append(palabra)
    
    return palabras_filtradas

if __name__ == "__main__":
    # Lista de palabras
    palabras = ["Tomate", "Lechuga", "Cebolla", "Legumbre", "Coliflor", "Leche"]
    
    objetivo1 = "le"
    resultado1 = filtrar_palabras(palabras, objetivo1)
    print(f"Palabras que contienen '{objetivo1}': {resultado1}\n")
    

#4. Función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencia(lista1, lista2):
    """
    Calcula la diferencia entre elementos de dos listas.
    
    Args:
        lista1 (list): Primera lista de números.
        lista2 (list): Segunda lista de números.
    
    Returns:
        list: Lista con las diferencias (lista1 - lista2).
    """
    # Función que calcula la diferencia entre dos números
    def diferencia(num1, num2):
        return num1 - num2
    
    # Usar map() con zip() para emparejar elementos de ambas listas
    diferencias = list(map(diferencia, lista1, lista2))
    
    return diferencias

if __name__ == "__main__":
    # Listas de números
    lista1 = [10, 20, 30, 40, 50]
    lista2 = [2, 5, 8, 10, 15]
    
    # Calcular diferencias
    resultado = calcular_diferencia(lista1, lista2)
    
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Diferencias: {resultado}\n")
    

#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def calcular_media_estado(numeros, nota_aprobado=5):
    """
    Calcula la media de una lista de números y determina si aprueba o suspende.
    
    Args:
        numeros (list): Lista de números (notas).
        nota_aprobado (int/float): Nota mínima para aprobar. Por defecto es 5.
    
    Returns:
        tuple: Tupla con (media, estado). Ejemplo: (7.5, "aprobado")
    """
    # Calcular la media
    media = sum(numeros) / len(numeros)
    
    # Determinar el estado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    # Devolver una tupla con la media y el estado
    return (media, estado)


# Pruebas de la función
if __name__ == "__main__":
    # Prueba 1: Con nota_aprobado por defecto (5)
    notas1 = [8, 4, 6, 8, 9, 4, 5, 5, 7, 10, 7]
    resultado1 = calcular_media_estado(notas1)
    media1, estado1 = resultado1
    print(f"Notas: {notas1}")
    print(f"Media: {media1}")
    print(f"Estado: {estado1}\n")
    
#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
    """
    Calcula el factorial de un número de manera recursiva.
    
    Args:
        numero (int): Número para calcular el factorial.
    
    Returns:
        int: El factorial del número.
     """
    # Caso base: si el número es 0 o 1, devolver 1
    if numero == 0 or numero == 1:
        return 1
    
    # Caso recursivo: multiplicar el número por el factorial del número anterior
    else:
        return numero * factorial(numero - 1)

if __name__ == "__main__":
    numero = 8
    resultado = factorial(numero)
    print(f"Factorial de {numero} = {resultado}")

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def convertir_tuplas_a_strings(lista_tuplas):
    """
    Convierte una lista de tuplas a una lista de strings.
    
    Args:
        lista_tuplas (list): Lista que contiene tuplas.
    
    Returns:
        list: Lista de strings representando las tuplas.
    """
    # Función que convierte una tupla a string
    def tupla_a_string(tupla):
        return str(tupla)
    
    # Usar map() para aplicar la función a cada tupla
    strings = list(map(tupla_a_string, lista_tuplas))
    
    return strings

if __name__ == "__main__":
    lista_tuplas = [(1, 2), (3, 4), (5, 6), (7, 8)]
    resultado = convertir_tuplas_a_strings(lista_tuplas)
    
    print(f"Lista de tuplas: {lista_tuplas}")
    print(f"Lista de strings: {resultado}")

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    """
    Solicita dos números al usuario y realiza la división.
    Maneja excepciones de valores no numéricos y división por cero.
    """
    try:
        # Solicitar números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Intentar realizar la división
        resultado = num1 / num2
        
        # Si todo fue exitoso
        print(f"\n División exitosa: {num1} / {num2} = {resultado}")
        
    except ValueError:
        # Error cuando el usuario ingresa algo que no es número
        print("\n Error: Solo ingresar valores numéricos.")
        
    except ZeroDivisionError:
        # Error cuando el usuario intenta dividir por cero
        print("\n Error: No se puede dividir por cero.")

if __name__ == "__main__":
    dividir_numeros()

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

def filtrar_mascotas_permitidas(lista_mascotas):
    """
    Filtra mascotas, excluyendo las prohibidas en España.
    
    Args:
        lista_mascotas (list): Lista de nombres de mascotas.
    
    Returns:
        list: Lista de mascotas permitidas.
    """
    # Lista de mascotas prohibidas en España
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    # Función que verifica si una mascota está permitida
    def es_permitida(mascota):
        return mascota not in mascotas_prohibidas
    
    # Usar filter() para obtener solo las mascotas permitidas
    mascotas_permitidas = list(filter(es_permitida, lista_mascotas))
    
    return mascotas_permitidas

if __name__ == "__main__":
    mascotas = ["Perro", "Gato", "Mapache", "Periquito", "Tigre", "Conejo", "Cocodrilo", "Hamster"]
    resultado = filtrar_mascotas_permitidas(mascotas)
    
    print(f"Mascotas permitidas: {resultado}")

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# Crear una excepción personalizada
class ListaVaciaError(Exception):
    """Excepción que se lanza cuando la lista está vacía."""
    pass


def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números.
    
    Returns:
        float: El promedio de los números.
    
    Raises:
        ListaVaciaError: Si la lista está vacía.
    """
    # Verificar si la lista está vacía
    if len(numeros) == 0:
        raise ListaVaciaError("La lista de números está vacía. No se puede calcular el promedio.")
    
    # Calcular el promedio
    promedio = sum(numeros) / len(numeros)
    return promedio

if __name__ == "__main__":
    try:
        numeros1 = [8, 29, 83, 99, 109, 234]
        resultado1 = calcular_promedio(numeros1)
        print(f"Lista: {numeros1}")
        print(f"Promedio: {resultado1}\n")
        
    except ListaVaciaError as e:
        print(f"Error, lista vacia: {e}\n")

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado, maneja las excepciones adecuadamente.

# Crear excepción personalizada para edad fuera de rango
class EdadFueraDeRangoError(Exception):
    """Excepción que se lanza cuando la edad está fuera del rango válido."""
    pass


def solicitar_edad():
    """
    Solicita la edad al usuario y valida que sea un valor correcto.
    """
    try:
        # Solicitar la edad al usuario
        edad = int(input("Introduce tu edad: "))
        
        # Verificar que la edad esté en el rango válido
        if edad < 16 or edad > 100:
            raise EdadFueraDeRangoError(f"La edad {edad} está fuera del rango válido (16-100).")
        
        # Si todo es correcto
        print(f"\n Edad válida: {edad} años")
        
    except ValueError:
        # Error cuando el usuario ingresa algo que no es un número
        print("\n Error: Solo ingresar un valor numérico.")
        
    except EdadFueraDeRangoError as e:
        # Error cuando la edad está fuera de rango
        print(f"\n Error, edad fuera del rango de edad (16-100) : {e}")

if __name__ == "__main__":
    solicitar_edad()

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def obtener_longitud_palabras(frase):
    """
    Recibe una frase y devuelve una lista con la longitud de cada palabra.
    
    Args:
        frase (str): La frase a procesar.
    
    Returns:
        list: Lista con la longitud de cada palabra.
    """
    # Función que obtiene la longitud de una palabra
    def longitud(palabra):
        return len(palabra)
    
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Usar map() para obtener la longitud de cada palabra
    longitudes = list(map(longitud, palabras))
    
    return longitudes

if __name__ == "__main__":
    frase = "Hoy me voy de viaje a Amsterdam"
    resultado = obtener_longitud_palabras(frase)
    
    print(f"Frase: {frase}")
    print(f"Longitudes: {resultado}")

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.

def convertir_mayus_minus(caracteres):
    """
    Recibe un conjunto de caracteres y devuelve una lista de tuplas
    con cada letra en mayúsculas y minúsculas, sin repetir.
    
    Args:
        caracteres (str): Conjunto de caracteres.
    
    Returns:
        list: Lista de tuplas (mayúscula, minúscula).
    """
    # Convertir a minúsculas y eliminar repetidos usando set
    caracteres_unicos = set(caracteres.lower())
    
    # Filtrar solo letras (no números ni caracteres especiales)
    letras = [char for char in caracteres_unicos if char.isalpha()]
    
    # Función que crea una tupla con mayúscula y minúscula
    def crear_tupla(letra):
        return (letra.upper(), letra.lower())
    
    # Usar map() para aplicar la función a cada letra
    tuplas = list(map(crear_tupla, letras))
    
    return tuplas

if __name__ == "__main__":
    caracteres = "Elcieloesazul23"
    resultado = convertir_mayus_minus(caracteres)
    
    print(f"Resultado: {resultado}")

#14. Crea una función que retorne las palabras de una lista de palabras que comiencen con una letra en especifico. Usa la función filter()

def filtrar_por_letra_inicial(lista_palabras, letra_inicial):
    """
    Filtra palabras que comienzan con una letra específica.
    
    Args:
        lista_palabras (list): Lista de palabras.
        letra_inicial (str): La letra con la que deben empezar las palabras.
    
    Returns:
        list: Lista de palabras que comienzan con la letra especificada.
    """
    # Función que verifica si una palabra comienza con la letra
    def comienza_con_letra(palabra):
        return palabra.lower().startswith(letra_inicial.lower())
    
    # Usar filter() para obtener las palabras que cumplen la condición
    palabras_filtradas = list(filter(comienza_con_letra, lista_palabras))
    
    return palabras_filtradas

if __name__ == "__main__":
    palabras = ["Azul", "Verde", "Amarillo", "Rojo", "Anaranjado", "Fucsia", "Gris"]
    letra = "a"
    resultado = filtrar_por_letra_inicial(palabras, letra)
    
    print(f"Palabras que empiezan con '{letra}': {resultado}")

#15. Crea una función lambda que sume 3 a cada número de una lista dada

def sumar_tres(numeros):
    """
    Suma 3 a cada número de una lista usando lambda.
    
    Args:
        numeros (list): Lista de números.
    
    Returns:
        list: Lista con cada número sumado 3.
    """
    # Usar lambda para sumar 3 a cada número
    resultado = list(map(lambda x: x + 3, numeros))
    
    return resultado

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = sumar_tres(numeros)
    print(f"Lista con +3: {resultado}")


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def filtrar_palabras_por_longitud(texto, n):
    """
    Filtra palabras que tengan más de n caracteres.
    
    Args:
        texto (str): Cadena de texto con palabras.
        n (int): Longitud mínima de las palabras a devolver.
    
    Returns:
        list: Lista de palabras más largas que n.
    """
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Función que verifica si una palabra es más larga que n
    def es_mas_larga(palabra):
        return len(palabra) > n
    
    # Usar filter() para obtener las palabras que cumplen la condición
    palabras_filtradas = list(filter(es_mas_larga, palabras))
    
    return palabras_filtradas

if __name__ == "__main__":
    texto = "Mañana tengo una reunión en el trabajo muy importante"
    n = 5
    resultado = filtrar_palabras_por_longitud(texto, n)
    
    print(f"Texto: {texto}")
    print(f"Palabras más largas que {n}: {resultado}")


#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Usa la función reduce()

from functools import reduce

def lista_digitos_a_numero(digitos):
    """
    Convierte una lista de dígitos a un número.
    
    Args:
        digitos (list): Lista de dígitos (0-9).
    
    Returns:
        int: El número formado por los dígitos.
    
    """
    # Función que acumula los dígitos en un número
    def acumular_digitos(acumulador, digito):
        return acumulador * 10 + digito
    
    # Usar reduce() para convertir la lista de dígitos en un número
    numero = reduce(acumular_digitos, digitos, 0)
    
    return numero

if __name__ == "__main__":
    digitos = [8, 3, 6]
    resultado = lista_digitos_a_numero(digitos)
    
    print(f"Lista de dígitos: {digitos}")
    print(f"Número correspondiente: {resultado}")

#18. Escribe un programa que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def filtrar_estudiantes_excelentes(estudiantes):
    """
    Filtra estudiantes con calificación mayor o igual a 90.
    
    Args:
        estudiantes (list): Lista de diccionarios con información de estudiantes.
    
    Returns:
        list: Lista de estudiantes con calificación >= 90.
    """
    # Función que verifica si la calificación es >= 90
    def tiene_excelente_calificacion(estudiante):
        return estudiante["calificacion"] >= 90
    
    # Usar filter() para obtener los estudiantes excelentes
    estudiantes_excelentes = list(filter(tiene_excelente_calificacion, estudiantes))
    
    return estudiantes_excelentes


# Prueba del programa
if __name__ == "__main__":
    # Lista de diccionarios con información de estudiantes
    estudiantes = [
        {"nombre": "Diego", "edad": 20, "calificacion": 95},
        {"nombre": "Ana", "edad": 19, "calificacion": 85},
        {"nombre": "Carlos", "edad": 21, "calificacion": 62},
        {"nombre": "María", "edad": 20, "calificacion": 98},
        {"nombre": "Pedro", "edad": 22, "calificacion": 90},
        {"nombre": "Laura", "edad": 18, "calificacion": 88},
        {"nombre": "Lucia", "edad": 19, "calificacion": 91},
        {"nombre": "Marta", "edad": 23, "calificacion": 88}
    ]
    
    # Filtrar estudiantes con calificación >= 90
    resultado = filtrar_estudiantes_excelentes(estudiantes)
    
    print(f"\nEstudiantes con calificación >= 90:")
    for estudiante in resultado:
        print(f"  {estudiante['nombre']}: {estudiante['calificacion']}")


#19. Crea una función lambda que filtre los números impares de una lista dada.

def filtrar_impares(numeros):
    """
    Filtra los números impares de una lista usando lambda y filter().
    
    Args:
        numeros (list): Lista de números.
    
    Returns:
        list: Lista con solo los números impares.
    """
    # Usar filter() con lambda para obtener los números impares
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    
    return impares


if __name__ == "__main__":
    numeros = [13, 22, 36, 49, 57, 16, 73, 58, 29, 106, 38, 41]
    resultado = filtrar_impares(numeros)
    print(f"Números impares: {resultado}")


#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_integers(lista_mixta):
    """
    Filtra solo los elementos de tipo integer de una lista.
    
    Args:
        lista_mixta (list): Lista con elementos de diferentes tipos.
    
    Returns:
        list: Lista con solo los elementos de tipo integer.
    """
    # Función que verifica si un elemento es de tipo integer
    def es_integer(elemento):
        return isinstance(elemento, int) and not isinstance(elemento, bool)
    
    # Usar filter() para obtener solo los integers
    solo_integers = list(filter(es_integer, lista_mixta))
    
    return solo_integers

if __name__ == "__main__":
    lista_mixta = [1, "martes", 8, "jueves", 3, "rojo","ciudad", 4, 50, "mañana"]
    resultado = filtrar_integers(lista_mixta)
    
    print(f"Solo integers: {resultado}")

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo(numero):
    """
    Calcula el cubo de un número usando una función lambda.
    
    Args:
        numero (int/float): El número al que calcular el cubo.
    
    Returns:
        int/float: El cubo del número.
    """
    # Crear una función lambda que calcula el cubo
    cubo = lambda x: x ** 3
    
    # Aplicar la lambda al número
    resultado = cubo(numero)
    
    return resultado

if __name__ == "__main__":
    numero = 386
    resultado = calcular_cubo(numero)
    
    print(f"Número: {numero}")
    print(f"Cubo: {resultado}")

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()

from functools import reduce

def calcular_producto_total(numeros):
    """
    Calcula el producto total de todos los números en una lista.
    
    Args:
        numeros (list): Lista de números.
    
    Returns:
        int/float: El producto de todos los números.
    """
    # Función que multiplica dos números
    def multiplicar(a, b):
        return a * b
    
    # Usar reduce() para multiplicar todos los números
    producto = reduce(multiplicar, numeros)
    
    return producto

if __name__ == "__main__":
    numeros = [8, 34, 26, 5]
    resultado = calcular_producto_total(numeros)
    
    print(f"Lista: {numeros}")
    print(f"Producto total: {resultado}")

#23. Concatena una lista de palabras. Usa la función reduce()

def concatenar_palabras(palabras):
    """
    Concatena todas las palabras de una lista en una sola cadena.
    
    Args:
        palabras (list): Lista de palabras.
    
    Returns:
        str: Las palabras concatenadas.

    """
    # Función que concatena dos palabras
    def unir_palabras(palabra1, palabra2):
        return palabra1 + palabra2
    
    # Usar reduce() para concatenar todas las palabras
    resultado = reduce(unir_palabras, palabras)
    
    return resultado

if __name__ == "__main__":
    palabras = ["Hola", "que", "tal", "estas"]
    resultado = concatenar_palabras(palabras)
    
    print(f"Lista: {palabras}")
    print(f"Concatenadas: {resultado}")

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()
def calcular_diferencia_total(numeros):
    """
    Calcula la diferencia total restando todos los números secuencialmente.
    
    Args:
        numeros (list): Lista de números.
    
    Returns:
        int/float: La diferencia total.
    """
    # Función que resta dos números
    def restar(a, b):
        return a - b
    
    # Usar reduce() para restar todos los números
    diferencia = reduce(restar, numeros)
    
    return diferencia

if __name__ == "__main__":
    numeros = [100, 20, 15, 10]
    resultado = calcular_diferencia_total(numeros)
    
    print(f"Lista: {numeros}")
    print(f"Diferencia total: {resultado}")

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    """
    Cuenta el número total de caracteres en una cadena de texto.
    
    Args:
        texto (str): Cadena de texto.
    
    Returns:
        int: El número total de caracteres.
    """
    # Usar len() para contar caracteres
    cantidad = len(texto)
    
    return cantidad

if __name__ == "__main__":
    texto = "Mi color favorito es el verde"
    resultado = contar_caracteres(texto)
    
    print(f"Texto: '{texto}'")
    print(f"Número de caracteres: {resultado}")

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

def calcular_resto(a, b):
    """
    Calcula el resto de la división entre dos números usando lambda.
    
    Args:
        a (int): Dividendo.
        b (int): Divisor.
    
    Returns:
        int: El resto de la división.

    """
    # Crear una función lambda que calcula el resto
    resto = lambda x, y: x % y
    
    # Aplicar la lambda a los números
    resultado = resto(a, b)
    
    return resultado

if __name__ == "__main__":
    a = 537
    b = 8
    resultado = calcular_resto(a, b)
    
    print(f"División: {a} ÷ {b}")
    print(f"Cociente: {a // b}")
    print(f"Resto: {resultado}")

#27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números.
    
    Returns:
        float: El promedio de los números.
    """
    # Calcular la suma de todos los números
    suma = sum(numeros)
    
    # Calcular la cantidad de números
    cantidad = len(numeros)
    
    # Calcular el promedio
    promedio = suma / cantidad
    
    return promedio

if __name__ == "__main__":
    numeros = [34, 26, 56, 21, 109]
    resultado = calcular_promedio_simple(numeros)
    
    print(f"Lista: {numeros}")
    print(f"Promedio: {resultado}")

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def buscar_primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento duplicado en una lista.
    
    Args:
        lista (list): Lista de elementos.
    
    Returns:
        El primer elemento duplicado o None si no hay duplicados.
    """
    # Conjunto para guardar elementos ya vistos
    vistos = set()
    
    # Recorrer la lista
    for elemento in lista:
        # Si el elemento ya está en vistos, es un duplicado
        if elemento in vistos:
            return elemento
        # Si no, lo añadimos al conjunto
        vistos.add(elemento)
    
    # Si no hay duplicados, devolver None
    return None

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 2, 5, 3]
    resultado = buscar_primer_duplicado(lista)
    
    print(f"Lista: {lista}")
    print(f"Primer duplicado: {resultado}")

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_texto(variable):
    """
    Convierte una variable en texto y enmascara todos los caracteres 
    excepto los últimos cuatro con '#'.
    
    Args:
        variable: Cualquier variable (int, str, float, etc).
    
    Returns:
        str: Texto enmascarado.
    """
    # Convertir la variable a string
    texto = str(variable)
    
    # Obtener la longitud del texto
    longitud = len(texto)
    
    # Si tiene menos de 4 caracteres, devolver como está
    if longitud <= 4:
        return texto
    
    # Enmascarar todos excepto los últimos 4
    caracteres_a_enmascarar = longitud - 4
    texto_enmascarado = "#" * caracteres_a_enmascarar + texto[-4:]
    
    return texto_enmascarado
if __name__ == "__main__":
    # Prueba con diferentes tipos
    print(f"String: {'1234567890'} → {enmascarar_texto('1234567890')}")
    print(f"String: {'ABCDEF'} → {enmascarar_texto('ABCDEF')}")
    print(f"String: {'ABC'} → {enmascarar_texto('ABC')}")
    print(f"Integer: {123456789} → {enmascarar_texto(123456789)}")
    print(f"Float: {3.14159} → {enmascarar_texto(3.14159)}")

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas.
    
    Args:
        palabra1 (str): Primera palabra.
        palabra2 (str): Segunda palabra.
    
    Returns:
        bool: True si son anagramas, False en caso contrario.
    """
    # Convertir a minúsculas y eliminar espacios
    palabra1_limpia = palabra1.lower().replace(" ", "")
    palabra2_limpia = palabra2.lower().replace(" ", "")
    
    # Ordenar las letras de ambas palabras
    palabra1_ordenada = sorted(palabra1_limpia)
    palabra2_ordenada = sorted(palabra2_limpia)
    
    # Comparar las palabras ordenadas
    return palabra1_ordenada == palabra2_ordenada

if __name__ == "__main__":
    # Prueba 1: Anagramas claros
    p1, p2 = "amor", "roma"
    resultado = son_anagramas(p1, p2)
    print(f"¿'{p1}' y '{p2}' son anagramas? {resultado}\n")
    
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

class NombreNoEncontradoError(Exception):
    """Excepción que se lanza cuando el nombre no está en la lista."""
    pass

def buscar_nombre_en_lista():
    """
    Solicita al usuario una lista de nombres y busca un nombre específico.
    Usando 'in' para verificar si está en la lista.
    """
    try:
        # Solicitar lista de nombres
        entrada_nombres = input("Ingresa nombres separados por coma: ")
        lista_nombres = [nombre.strip().lower() for nombre in entrada_nombres.split(",")]
        
        # Solicitar el nombre a buscar
        nombre_buscar = input("Ingresa el nombre a buscar: ").strip().lower()
        
        # Usar 'in' para verificar si el nombre está en la lista
        if nombre_buscar not in lista_nombres:
            raise NombreNoEncontradoError(f"El nombre '{nombre_buscar}' no está en la lista.")
        
        # Si se encontró
        print(f"\n El nombre '{nombre_buscar}' fue encontrado en la lista")
        
    except NombreNoEncontradoError as e:
        print(f"\n Error personalizado: {e}")
        
    except Exception as e:
        print(f"\n Error inesperado: {e}")
    
if __name__ == "__main__":
    buscar_nombre_en_lista()

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto_empleado(nombre_completo, lista_empleados):
    """Busca un empleado por nombre completo y devuelve su puesto."""
    nombre_buscar = nombre_completo.lower().strip()
    
    for empleado in lista_empleados:
        nombre_empleado = empleado["nombre"].lower().strip()
        if nombre_empleado == nombre_buscar:
            return f"{empleado['nombre']} trabaja como {empleado['puesto']}"
    
    return f" {nombre_completo} no trabaja aquí."


# Lista de empleados
empleados = [
    {"nombre": "Juan Pérez", "puesto": "Desarrollador"},
    {"nombre": "María García", "puesto": "Diseñadora"},
    {"nombre": "Carlos López", "puesto": "Gerente de Proyectos"},
    {"nombre": "Ana Martínez", "puesto": "Especialista de RRHH"},
    {"nombre": "Pedro Rodríguez", "puesto": "Administrador de Sistemas"}
]

nombre1 = "Juan Pérez"
resultado1 = buscar_puesto_empleado(nombre1, empleados)
print(f"Resultado: {resultado1}\n")


   #33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def sumar_listas(lista1, lista2):
    """
    Suma elementos correspondientes de dos listas usando lambda y map().
    
    Args:
        lista1 (list)
        lista2 (list)
    
    Returns:
        list: Lista con la suma de elementos correspondientes.
    
    """
    # Crear lambda que suma dos números
    sumar = lambda x, y: x + y
    
    # Usar map() con zip() para emparejar elementos y sumarlos
    resultado = list(map(sumar, lista1, lista2))
    
    return resultado

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [10, 20, 30, 40, 50]
    resultado = sumar_listas(lista1, lista2)
    
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Sumas: {resultado}")
 

#34. Clase Arbol con métodos para manipular la estructura del árbol.

class Arbol:
    """
    Clase que representa un árbol genérico con tronco y ramas.
    """
    
    def __init__(self):
        """
        Inicializa un árbol con un tronco de longitud 1 y lista vacía de ramas.
        """
        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en una unidad.
        """
        self.tronco += 1
    
    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud 1 a la lista de ramas.
        """
        self.ramas.append(1)
    
    def crecer_ramas(self):
        """
        Aumenta en una unidad la longitud de todas las ramas existentes.
        """
        self.ramas = [rama + 1 for rama in self.ramas]
    
    def quitar_rama(self, posicion):
        """
        Elimina una rama en una posición específica.
        
        Args:
            posicion (int): Índice de la rama a eliminar (empezando desde 0).
        """
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"Error: La posición {posicion} no es válida.")
    
    def info_arbol(self):
        """
        Devuelve información sobre el árbol.
        
        Returns:
            dict: Diccionario con información del tronco y ramas.
        """
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

if __name__ == "__main__":
    # 1. Crear un árbol
    mi_arbol = Arbol()
    print("1. Árbol creado")
    print(f"   Info: {mi_arbol.info_arbol()}\n")
    
    # 2. Hacer crecer el tronco del árbol una unidad
    mi_arbol.crecer_tronco()
    print("2. Tronco crecido")
    print(f"   Info: {mi_arbol.info_arbol()}\n")
    
    # 3. Añadir una nueva rama al árbol
    mi_arbol.nueva_rama()
    print("3. Nueva rama añadida")
    print(f"   Info: {mi_arbol.info_arbol()}\n")
    
    # 4. Hacer crecer todas las ramas del árbol una unidad
    mi_arbol.crecer_ramas()
    print("4. Ramas crecidas")
    print(f"   Info: {mi_arbol.info_arbol()}\n")
    
    # 5. Añadir dos nuevas ramas al árbol
    mi_arbol.nueva_rama()
    mi_arbol.nueva_rama()
    print("5. Dos nuevas ramas añadidas")
    print(f"   Info: {mi_arbol.info_arbol()}\n")
    
    # 6. Retirar la rama situada en la posición 2
    mi_arbol.quitar_rama(2)
    print("6. Rama en posición 2 retirada")
    print(f"   Info: {mi_arbol.info_arbol()}\n")
    
    # 7. Obtener información sobre el árbol
    print("7. Información final del árbol:")
    info = mi_arbol.info_arbol()
    print(f"   Longitud del tronco: {info['longitud_tronco']}")
    print(f"   Número de ramas: {info['numero_ramas']}")
    print(f"   Longitudes de las ramas: {info['longitudes_ramas']}")

#35. Clase UsuarioBanco con métodos para operaciones bancarias.

class SaldoInsuficienteError(Exception):
    """Excepción personalizada para saldo insuficiente."""
    pass

class SinCuentaCorrienteError(Exception):
    """Excepción personalizada para usuarios sin cuenta corriente."""
    pass

class UsuarioBanco:
    """
    Clase que representa a un usuario de un banco.
    """
    
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        """
        Inicializa un usuario de banco.
        
        Args:
            nombre (str): Nombre del usuario.
            saldo (float): Saldo inicial del usuario.
            tiene_cuenta_corriente (bool): True si tiene cuenta corriente, False si no.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente
    
    def retirar_dinero(self, cantidad):
        """
        Retira dinero del saldo del usuario.
        
        Args:
            cantidad (float): Cantidad a retirar.
        
        Raises:
            SinCuentaCorrienteError: Si el usuario no tiene cuenta corriente.
            SaldoInsuficienteError: Si el saldo es insuficiente.
        """
        # Verificar si tiene cuenta corriente
        if not self.tiene_cuenta_corriente:
            raise SinCuentaCorrienteError(f"{self.nombre} no tiene cuenta corriente.")
        
        # Verificar si hay saldo suficiente
        if self.saldo < cantidad:
            raise SaldoInsuficienteError(f"{self.nombre} no tiene saldo suficiente. Saldo actual: {self.saldo}")
        
        # Retirar dinero
        self.saldo -= cantidad
        print(f" {self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")
    
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere dinero desde este usuario a otro usuario.
        
        Args:
            otro_usuario (UsuarioBanco): Usuario que recibirá el dinero.
            cantidad (float): Cantidad a transferir.
        
        Raises:
            SinCuentaCorrienteError: Si alguno de los usuarios no tiene cuenta corriente.
            SaldoInsuficienteError: Si el saldo es insuficiente.
        """
        # Verificar si ambos tienen cuenta corriente
        if not self.tiene_cuenta_corriente:
            raise SinCuentaCorrienteError(f"{self.nombre} no tiene cuenta corriente.")
        
        if not otro_usuario.tiene_cuenta_corriente:
            raise SinCuentaCorrienteError(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        
        # Verificar si hay saldo suficiente
        if self.saldo < cantidad:
            raise SaldoInsuficienteError(f"{self.nombre} no tiene saldo suficiente. Saldo actual: {self.saldo}")
        
        # Realizar transferencia
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        print(f"Transferencia exitosa: {self.nombre} → {otro_usuario.nombre} ({cantidad})")
        print(f"   Saldo {self.nombre}: {self.saldo}")
        print(f"   Saldo {otro_usuario.nombre}: {otro_usuario.saldo}")
    
    def agregar_dinero(self, cantidad):
        """
        Agrega dinero al saldo del usuario.
        
        Args:
            cantidad (float): Cantidad a agregar.
        """
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")
    
    def __str__(self):
        """Representación en string del usuario."""
        cuenta = "con cuenta corriente" if self.tiene_cuenta_corriente else "sin cuenta corriente"
        return f"{self.nombre}: Saldo {self.saldo} ({cuenta})"

if __name__ == "__main__":
    print("=== CASO DE USO ===\n")
    
    # 1. Crear dos usuarios
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    
    print("1. Usuarios creados:")
    print(f"   {alicia}")
    print(f"   {bob}\n")
    
    # 2. Agregar 20 unidades de saldo a Bob
    print("2. Agregar 20 a Bob:")
    bob.agregar_dinero(20)
    print()
    
    # 3. Transferencia de 80 unidades desde Bob a Alicia
    print("3. Transferencia de 80 desde Bob a Alicia:")
    try:
        bob.transferir_dinero(alicia, 80)
    except (SaldoInsuficienteError, SinCuentaCorrienteError) as e:
        print(f"Error: {e}")
    print()
    
    # 4. Retirar 50 unidades de Alicia
    print("4. Retirar 50 de Alicia:")
    try:
        alicia.retirar_dinero(50)
    except (SaldoInsuficienteError, SinCuentaCorrienteError) as e:
        print(f"Error: {e}")
    print()
    
    # Estado final
    print("=== ESTADO FINAL ===")
    print(f"   {alicia}")
    print(f"   {bob}")


#37. Crea una función procesar_texto que procesa un texto según la opción especificada.

def contar_palabras(texto):
    """
    Cuenta el número de veces que aparece cada palabra en el texto.
    
    Args:
        texto (str): Texto a analizar.
    
    Returns:
        dict: Diccionario con palabras como claves y frecuencias como valores.
    """
    # Convertir a minúsculas y dividir en palabras
    palabras = texto.lower().split()
    
    # Crear diccionario de frecuencias
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra por otra en el texto.
    
    Args:
        texto (str): Texto original.
        palabra_original (str): Palabra a reemplazar.
        palabra_nueva (str): Palabra nueva.
    
    Returns:
        str: Texto con la palabra reemplazada.
    """
    # Reemplazar palabra (sensible a mayúsculas/minúsculas)
    texto_modificado = texto.replace(palabra_original, palabra_nueva)
    return texto_modificado


def eliminar_palabra(texto, palabra):
    """
    Elimina una palabra del texto.
    
    Args:
        texto (str): Texto original.
        palabra (str): Palabra a eliminar.
    
    Returns:
        str: Texto sin la palabra especificada.
    """
    # Reemplazar palabra por cadena vacía
    texto_modificado = texto.replace(palabra, "")
    
    # Limpiar espacios múltiples
    texto_modificado = " ".join(texto_modificado.split())
    
    return texto_modificado


def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción especificada.
    
    Args:
        texto (str): Texto a procesar.
        opcion (str): Opción de procesamiento ("contar", "reemplazar", "eliminar").
        *args: Argumentos variables según la opción:
               - "contar": no requiere argumentos adicionales
               - "reemplazar": palabra_original, palabra_nueva
               - "eliminar": palabra
    
    Returns:
        Depende de la opción:
        - "contar": dict con frecuencias
        - "reemplazar": str con texto modificado
        - "eliminar": str con texto modificado
    """
    if opcion == "contar":
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        if len(args) < 2:
            return "Error: Se requieren palabra_original y palabra_nueva"
        palabra_original = args[0]
        palabra_nueva = args[1]
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    
    elif opcion == "eliminar":
        if len(args) < 1:
            return "Error: Se requiere la palabra a eliminar"
        palabra = args[0]
        return eliminar_palabra(texto, palabra)
    
    else:
        return f"Error: Opción '{opcion}' no válida. Use 'contar', 'reemplazar' o 'eliminar'"


# Caso de uso
if __name__ == "__main__":
    # Texto de ejemplo
    texto = "Python es un lenguaje de programación. Python es fácil de aprender. Python es popular."
    
    print("=== CASO DE USO: PROCESAR TEXTO ===\n")
    print(f"Texto original:\n{texto}\n")
    print("=" * 60)
    
    # 1. Contar palabras
    print("\n1. CONTAR PALABRAS")
    resultado_contar = procesar_texto(texto, "contar")
    print("Frecuencias:")
    for palabra, frecuencia in sorted(resultado_contar.items()):
        print(f"   '{palabra}': {frecuencia}")
    
    # 2. Reemplazar palabras
    print("\n2. REEMPLAZAR PALABRAS")
    print("   Reemplazar 'Python' por 'Java'")
    resultado_reemplazar = procesar_texto(texto, "reemplazar", "Python", "Java")
    print(f"   Resultado:\n   {resultado_reemplazar}")
    
    # 3. Eliminar palabra
    print("\n3. ELIMINAR PALABRA")
    print("   Eliminar 'Python'")
    resultado_eliminar = procesar_texto(texto, "eliminar", "Python")
    print(f"   Resultado:\n   {resultado_eliminar}")
    
    # 4. Pruebas adicionales
    print("\n4. PRUEBAS ADICIONALES")
    
    # Probar opción inválida
    print("\n   a) Opción inválida:")
    resultado_invalido = procesar_texto(texto, "invalida")
    print(f"      {resultado_invalido}")
    
    # Probar reemplazar sin argumentos suficientes
    print("\n   b) Reemplazar sin argumentos suficientes:")
    resultado_error = procesar_texto(texto, "reemplazar", "Python")
    print(f"      {resultado_error}")
    
    # Probar eliminar sin argumentos
    print("\n   c) Eliminar sin argumentos:")
    resultado_error2 = procesar_texto(texto, "eliminar")
    print(f"      {resultado_error2}")

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia(hora):
    """
    Determina si es de noche, de día o tarde según la hora.
    
    Args:
        hora (int): Hora en formato 24 horas (0-23).
    
    Returns:
        str: "Día", "Tarde" o "Noche".
    """
    if 6 <= hora < 12:
        return "Día (Mañana)"
    elif 12 <= hora < 20:
        return "Tarde"
    elif 20 <= hora < 24 or 0 <= hora < 6:
        return "Noche"
    else:
        return "Hora inválida"


def programa_momento_del_dia():
    """
    Programa principal que solicita la hora al usuario y determina el momento del día.
    """
    try:
        # Solicitar la hora al usuario
        hora = int(input("Ingresa la hora (0-23): "))
        
        # Validar que esté en el rango correcto
        if hora < 0 or hora > 23:
            print("Error: La hora debe estar entre 0 y 23.")
            return
        
        # Determinar momento del día
        momento = determinar_momento_del_dia(hora)
        
        # Mostrar resultado
        print(f"\n Son las {hora}:00 horas → Es de {momento}")
        
    except ValueError:
        print("Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    programa_momento_del_dia()


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def obtener_calificacion_texto(calificacion_numerica):
    """
    Convierte una calificación numérica a su equivalente en texto.
    
    Args:
        calificacion_numerica (float): Calificación numérica (0-100).
    
    Returns:
        str: Calificación en texto.
    
    Reglas:
        0-69: Insuficiente
        70-79: Bien
        80-89: Muy bien
        90-100: Excelente
    """
    if 0 <= calificacion_numerica < 70:
        return "Insuficiente"
    elif 70 <= calificacion_numerica < 80:
        return "Bien"
    elif 80 <= calificacion_numerica < 90:
        return "Muy bien"
    elif 90 <= calificacion_numerica <= 100:
        return "Excelente"
    else:
        return "Calificación inválida"

def programa_calificacion():
    """
    Programa principal que solicita la calificación del alumno y muestra su equivalente en texto.
    """
    try:
        # Solicitar calificación al usuario
        calificacion = float(input("Ingresa la calificación numérica del alumno (0-100): "))
        
        # Validar rango
        if calificacion < 0 or calificacion > 100:
            print("Error: La calificación debe estar entre 0 y 100.")
            return
        
        # Obtener calificación en texto
        calificacion_texto = obtener_calificacion_texto(calificacion)
        
        # Mostrar resultado
        print(f"\n Calificación numérica: {calificacion}")
        print(f"   Calificación en texto: {calificacion_texto}")
        
    except ValueError:
        print("Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    programa_calificacion()

#40. Escribe una función que tome dos parámetros: figura ("rectangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica según los datos proporcionados.
    
    Args:
        figura (str): Tipo de figura: "rectangulo".
        datos (tuple): Tupla con los datos necesarios:
                      - "rectangulo": (base, altura)
    
    Returns:
        float: El área de la figura.
    
    Fórmulas:
        - Rectángulo: base × altura
    """
    if figura == "rectangulo":
        # Datos necesarios: (base, altura)
        if len(datos) != 2:
            return "Error: El rectángulo requiere (base, altura)"
        base, altura = datos
        area = base * altura
        return area
    
    else:
        return f"Error: Figura '{figura}' no válida. Use 'rectangulo'"

if __name__ == "__main__":
    print("=== CÁLCULO DE ÁREA ===\n")

    print("RECTÁNGULO")
    datos_rectangulo = (5, 10)
    area_rectangulo = calcular_area("rectangulo", datos_rectangulo)
    print(f"   Datos: base = {datos_rectangulo[0]}, altura = {datos_rectangulo[1]}")
    print(f"   Área: {area_rectangulo}\n")
    
   
   #41. Programa que calcula el precio final de una compra aplicando descuentos con cupón.

def obtener_precio():
    """Solicita y valida el precio original del artículo."""
    try:
        precio = float(input("Ingresa el precio original del artículo: "))
        if precio <= 0:
            print("Error: El precio debe ser mayor a 0.")
            return None
        return precio
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return None


def obtener_descuento():
    """Pregunta si el usuario tiene cupón y obtiene el valor del descuento."""
    tiene_cupon = input("\n¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

    if tiene_cupon == "sí" or tiene_cupon == "si":
        try:
            descuento = float(input("Ingresa el valor del cupón de descuento: "))
            if descuento > 0:
                return descuento
            else:
                print("Error: El valor del cupón debe ser mayor a 0.")
                return 0
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            return 0

    elif tiene_cupon == "no":
        return 0

    else:
        print("Error: Debes responder 'sí' o 'no'.")
        return 0


def calcular_precio_final(precio_original, descuento):
    """Calcula el precio final aplicando el descuento."""
    precio_final = precio_original - descuento
    if precio_final < 0:
        precio_final = 0
    return precio_final


def mostrar_resumen(precio_original, descuento, precio_final):
    """Muestra el resumen final de la compra."""
    print("\n" + "=" * 40)
    print("RESUMEN DE COMPRA")
    print("=" * 40)
    print(f"Precio original:    {precio_original:.2f} €")
    print(f"Descuento aplicado: {descuento:.2f} €")
    print(f"Precio final:       {precio_final:.2f} €")
    print("=" * 40)


def calcular_precio_con_descuento():
    """Función principal del programa."""
    print("=== CALCULADORA DE DESCUENTOS ===\n")

    precio_original = obtener_precio()
    if precio_original is None:
        return

    descuento = obtener_descuento()
    precio_final = calcular_precio_final(precio_original, descuento)

    mostrar_resumen(precio_original, descuento, precio_final)


if __name__ == "__main__":
    calcular_precio_con_descuento()
