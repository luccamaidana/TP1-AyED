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

def pantalla_novedades():
  print("Ingrese una opción a-e")
  print("a- Crear novedades")
  print("b- Modificar novedades")
  print("c- Eliminar novedades ")
  print("d- Ver reportes")
  print("e - Volver")

pantalla_novedades()