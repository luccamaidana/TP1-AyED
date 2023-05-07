#INICIO
def cerrar():
   return 0

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
    print("0_ Fin de programa")

#pantalla locales
def pantalla_locales():
    print("Ingrese una opción a-d\n")
    print("a- Crear locales")
    print("b- Modificar local")
    print("c- Eliminar local")
    print("d- Volver")

#pantalla_novedades
def pantalla_novedades():
  print("\nMENU Novedades")
  print("Ingrese una opción a-e\n")
  print("a- Crear novedades")
  print("b- Modificar novedades")
  print("c- Eliminar novedades ")
  print("d- Ver reportes")
  print("e- Volver")

#pantalla rubro
def pantalla_rubro():
    global rubroLocal
    print("Ingrese el rubro 1-3.")
    print("1. Indumentaria")
    print("2. Perfumería")
    print("3. Comida")

#mostrar
def mostrar1_may():
  global indu, mayRub
  print("El rubro con mayor cantidad de locales es:", indu, "con:", mayRub, "locales.")

def mostrar2_may():
  global perfu, mayRub
  print("El rubro con mayor cantidad de locales es:", perfu, "con:", mayRub, "locales.")

def mostrar3_may():
  global comi, mayRub
  print("El rubro con mayor cantidad de locales es:", comi, "con:", mayRub, "locales.")

def mostrar1_min():
  global indu, minRub
  print("El rubro con menor cantidad de locales es:", indu, "con:", minRub, "locales.")

def mostrar2_min():
  global perfu, minRub
  print("El rubro con menor cantidad de locales es:", perfu, "con:", minRub, "locales.")

def mostrar3_min():
  global comi, minRub
  print("El rubro con menor cantidad de locales es:", comi, "con:", minRub, "locales.")

#validadores
#valid menu
def valid_opc():
   global opc
   opc = input("\nOPCION: ")
   while opc != "1" and opc != "2" and opc != "3" and opc != "4" and opc != "5" and opc != "0":
      opc = input("Mal ingresado. Repetir opción. OPCION: ")

#valid opc loc
def valid_opc_loc():
    global opcloc
    opcloc = input("\nOPCION: ")
    opcloc = opcloc.lower()
    while opcloc != "a" and opcloc != "b" and opcloc != "c" and opcloc != "d":
        opcloc = input("Mal ingresado. Repetir opción. OPCION: ")
        opcloc = opcloc.lower()

#valid opc nov
def valid_opc_nov():
    global opcnov
    opcnov = input("\nOPCION: ")
    opcnov = opcnov.lower()
    while opcnov != "a" and opcnov != "b" and opcnov != "c" and opcnov != "d" and opcnov != "e":
        opcnov = input("Mal ingresado. Repetir opción. OPCION: ")
        opcnov = opcnov.lower()

#valid select rubro
def valid_selec_rubro():
    global rubroLocal
    rubroLocal = input("\nOPCION: ")
    while rubroLocal != "1" and rubroLocal != "2" and rubroLocal != "3":
        rubroLocal = input("Mal ingresado. Repetir opción. OPCION: ")

#valid salida
def valid_salida():
    global salida
    salida = input("\nOPCION: ")
    while salida != "0" and salida != "1":
        salida = input("Mal ingresado. Repetir opción. OPCION: ")

#comparadores
def comparacion_may():
    global mayRub,rub1,rub2,rub3
    if rub1>rub2 and rub1>rub3:
        mayRub=rub1
    else:
        if rub2>rub3:
            mayRub=rub2
        else:
            mayRub=rub3

def comparacion_min():
    global minRub,rub1,rub2,rub3
    if rub1<rub2 and rub1<rub3:
        minRub=rub1
    else:
        if rub2<rub3:
            minRub=rub2
        else:
            minRub=rub3

def exh_loc_may():
    global mayRub, rub1, rub2
    if mayRub==rub1:
      mostrar1_may()
    elif mayRub==rub2:
      mostrar2_may()
    else:
      mostrar3_may()

def exh_loc_min():
    if minRub==rub1:
      mostrar1_min()
    elif minRub==rub2:
      mostrar2_min()
    else:
      mostrar3_min()

#gestiones
#gestion locales
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

#gestion novedades
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

#creaciones
#crear locales
def crear_locales():
    global nombreLocal, ubicacionLocal, salida, opc
    print ("\nCreación de locales")
    print("antes",salida)
    nombreLocal = input("Ingrese un nombre para el local. Para finalizar ingrese *: ")
    while nombreLocal != "*":
        print("dentro",salida)
        ubicacionLocal = input("Ingrese la ubicacion del local: ")
        select_rubro() 
        nombreLocal = input("Ingrese un nombre para el local. Para finalizar ingrese *: ")
    comparacion_may()
    comparacion_min()
    exh_loc_may()
    exh_loc_min()
    print("\nPara crear locales pulse 0. Para volver al menu principal pulse 1.")
    valid_salida()
    if salida == "0":
        print("\nCreación de locales")
        return 0
    else:
        menu()

#selecciones
#select rubro
def select_rubro():
    global rub1,rub2,rub3
    pantalla_rubro()
    valid_selec_rubro()
    match rubroLocal:
        case "1":
            rub1 = rub1 + 1
            crear_locales()
        case "2":
            rub2 = rub2 + 1
            crear_locales()
        case "3":
            rub3 = rub3 + 1
            crear_locales()

#modulos principales
#logueo
def logueo():
    global correcto,cont
    nombre=input("Ingrese el nombre: ")
    #def mascara_leer():
    import maskpass
    password = maskpass.askpass(prompt="Ingresar contraseña: ", mask="*")
    #claveUsuario = str(input())
    #password=input("Ingrese la contraseña: ")
    while cont!=3 and correcto!=1:
        if(nombre==nombreUsuario and password==claveUsuario):
            correcto=1
        else:
            nombre=input("Ingrese el nombre: ")
            password = maskpass.askpass(prompt="Ingresar contraseña: ", mask="*")
            cont=cont+1
    if(nombre==nombreUsuario and password==claveUsuario):
       correcto=1
    if(correcto==1):
        menu()
    else:
       print("\nSaliendo...")
       return 0
    
#menu
def menu():
  pantalla()
  valid_opc()
  match opc:
      case "1":
        print("\nGestión de locales")
        gestion_locales()
      case "2":
       print("\nEn construcción…")
       menu()
      case "3":
       print("\nEn construcción…")
       menu()
      case "4":
         print("\nGestión de novedades")
         gestion_novedades()
      case "5":
        print("\nEn construcción…")
        menu()
      case "0":
        print("\nSaliendo...")
        return 0

def prog_prin():
  print("          Shopping")
  print("           Inicio\n")
  inicio()
  logueo()

prog_prin()
#FIN DEL TRABAJO. UN ORGULLO TRABAJAR CON UD. 10 cupos. creadores:joaquin pacheco sosa, valentin bustos, gaston pennice, lucca maidana