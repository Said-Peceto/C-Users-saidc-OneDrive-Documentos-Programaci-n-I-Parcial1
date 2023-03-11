"""En el hotel Guamúchil tiene los datos de los huéspedes, por cada huésped se tiene el nombre, apellido, edad, el tipo de 
habitación (1,2,3,4,5) y la cantidad de días que la ocupa;  se tiene un descuento de 10% si el cliente se hospeda más de 5 días, 
15% si se hospeda más de 10 días, y 20% si se hospeda más de 15 días;  de acuerdo con el tipo de habitación se tienen las tarifas:
Habitación 1 = 120.0 $
habitación 2 = 155.0 $
Habitación 3 = 210 $
Habitación 4 = 185.0 $
Habitación 5 = 400.0 $
Realice un programa qué contenga:
Realice un MENÚ con:
Ingresar información de huéspedes
Consultar información de huéspedes
Salir del sistema: En cuál el usuario deberá escribir “parcial#1”
Lea los datos de los huéspedes y almacenarla en una lista
Almacene la información en una lista.
Imprima un reporte con: Nombre del huésped, días, Tarifa, Subtotal, Descuento y Total a pagar. """
print("\t\t   Hotel Guamúchil \n ")
print("\t\t Datos de huespedes \n")

d_huesped = []
dia5 = 0.10
dia10 = 0.15
dia15 = 0.20

while True:
    print("-----Menú-----")
    print("1. Ingresar información de huéspedes")
    print("2. Consultar información de huéspedes")
    print("3. Salir del sistema")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        huesped = {}
        huesped["nombre"] = input("Ingrese el nombre del huésped: ")
        huesped["apellido"] = input("Ingrese el apellido del huésped: ")
        huesped["edad"] = int(input("Ingrese la edad del huésped: "))
        huesped["ocu"] = int(input("Ingrese los dias de hospedaje: " ))
        huesped["habi"] = int(input("Ingrese el número de habitación (1,2,3,4,5):  "))

        if huesped["habi"] == 1:
            tarifa = 120.0
        elif huesped["habi"] == 2:
            tarifa = 155.0
        elif huesped["habi"] == 3:
            tarifa = 210.0
        elif huesped["habi"] == 4:
            tarifa = 185.0
        elif huesped["habi"] == 5:
            tarifa = 400.0

        subtotal = huesped["ocu"] * tarifa

        if huesped["ocu"] > 15:
            descuento = subtotal * dia15
        elif huesped["ocu"] > 10:
            descuento = subtotal * dia10
        elif huesped["ocu"] > 5:
            descuento = subtotal * dia5
        else:
            descuento = 0

        total = subtotal - descuento

        huesped["subtotal"] = subtotal
        huesped["descuento"] = descuento
        huesped["total"] = total

        d_huesped.append(huesped)

    elif opcion == "2":
        for huesped in d_huesped:
            print("Nombre del Huesped: ",huesped["nombre"],huesped["apellido"]  )
            print("Dias de hospedaje: ", huesped["ocu"] )
            print("Tarifa: ", tarifa)
            print("Subtotal: ", huesped["subtotal"])
            print("Descuento: ", huesped["descuento"])
            print("Total a pagar: ", huesped["total"])
            print("--------------------------")

    elif opcion == "3":
        salir = input("¿Está seguro que desea salir del sistema? (Escribir: parcial#1): ")
        if salir.lower() == "parcial#1":
            print("Hasta pronto!")
            break
    else:
        print("Opción inválida. Intente nuevamente.")
