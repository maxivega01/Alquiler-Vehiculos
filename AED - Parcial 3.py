'''
Una empresa de alquiler de vehículos necesita un programa para procesar los datos de los alquileres que
tiene ofrecidos. Por cada alquiler se tienen los siguientes datos: número de identificación de esa operación,
descripción del automóvil alquilado, el tipo de vehículo
(un número entero entre 1 y 10, para indicar por ejemplo: 1: sedán cuatro puertas, 2: familiar siete asientos, etc.),
el importe a cobrar por el alquiler y la cantidad de días por los que se hace el alquiler.
Se desea almacenar la información referida a los n alquileres en un arreglo de registros de tipo Alquiler
(definir el tipo Alquiler y cargar n por teclado).


Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n alquileres. Valide que el número identificador de la operación de alquiler
sea positivo y que el tipo del vehículo esté entre 1 y 10. Puede hacer la carga en forma manual, o puede generar los datos
en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de todos los alquileres, en un listado ordenado de menor a mayor según los importes a cobrar de esos alquileres.
En el listado no incluya la visualización de la cantidad de días de alquiler. Al final del listado, mostrar una línea adicional
en la que se indique el importe promedio pagado entre todos los vehículos que se mostraron.

3- Determinar y mostrar la cantidad de alquileres que se hicieron de cada tipo posible de vehículo (un contador para los alquileres tipo 1,
otro para el tipo 2, etc.) En total, 10 contadores. Muestre solo los resultados mayores a cero.

4- Determinar y mostrar el alquiler con mayor importe. Mostrar además la diferencia entre este importe mayor,
y el importe promedio entre todos los alquileres del arreglo.

5- Determinar si fue alquilado un vehículo cuya descripción sea igual a c y que tenga un importe de x o más,
siendo c y x dos valores que se cargan por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
'''

from funciones_parcial3 import *


def prueba():
    print()

    # Ingresar la cantidad de alquileres
    n = validate(0, 'Ingrese la cantidad de alquileres: ')
    print()

    alquileres = [None] * n
    opc = None

    # Menu de opciones
    while opc != 6:

        print('-' * 25)
        print('MENU DE OPCIONES')
        print('-' * 25)
        print()

        print('Opcion 1: Cargar los datos de los alquileres')
        print('Opcion 2: Mostrar los alquileres de menor a mayor y el importe proemdio')
        print('Opcion 3: Mostrar la cantidad de alquileres por tipo de vehiculo')
        print('Opcion 4: Mostrar el alquiler con mayor importe y su diferencia con el importe proemdio')
        print('Opcion 5: Buscar algun vehiculo por su descripcion y su importe')
        print('Opcion 6: Salir del programa')
        print()

        opc = validate_code(1, 6, 'Elija una opcion: ')
        print()

        # Opcion 1
        if opc == 1:
            opcion1(alquileres)
            print()

        # Opcion 2
        elif opc == 2:
            if alquileres[0] is not None:
                opcion2(alquileres)
                print()

            else:
                print('Aun no se han cargado datos')
                print()

        # Opcion 3
        elif opc == 3:
            if alquileres[0] is not None:
                opcion3(alquileres)
                print()

            else:
                print('Aun no se han cargado datos')
                print()

        # Opcion 4
        elif opc == 4:
            if alquileres[0] is not None:
                opcion4(alquileres)
                print()

            else:
                print('Aun no se han cargado datos')
                print()

        # Opcion 5
        elif opc == 5:
            if alquileres[0] is not None:
                opcion5(alquileres)
                print()

            else:
                print('Aun no se han cargado datos')
                print()

        # Opcion 6: SALIR
        elif opc == 6:
            print('Programa Finalizado')


if __name__ == '__main__':
    prueba()
