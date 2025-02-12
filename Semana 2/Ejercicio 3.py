num = int(input("Introduzca el numero que guste:\n"))

if num==2 or num==3 or num==5 or num==7:
    print("si es numero primo")
elif num%2==0:
    print("No es numero primo")
elif num%3==0:
    print("No es numero primo")
elif num%5==0:
    print("No es numero primo")
elif num%7==0:
    print("No es numero primo")
else:
    print("Si es numero primo")