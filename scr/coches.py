from collections import namedtuple
import csv
from datetime import datetime

coche = namedtuple('coche','id,marca,color,fecha_matriculacion,averiado,kilometros,propietarios_anteriores,características,numero_bastidor')



def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y")


def parsea_boolean(cadena):
    if cadena == "VERDADERO":
        return True
    else:
        return False
        
def lee_coches(info_coche):
    #res = list
    res = []
    with open(info_coche,encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for id,marca,color,fecha_matriculacion,averiado,kilometros,propietarios_anteriores,características,numero_bastidor in lector:
            tupla = coche(int(id),marca,color,parsea_fecha(fecha_matriculacion),parsea_boolean(averiado),float(kilometros.replace(",",".")),int(propietarios_anteriores),características,numero_bastidor)
            res.append(tupla)
    return res


