
num = int(input("Introduca un numero del 1 al 20: "))
while num<1 or num>20:
    print ("No selecciono el numero entre el 1 y el 20")
    num = int(input("Introduca un numero del 1 al 20: "))
factorial = 1

for i in range(1,num+1):
    factorial*=i
print(factorial)
