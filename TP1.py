#TP1
global nombreUsuario , claveUsuario , password, opc, cont, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal
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


def pantalla_novedades():
  print("Ingrese una opción a-e")
  print("a- Crear novedades")
  print("b- Modificar novedades")
  print("c- Eliminar novedades ")
  print("d- Ver reportes")
  print("e - Volver")

#pantalla_novedades()

def pantalla():
    print("Ingrese una opcion 0-5\n")
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
        print("Gestión de locales\n")
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
menu()