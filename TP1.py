def mascara_leer()
    import maskpass
    password = maskpass.askpass(prompt="Ingresar contraseña: ", mask="*")
    claveUsuario = str(input())