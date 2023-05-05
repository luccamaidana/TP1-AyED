#INICIO
def inicio():
    global nombreUsuario , claveUsuario , password, con, opc, opcloc, opcnov, rub1, rub2, rub3, rubroLocal, mayRub, minRub, indu, perfu, comi, nombreLocal,cont,correcto
    correcto=0
    cont=1
    nombreUsuario = "admin@shopping.com"		
    claveUsuario = "12345"		
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

def logueo():
    global correcto,cont
    nombre=input("Ingrese el nombre:")
    password=input("Ingrese la contraseña:")
    while cont!=3 and correcto!=1:
        if(nombre==nombreUsuario and password==claveUsuario):
            correcto=1
        else:
            nombre=input("Ingrese el nombre:")
            password=input("Ingrese la contraseña:")
            cont=cont+1
    entro()
