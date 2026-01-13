import random 
from src.constantes_mastermind import POBLACION, GENES, VALORES_POSIBLES, TASA_MUTACION

# Crea un código secreto aleatório para el juego Mastermind
def crear_codigo_secreto(genes=GENES, valores_posibles=VALORES_POSIBLES): 
    codigo_secreto = []
    for i in range(genes):
        codigo_secreto.append(random.choice(valores_posibles))
    return codigo_secreto





# Crea un individuo aleatório (posible combinación de colores)
def crear_individuo(genes, valores_posibles):
    return [random.choice(valores_posibles) for i in range(genes)] 




# Crea una población inicial de individuos del algoritmo genético
def crear_poblacion(poblacion=POBLACION, genes=GENES, alelos=VALORES_POSIBLES): 
    return [crear_individuo(genes, alelos) for i in range(poblacion)] 




# Calcula el fitness de un individuo comparándolo con el código secreto
# El fitness es el número de colores en la posición correcta
def evaluar_fitness(individuo, codigo_secreto):
    fitness = 0
    for i in range(len(codigo_secreto)):
        if individuo[i] == codigo_secreto[i]:
            fitness += 1
    return fitness





# Selecciona los individuos con mejor fitness de la población como padres
def seleccionar_padres(poblacion, codigo_secreto):
    mejor_fitness = -1
    padres = []
 
    for individuo in poblacion:
        fitness = evaluar_fitness(individuo, codigo_secreto)
        if fitness > mejor_fitness:
            mejor_fitness = fitness
            padres = [individuo]
        elif fitness == mejor_fitness:
            padres.append(individuo)
    return padres
  
  



# Cruza dos padres seleccionados para crear un nuevo individuo (hijo)
def cruzar_padres(padres, genes=GENES): 
    padre1 = random.choice(padres) 
    padre2 = random.choice(padres) 

    punto_cruce = random.randint(1, genes - 1) 

    hijo = []

    for i in range(genes):
        if i < punto_cruce:
            hijo.append(padre1[i])
        else:
            hijo.append(padre2[i])
    return hijo
  



# Muta aleatoriamente un individuo con una tasa de mutación dada
def mutar_individuo(individuo, tasa_mutacion=TASA_MUTACION,
valores_posibles=VALORES_POSIBLES):
    individuo_mutado = individuo.copy()
    
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo_mutado[i] = random.choice(valores_posibles)
    return individuo_mutado





# Comprueba si un individuo es la solución (código secreto)
def es_solucion(individuo, codigo_secreto):
    return evaluar_fitness(individuo, codigo_secreto) == len(codigo_secreto)






