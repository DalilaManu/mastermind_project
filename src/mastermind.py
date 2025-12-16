import random

GENES = 4
VALORES_POSIBLES = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
POBLACION = 50


def crear_codigo_secreto(genes, alelos): 
    codigo_secreto = []
    for i in range(genes):
        codigo_secreto.append(random.choice(alelos))
    return codigo_secreto 
print(crear_codigo_secreto(GENES, VALORES_POSIBLES))


def crear_individuo(genes, alelos):
    return [random.choice(alelos) for i in range(genes)]
print(crear_individuo(GENES, VALORES_POSIBLES)) 





def crear_poblacion(poblacion, genes=GENES, alelos=VALORES_POSIBLES): 
    return [crear_individuo(genes, alelos) for i in range(poblacion)] 
print(crear_poblacion(POBLACION)) 





def evaluar_fitness(individuo, codigo_secreto):
    fitness = 0
    for i in range(GENES):
        if individuo[i] == codigo_secreto[i]:
            fitness += 1
    return fitness
print(evaluar_fitness(['ROJO', 'AZUL', 'VERDE', 'AMARILLO'], ['ROJO', 'NARANJA', 'VERDE', 'MORADO'])) #ejemplo de uso











