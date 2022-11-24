# Escribir una función que reciba una muestra de
# números en una lista y devuelva su media.
numero = [1, 2, 3, 4, 5, 6]
def media(numero):
    """" Esta funcion muestra lus numeros de una lista y devuelve la media de estos numeros
    Parametros:
        - numero: es la lista de numeros
    Salida:
        - media de los numeros de la lista"""
    return sum(numero) / len(numero)

print(numero)
print(media(numero))