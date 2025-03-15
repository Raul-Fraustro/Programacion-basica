def eliminar_espacios_extras(cadena):
    return " ".join(cadena.split())

tex = str(input("Introduzca texto: "))
print(eliminar_espacios_extras(tex))