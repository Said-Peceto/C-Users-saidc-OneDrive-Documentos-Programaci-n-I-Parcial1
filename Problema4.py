""" 1. Realizar un menú y submenú  mostrado en la imagen y agregar una opción para salir, escribiendo 100”
    2. Qué la opción de expediente permite:
        a. Agregar la información mostrada en pantallas de contenido con los de  (aseguradora, cliente, juzgado y adicional el estado) 
        b. Qué se almacene en la lista 
    3.  En la opción reporte:
        a. Imprimir cada uno de los estado qué aparece en la imagen 
        b. Qué cada estado tenga de forma numérica el total(sumatoria) con base a la información ingresada en el menú de expedientes.
    4. Al ingresar a las demás opciones del menu o submenu,  mostrar en pantalla:
        a. El nombre del menú o submenú 
        b. Descripción pantalla del menú desde su punto de vista 
        c. Su nombre y Apellido """

expendientes = []

while True:
    print("----- MENÚ PRINCIPAL -----")
    print("1. Inicio ")
    print("2. Expendiente ")
    print("3. Reporte")
    print("4. Configuración ")
    print("   Escriba '100' para Salir\n")
    print("Hecho por Said Peceto Y Davis Sánchez :D.")

    opc = int(input("Seleccione la opcion del menu de su preferencia: "))
    print("La Opcion elegida es: ", opc, "\n")

    if opc == 1:
        print("Esta es la pantalla de inició, bienvenido! \n Para regresar ingrese -> 5 ")
        exit = input("Ingresa el número para salir: ")
        if exit == '5':
            continue
        else:
            print("El número que ingreso no es el correcto.")
    elif opc == 2:
        while True:
            expendiente = {}
            expendiente["Aseguradora"] = input("Ingrese su Aseguradora: ")
            expendiente["Cliente"] = input("Ingrese el nombre del cliente: ")
            expendiente["Juzgado"] = int(input("Ingrese el Juzgado: "))
            expendiente["Estado"] = input("Ingrese el estado (pendiente, en curso o cerrado): ")
            expendientes.append(expendiente)

            salir = input("¿Desea agregar otro expediente? (si/no): ")
            if salir.lower() != "si":
                break
    elif opc == 3:
        print("\t\tREPORTE")
        t_pendiente = 0
        t_curso = 0
        t_cerrado = 0
        for expediente in expendientes:
            print("Aseguradora: ", expediente["Aseguradora"])
            print("Cliente: ", expediente["Cliente"])
            print("Juzgado: ", expediente["Juzgado"])
            print("Estado: ", expediente["Estado"])
            if expediente["Estado"] == "pendiente":
                t_pendiente += 1
            elif expediente["Estado"] == "en curso":
                t_curso += 1
            elif expediente["Estado"] == "cerrado":
                t_cerrado += 1
        print("\nTotal de expedientes pendientes: ", t_pendiente)
        print("total de expedientes en proceso: ", t_curso)
        print("Total de expedientes cerrados: ", t_cerrado)
    elif opc == 4:
        print("Sitio donde hay un submenú, en donde aparece aseguradora,usuarios y juzgado. \n Para regresar ingresa --> 50")
        sad = input("Ingresa el número para salir: ")
        if sad == '50':
            continue
    elif opc == 100:
        print("Has salido del sistema.")
