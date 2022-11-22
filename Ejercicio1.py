# Escribir una función a la que se le pase una cadena <nombre>
# y muestre por pantalla el saludo ¡hola <nombre>!.

nombre =input("¿Como te llamas?")
def saludo(nombre):
    """"Funcion que devuelve un saludo al usuario.

    Parametros:
        - nombre: cadena clase str
    Salida:
        - Saludo al usuario
    """
    print("¡hola", nombre + "!")
    return

saludo(nombre)
