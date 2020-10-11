import os
import socket
import time

time.sleep(0.5)
print("1.- Saber ip de un host")
print("2.- Ping de un host")
print("3.- Nmap a la ip")

time.sleep(0.5)

eleccion = int(input("¿Qué opción desea elegir? > "))

if eleccion == 1:
    host=input("Ingresa el host > ")
    hostip=socket.gethostbyname(host)
    print("---------")
    print(hostip)
    print("----------")
elif eleccion == 2:
    host = input("Pon tu host y le hago un ping > ")
    os.system("ping " + host)
elif eleccion == 3:
    time.sleep(0.5)
    print("       1.- Intense Scan")
    print("       2.- Intense scan plus UDP")
    print("       3.- Intense scan, all TCP ports")
    print("       4.- Intense scan, no ping")
    print("       5.- Ping scan ")
    print("       6.- Quick scan ")
    print("       7.- Quick scan plus ")
    print("       8.- Quick traceroute ")
    print("       9.- Regular scan   ")
    print("       10.-Slow comprehensive scan (más poderoso, pero tarda más.)")

    print("\n")
#EN ESTA PARTE DE EL SCRIPT FLYEAD ME AYUDÓ EN LO DE STR, TE QUIERO UWU
    nmap = int(input("¿Qué tipo de escaner quieres?"))
    if nmap == 1:
        ip = input("Introduzca la ip > ")
        os.system('nmap -T4 -A -v ' +str(ip))
    elif nmap == 2:
        ip = input("Introduzca la ip > ")
        os.system("nmap -sS -sU -T4 -A -v " + str(ip))
    elif nmap == 3:
        ip = input("Introduzca la ip > ")
        os.system("nmap -p 1-65535 -T4 -A -v " + str(ip))
    elif nmap == 4:
        ip = input("Introduzca la ip > ")
        os.system("nmap -T4 -A -v -Pn " + str(ip))
    elif nmap == 5:
        ip = input("Introduzca la ip > ")
        os.system("nmap -sn " + str(ip))
    elif nmap == 6:
        ip = input("Introduzca la ip > ")
        os.system("nmap -T4 -F " + str(ip))
    elif nmap == 7:
        ip = input("Introduzca la ip > ")
        os.system(" nmap -sV -T4 -O -f --version-light " + str(ip))
    elif nmap == 8:
        ip = input("Introduzca la ip > ")
        os.system("nmap -sn --traceroute " + str(ip))
    elif nmap == 9:
        ip = input("Introduzca la ip > ")
        os.system("nmap "+ str(ip))



    
        
    






