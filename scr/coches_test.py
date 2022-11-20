from coches import *

def test_lee_coches():
    print("Número de registros leídos:",len(datos))
    print("Los 3 primeros registros son:",datos[:3])
    print("Los 3 útimos registros son:",datos[-3:])

def test_número_marcas_distintas():
     print ("Hay {} marcas distintas en los datos"
           .format(número_marcas_distintas(datos)))

def test_media_kilómetros():
    media = media_kilómetros(datos)
    print(f"La media de los kilómetros recorridos es {int(media)}.")

def test_max_kilómetros():
    print("EL coche matriculado con mas kilómetros ha recorrido {} kilómetros."
        .format(int(max_kilómetros(datos, True))))

def test_marcas_con_menos_averías(n=5):
    print("\n Las {} marcas con menos averías son:".
            format(n))
    for c, v in marcas_con_menos_averías(datos,n):
        print("{} ==> {}".format(c,v))

def test_agrupar_por_color(color, n=5):
    print(agrupar_por_color(datos)[color][:n])

#Importante
datos = lee_coches("Proyecto Python/data/coches_50.csv")

#test_lee_coches()
#test_número_marcas_distintas()
#test_media_kilómetros()
#test_max_kilómetros()
#test_marcas_con_menos_averías()
#test_agrupar_por_color("Green")