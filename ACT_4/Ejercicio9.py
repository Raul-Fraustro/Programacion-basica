def ordenamiento(list1,list2):
    list3 = sorted(list1+list2)
    return list3
list1 = []
list2 = []
n1 = int(input("Cuantso elementos quieres en tu lista 1: "))
n2 = int(input("Cuantos elementos quieres en tu lista 2: "))
for i in range(n1):
    list1.append(int(input(": ")))
for i in range(n2):
    list2.append(int(input(": ")))

resultado = ordenamiento(list1,list2)
print(resultado)
    