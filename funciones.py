
# def mostrar_menu():

#     print("=" * 50)
#     print("  SUPERMERCADO PYTHON MARKET  ")
#     print("=" * 50)
#     print("1. Cargar producto")
#     print("2. Mostrar productos")
#     print("3. Buscar producto por código")
#     print("4. Ordenar productos por precio")
#     print("5. Mostrar producto con menor stock")
#     print("6. Calcular valor total del inventario")
#     print("7. Salir")

#     opcion = input("Ingrese una opcion: ")
#     opcion = int(opcion)
    
#     return opcion




# def ejecutar_programa():

#     codigos = []
#     nombres = []
#     precios = []
#     stocks = []

#     opcion = 0

#     while opcion != 7:

#         opcion = mostrar_menu()

#         if opcion == 1:
#             cargar_producto(codigos, nombres, precios, stocks)

#         elif opcion == 2:
#             mostrar_productos(codigos, nombres, precios, stocks)

#         elif opcion == 3:
#             buscar_producto_por_codigo(codigos, nombres, precios, stocks)

#         elif opcion == 4:
#             print("Sin terminar, no llegué ;(")

#         elif opcion == 5:
#             mostrar_producto_menor_stocks(codigos, nombres, precios, stocks)

#         elif opcion == 6:
#             calcular_valor_total_inventario(codigos, nombres, precios, stocks)

#         elif opcion == 7:
#             print("Saliendo del programa...")

#         else:
#             print("Opcion invalida!")


# ejecutar_programa()



# def buscar_producto(codigo):
#     for producto in productos:
#         if producto["codigo"] == codigo:
#             print(f"su producto encontrado es {producto["nombre"]}")
#             break
#         else:
#             print("producto no encontrado")

# buscar_producto(101)


# def ordenar(lista):
#     for i in range(len(lista) - 1):
#         for j in range(len(lista) - 1):
#             if lista[j]["precio"] > lista[j + 1]["precio"]:
#                 aux = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = aux

#     for producto in lista:
#         print(f"{producto['nombre']} y {producto['precio']}")



# ordenar(lista_productos)


# def mostrar_produc():
    
#     if  len(producto) == 0:
#         print("no hay productos cargados")

    
#     for producto in productos:
#         print(f"Código: {producto['codigo']}")
#         print(f"Nombre: {producto['nombre']}")
#         print(f"Precio: ${producto['precio']}")
#         print(f"Stock: {producto['stock']}")
#         print("-" * 50)


# def pedir_entero(mensaje):
#     "si el usuario ingresa un numero positivo lo devuelve al usuario,"
#     "de lo contrario lo vuelve a pedir"

#     texto = input(mensaje)

#     while es_numero(texto) == False:
#         texto = input("Error ingrese un numero valido: ")

#     numero = int(texto)

#     return numero



# def es_numero(texto):

#     es_numero = True 
    

#     if len(texto) == 0:
#         es_numero = False   # esta vacio

#     for i in range(len(texto)):
#         if  texto[i] < "0" or texto[i] > "9":
#             es_numero = False

#     return(es_numero)



# def cargar_producto():
#     lista=[]


#     codigo = int(input("ingrese codigo"))
#     for producto in lista_productos:
#         if producto[0] == codigo:
#             print("codigo incorrecto ya existe")
#             return

#     nombre = input("ingrese producto: ")
#     precio = int(input("ingrese precio:"))
#     while precio < 0:
#         precio = int(input("reingrese precio:"))

#     stock = int(input("ingrese stock"))
#     while stock < 0: 
#         stock = int(input("reingrese stock: "))

    

#     producto = [codigo , nombre , precio , stock]
#     lista_productos.append(producto)

#     print(f"producto registrado correctamente la lista que ingreso es : {lista_productos}")


# def numerobuscado(lista):
#     codigobus = input("ingrese su codigo buscado: ")
#     posi = -1
#     for i in range(len(lista)):
#         if codigobus == lista[i]:
#             posi = i + 1

#             print(posi, codigobus)

# numerobuscado(lista_nombre)


# def buscar_producto(listas, lista ,lista): 
#     print("buscar elemento")
    
#     if len(info) == 0:
#         print("no hay productos cargados")


#     else:
#         codigo_buscado = pedir_entero("ingrese codigo a buscar")

#         posicion = buscar_indice(lista, elemento)

#         if posicion != 0:
#             print("codigo encontrado")
#             print(F"codigo, [lista{posicion}]")
#             print(F"codigo, [lista{posicion}]")
#             print(F"codigo, [lista{posicion}]")
#             print(F"codigo, [lista{posicion}]")
#         else:
#             print("no se escontro")




# def mostrar_menor(lista,lista,lista,lista):
#     print("producto con menor stock")


#     if len(lista) == 0:
#         print("vacio")

#     else:
        