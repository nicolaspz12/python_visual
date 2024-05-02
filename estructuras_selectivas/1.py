nota1 = float(input("digite la primera nota:"))
#se pide la variable de nota
nota2 = float(input("digite la segunda nota:"))
#se pide la variable de nota
nota3 = float(input("digite la tercera nota:"))
#se pide la variable de nota
promedio= (nota1 + nota2 + nota3)/3
#se calcula el promedio sumando las 3 notas digitadas y dividiendolo en la cantidad de notas
if promedio >=70:
#el if ayuda a tomar una decision en este caso ayuda a calcular si el estudiante aprobo
    print ("el estudiante aprueba", promedio)
#imprime el resultado de la decision
else:    
    print("el estudiante reprueba",promedio)   
#imprime el resultado de la decision    