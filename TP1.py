#TP1
global nombreUsuario , claveUsuario , password, cont, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal , mayRub , minRub , indu , perfu , comi , nombreLocal 
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
    print("Ingrese una opcion 0-5\n")
    print("0 Gestión de locales\n")
    print("1 Crear cuentas de dueños de locales\n")
    print("2 Aprobar / Denegar solicitud de descuento\n")
    print("3 Gestión de novedades\n")
    print("4 Reporte de utilización de descuentos\n")
    print("5 Fin de programa\n")
pantalla()

def comparacion_may():
    if rub1>rub2 and rub1>rub3:
        mayRub=rub1
    else:
        if rub2>rub3:
            mayRub=rub2
        else:
            mayRub=rub3

def comparacion_min():
    if rub1<rub2 and rub1<rub3:
        minRub=rub1
    else:
        if rub2<rub3:
            minRub=rub2
        else:
            minRub=rub3

def exh_loc_may():
    if mayRub==rub1:
        print(mostrar1_may)
    else:
        if mayRub==rub2:
            print(mostrar2_may)
        else:
            print(mostrar3_may)

def exh_loc_min():
    if minRub==rub1:
        print(mostrar1_min)
    else:
        if minRub==rub2:
            print(mostrar2_min)
        else:
            print(mostrar3_min)

def mostrar1_may():
    print("El rubro con mayor cantidad de locales es: ", indu, "con: ", mayRub, "locales.")

def mostrar2_may():
    print("El rubro con mayor cantidad de locales es: ", perfu, "con: ", mayRub, "locales.")

def mostrar3_may():
    print("El rubro con mayor cantidad de locales es: ", comi, "con: ", mayRub, "locales.")

def mostrar1_min():
    print("El rubro con menor cantidad de locales es: ", indu, "con: ", minRub, "locales.")

def mostrar2_min():
    print("El rubro con menor cantidad de locales es: ", perfu, "con: ", minRub, "locales.")

def mostrar3_min():
        print("El rubro con menor cantidad de locales es: ", comi, "con: ", minRub, "locales.")