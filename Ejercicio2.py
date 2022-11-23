# Escribir una función que reciba un número entero
# positivo y devuelva su factorial. Realiza el ejercicio
# mediante bucles interactivos y mediante una función recursiva.

def factorial_bucle(num):
    """Funcion que calcula el factorial del numero que pida el usuario
    Parametros:
        - num : Un numero real
    Salida:
        - Un numero real con el factorial calculado
    """

    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i

    return factorial


def factorial_recursiva(num):
    """Funcion que calcula el factorial del numero que pida el usuario
    Parametros:
        - num : Un numero real
    Salida:
        - Un numero real con el factorial calculado
    """
    if num == 1:
        return 1
    else:
        return num * factorial_recursiva(num-1)

num = int(input("Introduce un mumero\n"))

print(factorial_bucle(num))
print(factorial_recursiva(num))

