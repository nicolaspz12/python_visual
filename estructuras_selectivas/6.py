#se definen variables 
promedio = float(input("ingrese el promedio obtenido en una escala del (1/10) :"))
pension = int(input("ingrese el valor de la pension :"))
#se ponen decisiones para calcular si segun el promedio se le puede aplicar el descuento y se imprimen resultados
if promedio >= 9:
    descuento = 0.3 * pension
    valorTotal = pension - descuento
    print("debe pagar la pension con (30%) de descuento", valorTotal) 
else:
    valorTotal = pension * 1.1
    print("debe pagar el valor total de la pension mas el impuesto (IVA)", valorTotal)    
        
