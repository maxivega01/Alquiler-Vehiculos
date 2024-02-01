
# Creacion de registro
class Alquiler:

    def __init__(self, num, desc, tipo, importe, dias):

        self.numero = num
        self.descripcion = desc
        self.tipo = tipo
        self.importe = importe
        self.dias = dias


# Imprimir todos los datos del registro menos la cantidad de dias
def to_string_punto2(alquiler):

    r = ''
    r += '{:<25}'.format(' | Numero: ' + str(alquiler.numero))
    r += '{:<25}'.format(' | Descripción: ' + alquiler.descripcion)
    r += '{:<25}'.format(' | Tipo: ' + str(alquiler.tipo))
    r += '{:<25}'.format(' | Importe: ' + str(alquiler.importe))

    return r


# Imprimir todos los datos del registro
def to_string_todo(alquiler):

    r = ''
    r += '{:<25}'.format(' | Numero: ' + str(alquiler.numero))
    r += '{:<25}'.format(' | Descripción: ' + alquiler.descripcion)
    r += '{:<25}'.format(' | Tipo: ' + str(alquiler.tipo))
    r += '{:<25}'.format(' | Importe: ' + str(alquiler.importe))
    r += '{:<25}'.format(' | Dias: ' + str(alquiler.dias))

    return r
