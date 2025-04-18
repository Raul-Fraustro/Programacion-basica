nombre_archivo = "estudiantes.txt"

def leer_estudiantes(nombre_archivo):
    estudiantes = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            estudiante = {"nombre":partes[0], "edad":partes[1],"calificaciones": list(map(int,partes[2:]))}
            estudiantes.append(estudiante)
    return estudiantes

def guardar_estudiantes(nombre_archivo, estudiantes):
    with open(nombre_archivo, "w") as archivo:
        for est in estudiantes:
            linea = f"{est["nombre"]}",f"{est["edad"]}",",".join(map(str,est["calificaciones"]))
            archivo.write(linea)
        
def imprimir_estudiantes(estudiantes):
    for est in estudiantes:
        print(f"{est["nombre"]}",{est["edad"]},",".join(map(str,est["calificaciones"])))

n = int(input("quieres cambiar los datos de un estudiante 1-si/2-no "))
if n == 1:
    def modificar_estudiante(estudiantes, nombre):
        for est in estudiantes:
            if est['nombre'].lower() == nombre.lower():
                nueva_edad = int(input(f"Nueva edad para {nombre}: "))
                nuevas_calificaciones = input(f"Nuevas 5 calificaciones para {nombre} (separadas por coma): ").split(',')
                est['edad'] = nueva_edad
                est['calificaciones'] = list(map(int, nuevas_calificaciones))
                print(f"Estudiante '{nombre}' modificado con éxito.")
                return
        print(f"No se encontró al estudiante '{nombre}'.")


estudiantes = leer_estudiantes(nombre_archivo)
modificar_estudiante(estudiantes, nombre=input("introduzca el nombre del estudiante que quiere cambiar"))
imprimir_estudiantes(estudiantes)