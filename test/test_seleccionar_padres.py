
from src.genetico import seleccionar_padres, crear_individuo
import pytest


def test_seleccionar_padres():
    codigo_secreto = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']
    individuo1 = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']  # Fitness 4
    individuo2 = ['ROJO', 'MORADO', 'VERDE', 'NARANJA']  # Fitness 2
    individuo3 = ['NARANJA', 'MORADO', 'AZUL', 'VERDE']  # Fitness 0
    individuo4 = ['ROJO', 'AZUL', 'VERDE', 'NARANJA']  # Fitness 3

    poblacion = [individuo1, individuo2, individuo3, individuo4]

    padres = seleccionar_padres(poblacion, codigo_secreto)

    assert len(padres) == 1
    assert padres[0] == individuo1
