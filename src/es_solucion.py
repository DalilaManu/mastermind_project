from src.evaluar_fitness import evaluar_fitness

# Comprueba si un individuo es la solución (código secreto)
def es_solucion(individuo, codigo_secreto):
    return evaluar_fitness(individuo, codigo_secreto) == len(codigo_secreto)


