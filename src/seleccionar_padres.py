import random
from src.evaluar_fitness import evaluar_fitness

def seleccionar_padres(poblacion, codigo_secreto):
    padres = []

    for i in range(len(poblacion)):
        padre1 = random.choice(poblacion)
        padre2 = random.choice(poblacion)

        if evaluar_fitness(padre1, codigo_secreto) >= evaluar_fitness(padre2, codigo_secreto):
            padres.append(padre1)
        else:
            padres.append(padre2)

    return padres
