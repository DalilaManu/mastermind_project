import random 
from src.constantes_mastermind import POBLACION, GENES, VALORES_POSIBLES
from src.crear_individuo import crear_individuo

# Crea una poblacion inicial
def crear_poblacion(poblacion=POBLACION, genes=GENES, alelos=VALORES_POSIBLES): 
    return [crear_individuo(genes, alelos) for i in range(poblacion)] 

