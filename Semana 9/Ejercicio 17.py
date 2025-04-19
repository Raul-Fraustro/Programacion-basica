import re
def validr_fecha(fecha):
    patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    return re.match(patron, fecha) is not None

fecha = input("Introduzca fecha en este formtado DD/MM/AAAA: ")
print(validr_fecha(fecha))