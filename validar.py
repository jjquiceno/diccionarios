#nombre del archivo: validar.py
#autor: juan jose quiceno londoño
#fecha: marzo 18/2023
#descripcion: codigo que valida nombre, edad y correo
#=====================================================
while True:
    menu="""
    bienvenido al registro de usuarios, llene los campos que soliciten y seleccione un numero del 1 al 3:
    [1]digite su numbre
    [2]digite su edad
    [3]digite su correo
    [4]para salir
    """
    print(menu)
    print('=======================================================================')
    opcion=input('entre la opcion 1, 2, 3 o 4: ')
    if opcion=='1':
        while True:
            nombre=input("diga su nombre ")
            if nombre.isalpha():
                print("su nombre es: ", nombre)
                break
            else:
                print('su nombre esta mal digitado')

    elif opcion=='2':
        while True:
            edad=input('digite su edad ')
            if edad.isdecimal():
                print('su edad es: ',edad)
                break
            else: 
                print('su edad esta mal digitada')

    elif opcion=='3':
        while True:
            correo=input('digite su correo ')
            if correo.find('@')>=0 and correo.find('.')>=0:
                print('su correo es: ',correo)
                break
            else: 
                print('su correo esta mal digitado')
    
    elif opcion=='4':
        print('adios')
        exit()