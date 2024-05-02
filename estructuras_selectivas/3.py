montoTotal = float(input("Ingrese el monto total de la compra: $"))
#se pide el valor total de la compra 
if montoTotal > 500000:
#se da una decision de que si el valor total es mayor a 500000 
    dineroPropio = montoTotal * 0.55
#se divide la forma de pago con su debido porcentaje    
    prestamoBancario = montoTotal * 0.30
#se obtiene el porcentaje del prestamo del banco
    creditoFabricante = (montoTotal * 0.15)
#se obtiene el porcentaje de lo que nos va a prestar el fabricante
    interes = (creditoFabricante) + (creditoFabricante * 0.2)
else:
#si no es mayor a 500000
    dineroPropio = montoTotal * 0.70
#se divide la forma de pago con su debido porcentaje
    creditoFabricante = (montoTotal * 0.3)
#se obtiene el porcentaje de lo que nos va a prestar el fabricante
    interes = (creditoFabricante) + (creditoFabricante * 0.2)
#se conoce los intereses que se deben pagar
    prestamoBancario = 0

print("Valor invertido de dinero propio: $", dineroPropio)
#se imprime el dinero propio invertido
print("Valor prestado al banco: $", prestamoBancario)
#se imprime el dinero que presto el banco
print("Valor del crédito solicitado al fabricante: $", creditoFabricante)
#se imprime el credito solicitado