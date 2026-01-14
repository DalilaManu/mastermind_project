import random 
from src.constantes_mastermind import GENES, VALORES_POSIBLES



# Crea un individuo aleatório (posible combinación de colores)
def crear_individuo(genes, valores_posibles):
    return [random.choice(valores_posibles) for i in range(genes)] 