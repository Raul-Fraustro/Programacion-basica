tex = str(input("Inroduzca texto o oracion: "))
vocales=0
consonantes=0
TEX = tex.upper()
for i in TEX:
    if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vocales+=1
    elif i==" ":
        consonantes=consonantes
    else:
        consonantes+=1
print(f"Vocales: {vocales}",f"Consonantes: {consonantes}")
