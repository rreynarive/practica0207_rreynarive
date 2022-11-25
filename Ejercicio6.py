# Escribir una función que convierta un número decimal en
# binario y otra que convierta un número binario en decimal

def binario(num):
    binario = " "
    while num // 2 != 0:
        binario = str(num % 2) + binario
        num = num // 2
    return str(num) + binario

num = int(input("Introduce un numero decimal para combertir en binario:\n"))
print(binario(num))

def decimal(num):
    for a, b in range(len(binario(num[::-1]))):
        numero_decimal +=  * 2 ** 




