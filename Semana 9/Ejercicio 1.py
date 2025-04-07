def nombre(n):
    lista=list()
    for i in range(n):
        lista.append(input(f"{i+1}. Introduzca nombre: "))
    
    nombre_archivo = "nombres.txt"
    with open(nombre_archivo, "w") as archivo:
        for nombre in lista:
            archivo.write(nombre + "\n")
    print(nombre_archivo)

nombre(n=int(input("Cuantas nombres quieres: ")))