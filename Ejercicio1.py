# Escribir una función a la que se le pase una cadena <nombre>
# y muestre por pantalla el saludo ¡hola <nombre>!.


def saludo(nombre):
    """"Funcion que devuelve un saludo al usuario.

    Parametros:
        - nombre: cadena clase str
    Salida:
        - Saludo al usuario
    """
    print("¡hola", nombre + "!")
    return
nombre = input("¿Como te llamas?")
saludo(nombre)
