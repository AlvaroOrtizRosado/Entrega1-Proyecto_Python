from coches import *

def test_lee_coches():
    print("Número de registros leídos:",len(datos))
    print("Los 3 primeros registros son:",datos[:3])
    print("Los 3 útimos registros son:",datos[-3:])

datos = lee_coches("Proyecto Python/data/coches_50.csv")

if __name__ == '__main__':
    test_lee_coches()