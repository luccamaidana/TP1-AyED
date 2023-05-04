#TP1

#INICIO
def inicio():
  global nombre, nombreUsuario, claveUsuario, password, con, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal
  nombre = " "
  nombreUsuario = "admin@shopping.com"		
  claveUsuario = "12345"		
  password = " "		
  con = 1
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
import maskpass



def menu():
    print("ENTRAsTE")


#def mascara_leer():
  #  global password
   
  # password = maskpass.askpass(prompt="Ingresar contraseña: ", mask="*")
   
   # return str(password)

#print("AFUERA",cont)

def logueo():
    inicio()
    print("ADENTRO",con)
    
    #global cont, password, nombreUsuario, claveUsuario, nombre
  
    nombre = input("Ingresar nombre de usuario: ")
    print(nombre)
    password = input("Ingresar contraseña: ")
    print(password)

#nombre != nombreUsuario and cont < 3 or password != claveUsuario
    #password = mascara_leer()

    while  claveUsuario  != password and nombreUsuario != nombre and con != 3:
        
        con = con + 1
        nombre = input("Nombre de usuario o contraseña incorrecto. Ingrese el nombre de usuario: ")

    if con == 3:
        print("Demasiados intentos. Saliendo del programa.")

    menu()

    #if(password == claveUsuario):
        #menu()
    
    #else:
        #print("Usuario o contraseña incorrectos.")

logueo()