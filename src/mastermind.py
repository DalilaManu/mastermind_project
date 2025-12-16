import random

TAMANHO_GENES = 4
VALORES_POSIBLES = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
TAMANHO_POBLACION = 100
TASA_MUTACION = 0.1

def crear_codigo_secreto(tamanho_genes, valores_posibles): # Crear un código secreto aleatorio
    codigo = [] # Inicializar lista vacía para el código
    for _ in range(tamanho_genes): # Añadir genes al código
        codigo.append(random.choice(valores_posibles)) # Elegir un color aleatorio
    return codigo

def crear_individuo(tamanho_genes, valores_posibles):
    return [random.choice(valores_posibles) for _ in range(tamanho_genes)] # Crear un individuo aleatorio

def crear_poblacion(tamanho_poblacion, tamanho_genes=TAMANHO_GENES, valores_posibles=VALORES_POSIBLES): 
    return [crear_individuo(tamanho_genes, valores_posibles) for _ in range(tamanho_poblacion)]# Crear una población de individuos

def mutacion(individuo, valores_posibles, tasa_mutacion): # Mutar un individuo con una tasa de mutación dada
    return [random.choice(valores_posibles) if random.random() < tasa_mutacion else gene  # Mantener el gen original
            for gene in individuo] # Mutar cada gen según la tasa de mutación

def evaluar_fitness(individuo, codigo_secreto): # Evaluar la aptitud de un individuo comparándolo con el código secreto
    return sum(ind == cs for ind, cs in zip(individuo, codigo_secreto)) # Contar coincidencias exactas


def cruce(padre1, padre2): # Realizar cruce entre dos padres para crear dos hijos
    punto = random.randint(1, TAMANHO_GENES - 1) # Elegir un punto de cruce aleatorio
    hijo1 = padre1[:punto] + padre2[punto:] # Crear el primer hijo
    hijo2 = padre2[:punto] + padre1[punto:] # Crear el segundo hijo
    return hijo1, hijo2   





