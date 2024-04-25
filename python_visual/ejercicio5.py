compra=float(input("digite el valor de su compra:"))
#se declara una variable para que el cliente digite el valor de la compra
descuento=float(input("digite el valor del descuento (%):"))
#se declara una variable para que el cliente digite el valor del descuento
valor_con_descuento= compra * (descuento/100)
#se declara una variable para que haga la operacion de aplicar el descuento a la compra
valor_total= compra-valor_con_descuento
#se declara una vaiable para que le reste el descuento a el valor a la compra 
print("la compra fue", compra, ",con un descuento de", valor_con_descuento, ", y el Valor final a pagar:", valor_total, )
#se imprime el resultado