import random
#se importa la carpeta random

valorCompra = float(input("Ingrese el valor de la compra: $ "))
coloresBalota = ["verde", "amarillo", "rojo", "blanco"]
colorBalota = random.choice(coloresBalota)
#se definen variables

#se ponen decisiones para para que se aplique el descuento
if colorBalota == "verde":
    descuento = 0.2
    print ("su descuento es del 20%")
elif colorBalota == "amarillo":
    descuento = 0.0
    print ("su descuento es del 0%")
elif colorBalota == "rojo":
    descuento = 0.15
    print ("su descuento es del 15%")
elif colorBalota == "blanco":
    descuento = 0.0
    print ("su descuento es del 0%")
    
#se realizan las ecuaciones para aplicar el descuento y saber el valor total
valorPagar = (valorCompra *  descuento) 
valorDescuento = valorCompra - valorPagar
#se imprimen los resultados
print("Valor de la compra:" , valorCompra)
print("Color de la balota:" , colorBalota)
print("Valor a pagar:", valorDescuento)