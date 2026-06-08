

def cargar_producto(codigos, nombres, precios, stocks):

    codigo = (input("ingrese codigo"))
    codigo = int(codigo)
    nombre = input("ingrese producto: ")
    precio = int(input("ingrese precio:"))
    while precio < 0:
        precio = int(input("reingrese precio:"))

    stock = int(input("ingrese stock"))
    while stock < 0: 
        stock = int(input("reingrese stock: "))

    

    codigos.append(codigo)
    nombres.append(nombre)
    stocks.append(stock)
    precios.append(precio)

    return print(f"producto registrado correctamente la lista que ingreso es del producto {nombre} ")


def mostrar_productos(codigos, nombres , stocks , precios):
    
    if  len(codigos) == 0:
        print("no hay productos cargados")

    
    for producto in nombres:
        print(f"Código: {codigos}")
        print(f"Nombre: {nombres}")
        print(f"Precio: ${precios}")
        print(f"Stock: {stocks}")
        print("-" * 50)


def buscar_producto(codigos, nombres):
    codigo = int(input("ingrese su codigo: "))
    codigo = int(codigo)
    for producto in codigos:
        if codigos[producto] == codigo:
            
            print(f"su producto encontrado es {codigo}")
            break
        else:
            print("producto no encontrado")


# def ordenar(lista):
#     for i in range(len(lista) - 1):
#         for j in range(len(lista) - 1):
#             if lista[j]["precio"] > lista[j + 1]["precio"]:
#                 aux = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = aux

    for producto in lista:
        print(f"{producto['nombre']} y {producto['precio']}")



def ordenar_precio(codigos, nombres, precios, stocks):
    for i in range(len(precios)-1):
        for j in range(len(precios) -  1):
            if precios[j] > precios[j+1]:
                aux = precios[j]
                precios[j] = precios[j + 1]
                precios[j + 1] = aux

    for producto in nombres:
        print(f"{nombres} y {precios}")




def mostrar_menor_stocks(codigos, nombres, precios, stocks):
    print("producto con menor stock")


    if len(nombres) == 0:
        print("vacio")

    else:
        

        menor = stocks[0] 



        for i in range(len(nombres)):
            if menor > stocks[i]:
                menor = stocks[i]
                nombre = nombres[i]


    return print(f"el menor producto es {menor} y {nombre}")

            