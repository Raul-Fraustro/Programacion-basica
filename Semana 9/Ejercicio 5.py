n = int(input("Cuantos empleados quiere: "))
lista_empleado = []
for i in range(n):
    nombre = input(f"Introduzca nombre {i+1}: ")
    edad = int(input("Introduzca edad: "))
    salario = float(input("Introduzca salario: "))
    diccionario_empleado = {"nombre":nombre, "edad":edad, "salario":salario}
    lista_empleado.append(diccionario_empleado)

nombre_archivo = 'empleados.txt'

with open(nombre_archivo, 'w') as archivo:
    archivo.write(f"{'Nombre':<15} {'Edad':<5} {'Salario':>10}\n")
    archivo.write("="*35 + "\n")
    for emp in lista_empleado:
        archivo.write(f"{emp['nombre']:<15} {emp['edad']:<5} ${emp['salario']:>9.2f}\n")



print(nombre_archivo)