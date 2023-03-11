""""Elabore un programa que calcule e imprima el costo de un terreno cuadrado o rectangular, teniendo como datos 
el ancho y la longitud en metros, y el costo del metro cuadrado."""

print("\t\t Calculadora de terreno \n")
valor = float(input("Costo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))
longitud = float(input("Ingrese la longitud del terreno: "))

terreno = ancho*longitud
costot = terreno*valor

print("El costo total es de: ", costot)
