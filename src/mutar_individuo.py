import random
from src.constantes_mastermind import TASA_MUTACION, VALORES_POSIBLES

# Muta aleatoriamente un individuo con una tasa de mutación dada
def mutar_individuo(individuo, tasa_mutacion=TASA_MUTACION,
valores_posibles=VALORES_POSIBLES):
    individuo_mutado = individuo.copy()
    
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo_mutado[i] = random.choice(valores_posibles)
    return individuo_mutado