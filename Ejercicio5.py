# Escribir una función que reciba una muestra de
# números en una lista y devuelva otra lista con sus cuadrados
lista_cuadrado =[]
def cuadrado(lista_num):
    """" """
    lista_num = list(lista_num)
    for numero in lista-num:
        lista_cuadrado = numero ** 2 + lista_cuadrado
    return lista_cuadrado

lista_num = input("Introduzca numeros separados por comas:\n")
print(cuadrado(lista_num))


