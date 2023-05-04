contar=1
correcto=0
nombre = " "
nombreUsuario = "admin@shopping.com"		
claveUsuario = "12345"		
password = " "

nombre=input("Ingrese el nombre:")
password=input("Ingrese la contraseña:")

def poronga():
    while contar!= 0 or correcto=1:
        if(nombre==nombreUsuario and password==claveUsuario):
            correcto=1
        else:
            contar=contar+1
            nombre=input("Ingrese el nombre:")
            password=input("Ingrese la contraseña:")

def entro():
    if(correcto=1):
        menu()
    else:
        print("se cierra")

poronga()
entro()