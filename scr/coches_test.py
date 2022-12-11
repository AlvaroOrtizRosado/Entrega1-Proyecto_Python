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

def test_coches_por_marca():
    print("El número de coches registrados por marca es:{}"
    .format(coches_por_marcas(datos)))

def test_marca_con_más_averías():
    print(f"La marca con más averías es {marca_con_más_averías(datos)}")

def test_máximo_de_km_por_marca():
    print("El máximo de kilómetros recorridos por un coche de cada marca es:")
    print(máximo_de_km_por_marca(datos))

def test_colores_más_vendidos_por_marca(n):
    print(f"Los {n} colores más vendidos por marca son:")
    print(colores_más_vendidos_por_marca(datos, n))

def test_gráfica_km_por_marca():
    gráfica_km_por_marca(datos, "Marcas por kilómetros recorridos máximos")


#Importante
datos = lee_coches("Proyecto Python/data/coches_50.csv")

# test_lee_coches()
# test_número_marcas_distintas()
# test_media_kilómetros()
# test_max_kilómetros()
# test_marcas_con_menos_averías()
# test_agrupar_por_color("Green")
# test_coches_por_marca()
# test_marca_con_más_averías()
# test_máximo_de_km_por_marca()
# test_colores_más_vendidos_por_marca(5)
# test_gráfica_km_por_marca()