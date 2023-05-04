#TP1
global nombreUsuario, claveUsuario, password, con, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal
#INICIO
nombre = " "
nombreUsuario = "admin@shopping.com"		
claveUsuario = "12345"		
password = " "		
cont = 0		
opc = 1		
opcloc = " "		
opcnov = " "		
rub1 = 0		
rub2 = 0		
rub3 = 0		
rubroLocal = 0		
mayRub = 0		
minRub = 0		
indu = 'indumentaria'		
perfu = "perfumería"		
comi = "comida"		
nombreLocal = " "		
import sys
import maskpass

def menu():
    print("prueba1")
menu()

def mascara_leer():
    password = maskpass.askpass(prompt="Ingresar contraseña: ", mask="*")
    return str(password)


def logueo():
    nombre = input("Ingresar nombre de usuario: ")

    while(nombre != nombreUsuario and cont < 3):
        cont = cont + 1
        nombre = input("Nombre de usuario incorrecto. Ingrese el nombre de usuario: ")

    if cont == 3:
        print("Demasiados intentos. Saliendo del programa.")

    password = mascara_leer()

    if(password == claveUsuario):
        menu()

    else:
        print("Usuario o contraseña incorrectos.")
logueo()