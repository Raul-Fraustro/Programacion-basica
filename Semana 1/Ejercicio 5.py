pre = float(input("Introduzca precio: "))
desc = float(input("Introduzca descuento: "))

if desc>1:
    desc=desc/100

des = pre*desc

print("Total", pre-des)