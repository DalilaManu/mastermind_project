from src.genetico import  GENES, VALORES_POSIBLES, evaluar_fitness
import pytest

def test_evaluar_fitness():
    codigo_secreto = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']
    individuo_correcto = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']
    individuo_parcial = ['ROJO', 'MORADO', 'VERDE', 'NARANJA']
    individuo_incorrecto = ['NARANJA', 'MORADO', 'AZUL', 'VERDE']
    
    fitness_correcto = evaluar_fitness(individuo_correcto, codigo_secreto)
    fitness_parcial = evaluar_fitness(individuo_parcial, codigo_secreto)
    fitness_incorrecto = evaluar_fitness(individuo_incorrecto, codigo_secreto)
    
    assert fitness_correcto == GENES
    assert fitness_parcial == 2
    assert fitness_incorrecto == 0