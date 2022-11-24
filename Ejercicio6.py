# Escribir una función que convierta un número decimal en
# binario y otra que convierta un número binario en decimal

def binario(num):
    binario = " "
    if num // 2 != 0:
        binario = str(num % 2)
        binario = list(binario)
        binario.reverse()
    num = num // 2
    print(binario)
    return

num = int(input("Introduce un numero decimal para combertir en binario:\n"))
print(binario(num))

