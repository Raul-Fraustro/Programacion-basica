def cifrado_cesar(cadena, desplazamiento):
    resultado = ""
    for caracter in cadena:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado
texto = str(input("Introduzca texto: "))
desplazamiento = int(input("Cuanto de desplazamiento: "))
texto_cifrado = cifrado_cesar(texto, desplazamiento)
print(texto_cifrado)  