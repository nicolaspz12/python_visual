nombre= input("Ingresa el nombre del estudiante: ")
# Solicitar al usuario que ingrese el nombre del estudiante
calif_actividades = float(input("Ingresa la calificación promedio de actividades en clase (30%): "))
#se declara una variable para solicitar al usuario que ingrese la calificación promedio de las actividades en clase
calif_proyecto = float(input("Ingresa la calificación del proyecto final (50%): "))
#se declara una variable para solicitar al usuario que ingrese la calificación del proyecto final
calif_evaluaciones = float(input("Ingresa la calificación promedio de evaluaciones parciales (20%): "))
#se declara una variable para solicitar al usuario que ingrese la calificación promedio de evaluaciones parciales
nota_final = (calif_actividades * 0.3) + (calif_proyecto * 0.5) + (calif_evaluaciones * 0.2)
#se declara una variable para calcular la nota final
print("La nota final de algoritmia del estudiante", nombre, "es:", nota_final)
# Imprimir los resultados