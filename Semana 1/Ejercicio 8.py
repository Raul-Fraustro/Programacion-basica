año = int(input("Introduzca edad: "))

if año<100 and año%4==0:
    print("Es bisiesto")
elif año>=100 and año%4==0 and año/100>=1:
    print("Es bisiesto")
else:
    print("No es bisiesto")
