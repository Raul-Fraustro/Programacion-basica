edad = int(input("Introduzca edad: "))

if edad<12:
    print("Es niño")
elif edad>=12 and edad<18:
    print("Es joven")
elif edad>=18 and edad<60:
    print("Es adulto")
else:
    edad>=60
    print("Es adulto mayor")