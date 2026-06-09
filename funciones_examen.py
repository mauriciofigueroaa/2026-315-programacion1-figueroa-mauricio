

def cargar_producto(codigos, nombres, precios, stocks):

    codigo = (input("ingrese codigo"))
    if es_numero(codigo) == False:
        codigo = input("ingrese el codigo correctamente: ")
    codigo = int(codigo)
    nombre = input("ingrese producto: ")
    precio = (input("ingrese precio:"))
    if es_numero(precio) == False:
        precio= input("reingrese el numero correctamente: ")
    while precio < 0:
        precio = int(input("reingrese precio:"))
    precio = int(precio)
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


def buscar_producto(codigos):
    codigo = int(input("ingrese su codigo: "))
    codigo = int(codigo)
    for producto in codigos:
        if codigos[producto] == codigo:
            
            print(f"su producto encontrado es {codigo}")
            break
        else:
            print("producto no encontrado")




    for producto in lista:
        print(f"{producto['nombre']} y {producto['precio']}")



def ordenar_precio(nombres, precios):
    for i in range(len(precios)-1):
        for j in range(len(precios) -  1):
            if precios[j] > precios[j+1]:
                aux = precios[j]
                precios[j] = precios[j + 1]
                precios[j + 1] = aux

    for i in range(len(precios)):
        print(f"{precios}  ,{nombres} ")
        








def mostrar_menor_stocks(nombres, stocks):
    print("producto con menor stock")


    if len(nombres) == 0:
        print("vacio")

    else:
        

        menor = stocks[0] 



        for i in range(len(nombres)):
            if menor > stocks[i]:
                menor = stocks[i]
                nombre_menor = nombres[i]
            else:
                menor = stocks[0]
                nombre_menor = nombres[0]

    return print(f"el menor producto es tiene de stock{menor} y el nombre del producto es : {nombre_menor}")

            

def calcular_valor_inventario(precios, stocks):

    total = 0

    for i in range(len(precios)):
        
        valor = precios[i] * stocks[i]

        total += valor
        print(f"{precios[i]} * {stocks[i]}")


    return print(f"el valor total del inventario es de {total}")



def es_numero(texto):

    es_numero = True 
    

    if len(texto) == 0:
        es_numero = False   # esta vacio

    for i in range(len(texto)):
        if  texto[i] < "0" or texto[i] > "9":
            es_numero = False

    return(es_numero)