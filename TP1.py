global nombreUsuario , claveUsuario , password, con, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal,cont,correcto
#INICIO
correcto=0
cont=1
nombreUsuario = "1"		
claveUsuario = "2"		
password = " "				
#opc = 1		
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



def poronga():
    global correcto,cont
    nombre=input("Ingrese el nombre:")
    password=input("Ingrese la contraseña:")
    while cont!=3 and correcto!=1:
        if(nombre==nombreUsuario and password==claveUsuario):
            correcto=1
            print("correcto",correcto)
        else:
            nombre=input("Ingrese el nombre:")
            password=input("Ingrese la contraseña:")
            cont=cont+1
            print("contar",cont)
    entro()

def entro():
    if(correcto==1):
        menu()
    else:
        print("se cierra")

def pantalla_novedades():
  print("Ingrese una opción a-e")
  print("a- Crear novedades")
  print("b- Modificar novedades")
  print("c- Eliminar novedades ")
  print("d- Ver reportes")
  print("e - Volver")

#pantalla_novedades()

def pantalla():
    print("Ingrese una opcion 0-5")
    print("1_ Gestión de locales")
    print("2_ Crear cuentas de dueños de locales")
    print("3_ Aprobar / Denegar solicitud de descuento")
    print("4_ Gestión de novedades")
    print("5_ Reporte de utilización de descuentos")
    print("0_ Fin de programa\n")

def valid_opc():
   global opc
   opc = int(input("OPCION: "))
   while opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc != 0:
      opc = int(input("Mal ingresado. Repetir opción. OPCION: "))

def menu():
  pantalla()
  valid_opc()
  match opc:
      case 1:
        print("Gestión local")
      case 2:
       print("En construcción…")
      case 3:
       print("En construcción…")
      case 4:
         print("Gestion local")
      case 5:
        print("En construcción…")
      case 0:
        print("En construcción…")

poronga()
