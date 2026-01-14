import random 


# Calcula el fitness de un individuo comparándolo con el código secreto
def evaluar_fitness(individuo, codigo_secreto):
    fitness = 0
    for i in range(len(codigo_secreto)):
        if individuo[i] == codigo_secreto[i]:
            fitness += 1
    return fitness