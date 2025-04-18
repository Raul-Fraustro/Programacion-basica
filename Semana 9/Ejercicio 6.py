empleados = []

# Leer el archivo
with open('empleados.txt', 'r') as archivo:
    lineas = archivo.readlines()[2:]  # Saltar encabezado y separador

    for linea in lineas:
        partes = linea.strip().split()
        if len(partes) >= 3:
            nombre = partes[0]
            edad = int(partes[1])
            salario = float(partes[3])
            empleados.append({
                'nombre': nombre,
                'edad': edad,
                'salario': salario
            })

# Calcular salario promedio
if empleados:
    total_salarios = sum(emp['salario'] for emp in empleados)
    promedio = total_salarios / len(empleados)

    # Mostrar datos
    print("Empleados cargados:")
    for emp in empleados:
        print(f"Nombre: {emp['nombre']}, Edad: {emp['edad']}, Salario: ${emp['salario']:.2f}")

    print(f"\n Salario promedio: ${promedio:.2f}")
else:
    print("No se encontraron empleados en el archivo.")