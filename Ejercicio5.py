# Escribir una función que reciba una muestra de
# números en una lista y devuelva otra lista con sus cuadrados

def cuadrado(l_num):
   """" Esta funcion devuelve una lista de cuadrados de la
   lista que ha recibido
   Parametros:
   - l_num = una lista de numeros separados por comas
   Salida:
   - Una lista de cuadrados de la lista de numeros
   """
   l_num = l_num.split(",")
   l_num = list(l_num)
   l_cuadrado = []
   for cifra in l_num:
      cifra = int(cifra)
      l_cuadrado.append(cifra ** 2)
   return l_cuadrado

l_num = input("Introduzca numeros separados por comas:\n")
print(l_num)
print(cuadrado(l_num))