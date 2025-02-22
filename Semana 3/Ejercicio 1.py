
def persona(nombre, edad):
    if edad=="":
        print(f"Hola {nombre}",f"Con 18 años")
    else:
        print(f"Hola {nombre}",f"Con {edad} años")
        return
persona(input("Introduzca su nombre: "),input("Introduzca su edad: "))