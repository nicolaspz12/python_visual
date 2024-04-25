a=(input("ingrese el nombre del vendedor:"))
#se declara una variable donde se digite el nombre del vendedor
b=int(input("ingrese el sueldo base:"))
#se declara una variable donde se digite el sueldo base
c=int(input("ingrese el valor de las comisiones:"))
#se declara una variable donde se digiten las comisiones
d=int(input("ingrese las ventas:"))
#se declara una variable donde se digiten la cantidad de ventas que se hicieron
total_comision= (d*c)
#se declara una variable con la operacion para calcula el total de la comision por venta
sueldo_total= (b+total_comision)
#se declara una variable con la operacion para calcular el valor del sueldo con las comisiones
print("el vendedor" ,a , ", tiene un sueldo base de" ,b , ", durante el mes obtuvo una comision de" ,c , "y el sueldo final es:" ,sueldo_total , )
#se imprime el resultado