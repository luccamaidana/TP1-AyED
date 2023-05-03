#TP1
global nombreUsuario ; claveUsuario ; password; cont; opc; opcloc; opcnov; rub1; rub2;rub3 ; rubroLocal ; mayRub ; minRub ; indu ; perfu ; comi ; nombreLocal ;
#INICIO
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
def pantalla():
    print("Ingrese una opcion 0-5")
    print("Gestión de locales")
    print("Crear cuentas de dueños de locales")
    print(" Aprobar / Denegar solicitud de descuento")
    print("Gestión de novedades")
    print("Reporte de utilización de descuentos")
    print("Fin de programa")