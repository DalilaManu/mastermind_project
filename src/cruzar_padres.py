import random
from src.constantes_mastermind import GENES

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
  