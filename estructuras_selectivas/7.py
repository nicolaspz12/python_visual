#se define variable
cantidadLlantas = int(input("Ingrese la cantidad de llantas a comprar: "))
#se pone condicion para que segun la cantidad de llantas que compre se seleccione el precio
if cantidadLlantas < 5:
    precioLlanta = 300
elif 5 <= cantidadLlantas <= 10:
    precioLlanta = 250
else:
    precioLlanta = 200
#se hace el calculo para definir el valor total de la compra
total = cantidadLlantas * precioLlanta
#se imprime el resultado
print("El precio por cada llanta es:", precioLlanta)
print("El total a pagar es:", total)