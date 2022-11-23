# Escribir una función que calcule el área de un círculo
# y otra que calcule el volumen de un cilindro usando la
# primera función

def area_circulo(a):
    """" La funcion calcula el area del circulo
    Parametros:
        - a : numero real con el radio del circulo
    Salida:
        Un numero real con el area del ciculo especificada.
    """
    return (a**2)*3.14

def volumen_cilindro(a, h):
    """" La funcion calcula el volumen de un cilindro
    Parametros:
        - h : numero real que representa la altura de cilindro
    Salida:
        Un numero real con el volumen del cilindro especificada.
    """
    return h * area_circulo(a)

a = int(input("Introduce el radio del circulo\n"))
h = int(input("Introduce la altura del cilindro\n"))
print(area_circulo(a))
print(volumen_cilindro(h))