compraZapatillas = float(input("ingrese le valor de la compra: "))
#se pide que dijite el valor de la variable compraZapatillas
cantidad= int(input("ingrese la cantidad de pares de zapatos que lleva:"))
#se pide que dijite la cantidad de zapatillas
descuento1 = compraZapatillas * (1 - 0.1)
#se hace la ecuacion para aplicar el descuento
descuento2 = compraZapatillas * (1 - 0.2)
#se hace la ecuacion para aplicar el descuento
if cantidad >=3:
#se pone if para que si la cantidad de zapatillas compradas es mayor o igual a 3 se aplique un descuento del 20%
    valor= compraZapatillas - descuento2
#se aplica el descuento
    print("se aplico un descuento del 20(%)",valor)
#imprime resultados
else:
#si la cantidad de zapatillas compradas es menor a 3 se aplica el 10% de descuento
    valor= compraZapatillas - descuento1  
#se aplica el descuento
    print("se aplico un descuento del 10(%)",valor)  
#se imprime el resultado          