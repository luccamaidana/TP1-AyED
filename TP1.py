#TP1
global nombreUsuario , claveUsuario , password, cont, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal
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
ubicacionLocal = " "
salida = 0	

#PANTALLA LOCALES
def pantalla_locales():
    print("Ingrese una opción a-d")
    print("a- Crear locales")
    print("b- Modificar local")
    print("c- Eliminar local")
    print("d- Volver")


#PANTALLA RUBRO
def pantalla_rubro():
    print("Ingrese el rubro 1-3.")
    print("1. Indumentaria")
    print("2. Perfumería")
    print("3. Comida")
    rubroLocal = input()

#VALID SALIDA
def valid_salida():
    global salida
    salida = input()
    while salida != "0" and salida != "1":
        salida = input("Mal ingresado. Repetir opción. OPCION: ")

#CREAR LOCALES
def crear_locales():
    print ("Creación de locales.")
    nombreLocal = input("Ingrese un nombre para el local. Para finalizar la creación de locales ingrese * ")
    while nombreLocal != "*":
        ubicacionLocal = input("Igrese la ubicacion del local ")
        select_rubro() 
        nombreLocal = input("Ingrese un nombre para el local. Para finalizar la creación de locales ingrese * ")
    comparacion_may()
    comparacion_min()
    exh_loc_may()
    exh_loc_min()
    print("Para salir pulse 0. Para volver pulse 1.")
    valid_salida()
    if salida == 0 :
        gestion_locales()
    else:
        menu()


#VALID OPC LOC
def valid_opc_loc():
    global opcloc
    opcloc = input()
    while opcloc != "a" and opcloc != "b" and opcloc != "c" and opcloc != "d":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")
#VALID OPC NOV
def valid_opc_nov():
    global opcnov
    opcnov = input()
    while opcnov != "a" and opcnov != "b" and opcnov != "c" and opcnov != "d" and opcnov != "e":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")

#GESTION LOCALES 
def gestion_locales():  
    pantalla_locales()
    valid_opc_loc()
    match opcloc:
        case "a":
            crear_locales()
        case "b":
            print("\nEn construcción...")
            gestion_locales()
        case "c":
            print("\nEn construcción...")
            gestion_locales()
        case "d":
            menu()
gestion_locales()

#GESTION NOVEDADES
def gestion_novedades():
    pantalla_novedades()
    valid_opc_nov()
    match opcnov:
        case "a":
            print("\nEn construcción...")
            gestion_novedades()
        case "b":
            print("\nEn construcción...")
            gestion_novedades()
        case "c":
            print("\nEn construcción...")
            gestion_novedades()
        case "d":
            print("\nEn construcción...")
            gestion_novedades()
        case "e":
            menu()
gestion_novedades()
