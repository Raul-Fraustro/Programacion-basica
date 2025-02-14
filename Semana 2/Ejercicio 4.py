n = int(input("Introduzca un numero del 1 al 50:"))

while n<1 or n>50:
    print("No es un numero del 1 al 50")
    n = int(input("Introduzca un numero del 1 al 50:"))
lista=[]

def rec_fib(n):
    if n > 1:
        return rec_fib(n - 1) + rec_fib(n - 2)
    return n


for i in range(n):
    print(rec_fib(i))