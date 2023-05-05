

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
