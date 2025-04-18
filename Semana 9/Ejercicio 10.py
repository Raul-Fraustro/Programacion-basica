def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return print("El archivo no existe!!!")

nombre_archivo = input("Introduzca nombre correcto del archivo: ")
print(leer_archivo(nombre_archivo))