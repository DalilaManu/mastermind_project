import random

GENES = 4
ALELOS = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
POBLACION = 100
TASA_MUTACION = 0.1

def crear_codigo_secreto(genes, alelos): 
    codigo = []
    for _ in range(genes): 
        codigo.append(random.choice(alelos))

def crear_individuo(genes, alelos):
    return [random.choice(alelos) for _ in range(genes)] 

def crear_poblacion(poblacion, genes=GENES, alelos=ALELOS): 
    return [crear_individuo(genes, alelos) for _ in range(poblacion)]
def mutacion(individuo, alelos, tasa_mutacion): 
    return [random.choice(alelos) if random.random() < tasa_mutacion else gene  
            for gene in individuo] 

def evaluar_fitness(individuo, codigo_secreto): # Evaluar el fitness de un individuo comparándolo con el código secreto
    fitness = 0 # Inicializar fitness en 0
    for i in range(len(individuo)):     # Iterar sobre los genes del individuo
        if individuo[i] == codigo_secreto[i]: # Comparar con el código secreto
            fitness += 1 # Incrementar fitness por cada coincidencia
    return fitness # Retornar el valor de fitness



def cruce(padre1, padre2): # Realizar cruce entre dos padres para crear dos hijos
    punto = random.randint(1, GENES - 1) # Elegir un punto de cruce aleatorio
    hijo1 = padre1[:punto] + padre2[punto:] # Crear el primer hijo
    hijo2 = padre2[:punto] + padre1[punto:] # Crear el segundo hijo
    return hijo1, hijo2   








