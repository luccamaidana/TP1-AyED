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

def pantalla_locales():
    print("Ingrese una opción a-d")
    print("a- Crear locales")
    print("b- Modificar local")
    print("c- Eliminar local")
    print("d- Volver")
pantalla_locales()



while (nombreLocal!= "*"):
    mostrar_creacio()
    nombreLocal = input("Ingrese el nombre")
    ubicacionLocal = input("Ingrese la ubicacion")
    select_rubro()
comparacion_may()
comparacion_min()
exh_loc_may()
exh_loc_min()
print("Para salir pulse 0. Para volver pulse 1.")
valid_salida()
if salida == 0 :
    Salir
else:
    Menu 