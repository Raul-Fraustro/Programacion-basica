import re

def validar_ipv4(ip):
    patron = r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}' \
             r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'
    return re.match(patron, ip) is not None

ip = input("Ingresa direccion ip: ")
print(validar_ipv4(ip)) 