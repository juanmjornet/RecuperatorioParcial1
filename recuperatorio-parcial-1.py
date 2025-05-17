

productos = []
cantidades = []

def pedir_cantidad(mensaje):
    entrada = input(mensaje)
    while not entrada.isdigit():
        print("Entrada Invalida. Ingrese un numero entero positivo.")
        entrada = input (mensaje)
    return int(entrada)

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in productos:
        print("El producto ya existe")
    else:
        cantidad = pedir_cantidad("Ingrese cantidad inicial: ")
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto agregado.")

def ver_productos_agotados():
    print("\n PRODUCTOS AGOTADOS: ")
    agotados = False
    for i in range(len(productos)):
        if cantidades[i] == 0:
            print(f"- {productos[i]}")
            agotados = True
    if not agotados:
            print("No hay productos agotados.")

def actualizar_stock():
    nombre = input("Ingrese el nombre del producto a actualziar: ")
    if nombre in productos:
        index = productos.index(nombre)
        nueva_cantidad = pedir_cantidad("Ingrese la Nueva cantidad: ")
        cantidades[index] = nueva_cantidad
        print("Stock Actualizado.")
    else:
        print("El producto NO existe.")

def ver_todos_los_productos():
    print("\n Stock Completo: ")
    if not productos:
        print("No hay productos cargados.")
    else:
        for i in range(len(productos)):
            print(f"- {productos[i]}: {cantidades[i]} unidades.")
    respuesta = input("¿Desea consultar el stock de un producto específico? (s/n): ")
    if respuesta == "s":
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in productos:
            index = productos.index(nombre)
            print(f"Stock de {nombre}: {cantidades[index]} unidades")
        else:
            print("El producto no existe.")

def menu():
    while True:
        print("\n ---MENU DEL PROGRAMA---")
        print("OPCION 1: AGREGAR PRODUCTO")
        print("OPCION 2: VER PRODUCTOS AGOTADOS")
        print("OPCION 3: ACTUALIZAR STOCK")
        print("OPCION 4: VER TODOS LOS PRODUCTOS")
        print("OPCION 5: SALIR")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            ver_productos_agotados()
        elif opcion == 3:
            actualizar_stock()
        elif opcion == 4:
            ver_todos_los_productos()
        elif opcion == 5:
            print("Hasta Luego!")
            break
        else:
            print("Opcion invalida, pruebe nuevamente.")

menu()