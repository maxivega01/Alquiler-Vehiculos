import registro_parcial3


# Validante para que el numero ingresado sea mayor a otro
def validate(inf, text):
    x = int(input(text))

    while x <= inf:
        x = int(input(f'ERROR (mayores a {inf}), ' + text))

    return x


# Validante para que le numero ingresado este dentro de un rango
def validate_code(inf, sup, text):
    x = int(input(text))

    while x < inf or x > sup:
        x = int(input('ERROR, ' + text))

    return x


# Generar los registros y cargarlos al vector
def cargar_datos(alquileres):

    for i in range(len(alquileres)):

        print('Vehiculo', i+1)

        num = validate(0, 'Ingrese el numero de identificacion de la operacion: ')
        desc = input('Ingrese la descricpcion del vehiculo alquilado: ')
        tipo = validate_code(1, 10, 'Ingrese el tipo de vehiculo alquilado (del 1 al 10): ')
        importe = validate(0, 'Ingrese el impote del alquiler: ')
        dias = validate(0, 'Ingrese la cantidad de dias del alquiler: ')
        print()

        alquileres[i] = registro_parcial3.Alquiler(num, desc, tipo, importe, dias)


def opcion1(alquileres):

    cargar_datos(alquileres)


# Ordenar el vector segun los importes de cada registro
def ordenar_importe(alquileres):

    for i in range(len(alquileres) - 1):
        for j in range(i + 1, len(alquileres)):

            if alquileres[i].importe > alquileres[j].importe:
                alquileres[i], alquileres[j] = alquileres[j], alquileres[i]


# Mostrar todos los datos de los registros del vector excepto el dia
def mostrar_vector_punto2(alquileres):

    for alquiler in alquileres:
        print(registro_parcial3.to_string_punto2(alquiler))


# Calcular el importe promedio
def importe_promedio(alquileres):
    total = cont = 0

    for alquiler in alquileres:
        total += alquiler.importe
        cont += 1

    return total/cont


def opcion2(alquileres):

    ordenar_importe(alquileres)

    print('LISTADO DE LOS ALQUILERES')

    print('-' * 100)
    mostrar_vector_punto2(alquileres)
    print('-' * 100)
    print()

    imp_prom = importe_promedio(alquileres)
    print('El importe promedio es de: ', imp_prom)


# Generar un vector de conteo y cargarlo con los valores contados
def cont_por_tipo(alquileres):

    vc = [0] * 10

    for alquiler in alquileres:
        vc[alquiler.tipo - 1] += 1

    return vc


# Mostrar vector de conteo
def mostrar_conteo(vc):

    for i in range(len(vc)):

        if vc[i] != 0:
            r = ''
            r += '{:<25}'.format('Tipo de vehiculo: ' + str(i+1))
            r += '{:<25}'.format('Cantidad de alquileres: ' + str(vc[i]))

            print(r)


def opcion3(alquileres):

    vc = cont_por_tipo(alquileres)

    print('-' * 50)
    mostrar_conteo(vc)
    print('-' * 50)


# Buscar el registro con mayor importe
def mayor_importe(alquileres):

    mayor = alquileres[0]

    for alquiler in alquileres:

        if alquiler.importe > mayor.importe:
            mayor = alquiler

    return mayor


# Mostrar el registro con mayor importe y su diferencia con el importe proemedio
def opcion4(alquileres):

    mayor_imp = mayor_importe(alquileres)

    print('El alquiler con mayor importe es:')

    print('-' * 120)
    print(registro_parcial3.to_string_todo(mayor_imp))
    print('-' * 120)
    print()

    print('La diferencia entre el importe mayor y el importe promedio'
          'es de: ', (mayor_imp.importe - importe_promedio(alquileres)))


# Buscar un solo registro que tenga la misma descripcion e importe ingresado
def buscar(alquileres, c, x):
    encontrado = False

    for alquiler in alquileres:

        if alquiler.descripcion == c and alquiler.importe >= x:
            encontrado = True
            return alquiler

    if not encontrado:
        return -1


# Mostrar la busqueda del registro que tenga la misma descripcion e importe ingresado
def opcion5(alquileres):
    c = input('Ingrese la descripcion del vehiculo a buscar: ')
    x = validate(0, 'Ingrese el importe del vehiculo a buscar: ')
    print()

    busqueda = buscar(alquileres, c, x)

    if busqueda != -1:
        print('VEHICULO ENCONTRADO')

        print('-' * 120)
        print(registro_parcial3.to_string_todo(busqueda))
        print('-' * 120)

    else:
        print('VEHICULO NO ENCONTRADO')
        print('No se encontro ningun alquiler cuya descripcion sea', c, 'y su importe sea igual o mayor a', x)



