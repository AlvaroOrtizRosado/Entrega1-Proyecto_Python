from collections import namedtuple, defaultdict
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
    res = []
    with open(info_coche,encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for id,marca,color,fecha_matriculacion,averiado,kilometros,propietarios_anteriores,características,numero_bastidor in lector:
            tupla = coche(int(id),marca,color,parsea_fecha(fecha_matriculacion),parsea_boolean(averiado),float(kilometros.replace(",",".")),int(propietarios_anteriores),características,numero_bastidor)
            res.append(tupla)
    return res

def número_marcas_distintas(registros):
    res=set()
    for r in registros:
        res.add(r.marca)
    return len(res)

def media_kilómetros(registros):
    res=list()
    if len(registros)>0:
        for r in registros:
            res.append(r.kilometros)
        med_km=sum(res)/len(res)
    return med_km  

def max_kilómetros(registros, matriculación):
    res = dict()
    for r in registros:
        if matriculación == True :
            clave = r.kilometros
            if clave not in res:
                res[clave]=0
            res[clave]+=r.kilometros
    return max(res.items(),key=lambda e:e[1])[0]

def marcas_con_menos_averías(registros, n=3):
    res = dict()
    for r in registros:
        clave=r.marca
        if clave not in res:
            res[clave]=0
        res[clave]+=r.averiado
    return sorted(res.items(),
                 key=lambda e:e[1], 
                 reverse=False)[:n]

def agrupar_por_color(registros):
    res=defaultdict(list)
    for r in registros:
        res[r.color].append(r)
    return res
