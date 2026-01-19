import random
from src.seleccionar_padres import seleccionar_padres
from src.evaluar_fitness import evaluar_fitness

def test_seleccionar_padres_basico():
    poblacion = ["AAAA", "BBBB", "CCCC"]
    codigo_secreto = "AAAA"

    random.seed(0)
    padres = seleccionar_padres(poblacion, codigo_secreto)

    # 1. Debe devolver el mismo tamaño
    assert len(padres) == len(poblacion)

    # 2. Todos los padres deben estar en la población original
    assert all(p in poblacion for p in padres)

    # 3. El mejor individuo según fitness debe aparecer al menos una vez
    mejor = max(poblacion, key=lambda ind: evaluar_fitness(ind, codigo_secreto))
    assert mejor in padres
def test_seleccionar_padres_igual_fitness():
    poblacion = ["ABCD", "ABCD", "EFGH"]
    codigo_secreto = "ABCD"

    random.seed(1)
    padres = seleccionar_padres(poblacion, codigo_secreto)

    # 1. Debe devolver el mismo tamaño
    assert len(padres) == len(poblacion)

    # 2. Todos los padres deben estar en la población original
    assert all(p in poblacion for p in padres)

    # 3. El individuo con mejor fitness debe aparecer al menos una vez
    mejor = max(poblacion, key=lambda ind: evaluar_fitness(ind, codigo_secreto))
    assert mejor in padres