def escribir_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
    except IOError as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")
nombre_archivo = input("Escriba el nombre del archivo: ")
contenido = input("Ingrese el contenido que quiere agregar al archivo: ")

print(escribir_archivo(nombre_archivo,contenido))