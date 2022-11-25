# Escribir una función que convierta un número decimal en
# binario y otra que convierta un número binario en decimal

def binario(num):
    """" """
    binario = " "
    while num // 2 != 0:
        binario = str(num % 2) + binario
        num = num // 2
    return str(num) + binario

def decimal(num):
    """" """
    num_dec = 0

    for a, b in enumerate(int(binario(num[::-1]))):
        numero_dec += int(b) * 2 ** a
        return num_dec

num = int(input("Introduce un numero decimal para convertir en binario:\n"))
print("Numero decimal a binario es: "+ binario(num))
print("Numero binario convertido a decimal es: " + decimal(num))


