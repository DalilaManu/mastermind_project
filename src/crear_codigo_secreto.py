import random 
from src.constantes_mastermind import GENES, VALORES_POSIBLES

# Crea un código secreto aleatório para el juego Mastermind
def crear_codigo_secreto(genes=GENES, valores_posibles=VALORES_POSIBLES): 
    codigo_secreto = []
    for i in range(genes):
        codigo_secreto.append(random.choice(valores_posibles))
    return codigo_secreto

