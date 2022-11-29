# Escribir un programa que reciba una cadena de caracteres
# y devuelva un diccionario con cada palabra que contiene y
# su frecuencia. Escribir otra función que reciba el diccionario
# generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.
def frecuencia(fragmento):
    """" Esta funcion cuenta el numero de veces que aparece cada palabra en un texto
    Parametro:
    - fragmeto: Es una cadena de caracteres
    Salida:
    - Devuelve la frecuencia con las palabras contenidas en el fragmento
    """
    dic_frecuencias = {}
    list_palabras = fragmento.split(" ")
    for palabra in list_palabras:
        if palabra in dic_frecuencias.keys():
            dic_frecuencias[palabra] += 1
        else:
            dic_frecuencias[palabra] = 1
    return dic_frecuencias

def may_frecuencia(dic_frecuencias):
    palabra_mas_repetida = ()
    repe_max = 0
    clave_max = " "
    for palabra, repeticiones in dic_frecuencias.items():
        if repeticiones > repe_max:
            rep_max = repeticiones
            clave_max = palabra
    return (clave_max, rep_max)

print(may_frecuencia(clave_max, rep_max))