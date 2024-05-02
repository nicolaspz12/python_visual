#se definen variables
edad = int(input("ingrese su edad :"))
sexo = (input("ingrese su sexo (femenino/masculino) :"))
#se ponen decisiones para calcular el numero de pulsaciones y se imprimen los resultados
if sexo == "femenino":
    pulsaciones = (220 * edad) /10
    print("su numero de pulsaciones cada 10 segundos es :", pulsaciones)
elif sexo == "masculino":
    pulsaciones = (210 * edad) /10  
    print("su numero de pulsaciones cada 10 segundos es :", pulsaciones)
else:
    print("sexo no valido")    