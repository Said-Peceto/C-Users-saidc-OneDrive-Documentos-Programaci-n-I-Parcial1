""" 1. Realizar un menú y submenú  mostrado en la imagen y agregar una opción para salir, escribiendo ‘’100”
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
#
expendientes = []

while True:
    print("----- MENÚ PRINCIPAL -----")
    print("1. Inicio ")
    print("2. Expendiente ")
    print("3. Reporte")
    print("4. ")
    print("Escriba '100' para Salir")

    opc = int(input("Seleccione la opcion del menu de su preferencia"))
    print("La Opcion elegida es: ", opc)

    if opc == 1:
    
    elif opc == 2:
        
        while True:
            expendiente = {}
            expendiente["Asegudora"] = input("Ingrese su Aseguradora: ")
            expendiente["Cliente"] = input("Ingrese el nombre del cliente: ")
            expendiente["Juzgado"] = int(input("Ingrese el Juzgado: "))
            expendiente["estado"] = int(input("Ingrese el estado: " ))
            expendientes.append = [expendiente]
            
            salir = input("Salir") 
            if salir.lower() =! "si":
                break
    elif opc == 3

        t_pendiente = 0
        t_curso = 0
        t_proceso = 0

        for expediente in expendientes:
            if expendiente["estado"] == "en curso":

            elif expendiente["estado"] == "proceso":
            elif expendiente["estado"] == "cerraod":
            else:
                print("Archivo no encontrado")
    
    
    elif opc == 4:
    
    elif opc == 100:
        ("Saliendo del Menu")

    else: 
        ("La opcion elegida no es correcta")
