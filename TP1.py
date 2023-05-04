#TP1
global nombreUsuario , claveUsuario , password, con, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal
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
pantalla_locales()

#PANTALLA RUBRO
def pantalla_rubro():
    print("Ingrese el rubro 1-3.")
    print("1. Indumentaria")
    print("2. Perfumería")
    print("3. Comida")
    rubroLocal = input()
pantalla_locales()

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
crear_locales()

#GESTION LOCALES (creo q esta mal)
def gestion_locales():  
    pantalla_locales()
    opcloc = input()
    while opcloc != "d":
        valid_opc_loc()
        match opcloc:
             case "a":
                crear_locales()
             case "b":
                print("En construcción")
             case "c":
                print("En construcción")
             case "d":
                menu()
    pantalla_locales()
    opcloc = input()
gestion_locales()