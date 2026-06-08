

from funciones_examen import *




def main():
    codigos = []
    nombres = []
    precios = []
    stocks = []
    


    print("=" * 50)
    print("  SUPERMERCADO PYTHON MARKET  ")
    print("=" * 50)
    print("1. Cargar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por código")
    print("4. Ordenar productos por precio")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario")
    print("7. Salir")

    opcion = 0


    opcion = 0

    while opcion != 7:

        opcion = input("ingrese opcion: ")

        if opcion == "1":
            cargar_producto(codigos, nombres, precios, stocks)

        elif opcion == "2":
            mostrar_productos(codigos, nombres, precios, stocks)

        elif opcion == "3":
            buscar_producto(codigos, nombres, precios, stocks)

        elif opcion == "4":
            ordenar_precio(codigos, nombres, precios, stocks)

        elif opcion == "5":
            mostrar_producto_menor_stocks(codigos, nombres, precios, stocks)

        elif opcion == "6":
            calcular_valor_total_inventario(codigos, nombres, precios, stocks)

        elif opcion == "7":
            print("Saliendo del programa...")

        else:
            print("Opcion invalida!")











main()