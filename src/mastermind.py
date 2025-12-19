import random

GENES = 4
VALORES_POSIBLES = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
POBLACION = 50
TASA_MUTACION = 0.01



def crear_codigo_secreto(genes, valores_posibles): 
    codigo_secreto = []
    for i in range(genes): # 0 a 3 
        codigo_secreto.append(random.choice(valores_posibles))
    return codigo_secreto


def crear_individuo(genes, valores_posibles):
    return [random.choice(valores_posibles) for i in range(genes)] 





def crear_poblacion(poblacion=POBLACION, genes=GENES, alelos=VALORES_POSIBLES): 
    return [crear_individuo(genes, alelos) for i in range(poblacion)] 





def evaluar_fitness(individuo, codigo_secreto):
    fitness = 0
    for i in range(GENES):
        if individuo[i] == codigo_secreto[i]:
            fitness += 1
    return fitness


def seleccionar_padres(poblacion, codigo_secreto):
    # Calcular el fitness de cada individuo
    fitness_poblacion = [] 
    for individuo in poblacion:
        fitness = evaluar_fitness(individuo, codigo_secreto)
        fitness_poblacion.append((individuo, fitness)) 
        mejor_fitness = max(fitness for individuo, fitness in fitness_poblacion) 
     # Seleccionar los individuos con el mejor fitness
    padres = [individuo for individuo, fitness in fitness_poblacion if fitness == mejor_fitness] 
    return padres
  
def cruzar_padres(padres, genes=GENES): 
    padre1 = random.choice(padres) 
    padre2 = random.choice(padres) 
    punto_cruce = random.randint(1, genes - 1) 
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo

def mutar_individuo(individuo, tasa_mutacion=TASA_MUTACION,
valores_posibles=VALORES_POSIBLES):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = random.choice(valores_posibles)
    return individuo









 








