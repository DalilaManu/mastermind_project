import random
from src.evaluar_fitness import evaluar_fitness

# Selecciona los individuos con mejor fitness de la población como padres
def seleccionar_padres(poblacion, codigo_secreto):
    padres = []
 
    for individuo in poblacion:
        fitness = evaluar_fitness(individuo, codigo_secreto)
        if fitness > mejor_fitness:
            mejor_fitness = fitness
            padres = [individuo]
        elif fitness == mejor_fitness:
            padres.append(individuo)
    return padres
  