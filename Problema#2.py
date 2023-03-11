""" 2.	Se le solicita realizar un programa para Instituciones Educativas.  
que permita calcular el promedio de calificaciones de un estudiante.  Los datos 
disponibles para leer son el nombre, calificación 1, calificación 2, 
calificación 3 y calificación 4;  de cada uno de los cuatro exámenes pertinentes.  
La información que se debe imprimir es el Nombre, el promedio de las calificaciones y 
un comentario de "Aprobado" si se obtiene 71 o más, o "Reprobado" en caso contrario.  
El promedio se obtiene sumando las cuatro calificaciones y dividiendo la suma entre 
el total de calificaciones."""

# varibles

estudiante = ""
Calif1 = 0
Calif2 = 0
Calif3 = 0
Calif4 = 0
prom = 0

# Datos a ingresar para realizar calculo

print ("\n Bienvenido, ingrese los siguiente datos para calcular sus Calificaciones ")
estudiante = input("Ingrese el nombre del estudiante: ")
calif1 = float(input("===Ingrese la calificación 1: "))
calif2 = float(input("===Ingrese la calificación 2: "))
calif3 = float(input("===Ingrese la calificación 3: "))
calif4 = float(input("===Ingrese la calificación 4: "))

# Proceso del programa e Impresion

prom = (calif1 + calif2 + calif3 + calif4) / 4

print("Nombre del estudiante:", estudiante)
print("Promedio de calificaciones:", prom)

if prom >= 71:
    print("Aprobado")
else:
    print("Reprobado")

#Fin