menu="""
bienvenido al registro de usuarios, llene los campos que soliciten y seleccione un numero del 1 al 3:
[1]digite su numbre
[2]digite su edad
[3]digite su correo
"""
print(menu)
opcion=input('entre la opcion 1, 2 o 3: ')
if opcion=='1':
    nombre=input("diga su nombre ")
    if nombre.isalpha():
        print("su nombre es: ", nombre)
    else:
        print('su nombre esta mal digitado')
elif opcion=='2':
    edad=input('digite su edad')
    if edad.isalnum():
        print('su edad es: ',edad)
    else: 
        print('su edad esta mal digitada')