# Escribir una función que convierta un número decimal en
# binario y otra que convierta un número binario en decimal

def binario(num):
    """" Esta funcion convierte un numero decimal en binario
    Parametro:
    - num: es un numero entero
    Salida:
    - Un numero decimal correspondiente a n
    """
    binario = " "
    while num // 2 != 0:
        binario = str(num % 2) + binario
        num = num // 2
    return str(num) + binario

def decimal(num):
    """" Esta funcion convierte un numero decimal en decimal
    Parametro: numero
    - num: numero entero
    Salida:
    - Un numero binario que corresponde a num
    """
    l_binario = list(binario(num))
    l_binario.reverse()
    l_binario.remove(" ")
    suma_binario = []
    posicion = 0
    for cifra in l_binario:
        if cifra == "1":
            suma_binario.append(2 ** posicion * int(cifra))
            posicion += 1
        else:
            posicion += 1
    return sum(suma_binario)


num = int(input("Introduce un numero decimal para convertir en binario:\n"))
print("El numero binario es: ", binario(num))
print("El numero decimal es: ", decimal(num))


