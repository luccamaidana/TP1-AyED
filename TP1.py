#INICIO
def inicio():
    global nombreUsuario , ubicacionLocal, salida, claveUsuario , password, cont, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal,cont,correcto
    correcto=0
    cont=1
    nombreUsuario = "admin@shopping.com"		
    claveUsuario = "12345"		
    password = " "				
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
    salida = 0
    ubicacionLocal = " "

inicio()

#pantallas
#pantalla
def pantalla():
    print("\nMENU")
    print("Ingrese una opcion 0-5\n")
    print("1_ Gestión de locales")
    print("2_ Crear cuentas de dueños de locales")
    print("3_ Aprobar / Denegar solicitud de descuento")
    print("4_ Gestión de novedades")
    print("5_ Reporte de utilización de descuentos")
    print("0_ Fin de programa\n")

#pantalla_novedades
def pantalla_novedades():
  print("pantalla_novedades")
  print("Ingrese una opción a-e")
  print("a- Crear novedades")
  print("b- Modificar novedades")
  print("c- Eliminar novedades ")
  print("d- Ver reportes")
  print("e - Volver")

#pantalla rubro
def pantalla_rubro():
    global rubroLocal
    print("Ingrese el rubro 1-3.")
    print("1. Indumentaria")
    print("2. Perfumería")
    print("3. Comida")
    rubroLocal = input()

#validadores
#valid menu
def valid_opc():
   global opc
   opc = int(input("OPCION: "))
   while opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc != 0:
      opc = int(input("Mal ingresado. Repetir opción. OPCION: "))

#valid opc loc
def valid_opc_loc():
    global opcloc
    opcloc = input()
    while opcloc != "a" and opcloc != "b" and opcloc != "c" and opcloc != "d":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")

#valid opc nov
def valid_opc_nov():
    global opcnov
    opcnov = input()
    while opcnov != "a" and opcnov != "b" and opcnov != "c" and opcnov != "d" and opcnov != "e":
        opcnov = input("Mal ingresado. Repetir opción. OPCION: ")

#valid salida
def valid_salida():
    global salida
    salida = input()
    while salida != "0" and salida != "1":
        salida = input("Mal ingresado. Repetir opción. OPCION: ")

#modulos principales
#logueo
def logueo():
    global correcto,cont
    nombre=input("Ingrese el nombre: ")
    password=input("Ingrese la contraseña: ")
    while cont!=3 and correcto!=1:
        if(nombre==nombreUsuario and password==claveUsuario):
            correcto=1
        else:
            nombre=input("Ingrese el nombre: ")
            password=input("Ingrese la contraseña: ")
            cont=cont+1
    if(nombre==nombreUsuario and password==claveUsuario):
       correcto=1
    if(correcto==1):
        menu()
    else:
       print("Saliendo...")
       return
    
#menu
def menu():
  pantalla()
  valid_opc()
  match opc:
      case 1:
        print("Gestión de locales\n")
        gestion_locales()
      case 2:
       print("En construcción…\n")
       menu()
      case 3:
       print("En construcción…\n")
       menu()
      case 4:
         print("Gestión de novedades\n")
      case 5:
        print("En construcción…\n")
        menu()
      case 0:
        print("Saliendo...")
        return

def prog_prin():
  inicio()
  logueo()

prog_prin()

#----VALEN




#CREAR LOCALES
def crear_locales():
    global ubicacionLocal
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


#VALID SELECT RUBRO
def valid_selec_rubro():
    global rubroLocal
    rubroLocal = input()
    while rubroLocal != 1 and rubroLocal != 2 and rubroLocal != 3:
        rubroLocal = input("Mal ingresado. Repetir opción. OPCION: ")

#SELECT RUBRO
def select_rubro():
    pantalla_rubro()
    valid_selec_rubro()
    match rubroLocal:
        case 1:
            rub1 = rub1 + 1
        case 2:
            rub2 = rub2 + 1
        case 3:
            rub3 = rub3 + 1