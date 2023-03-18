frutas={"Platano":10000, "Manzana":12000, "Pera":8500, "Naranja":7000, "Sandia":20000, "Uva":5000, "Banano":2500, "Coco":9000}
fruta=input("que fruta quieres?").title()
kg=float(input("cuantos kilos?"))

if fruta in frutas:
    print(kg, "kilos de", fruta, "valen $", frutas[fruta]*kg)
else: 
    print("lo sentimos la fruta", fruta, "no se encuentra disponible")

