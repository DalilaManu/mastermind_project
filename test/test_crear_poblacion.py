import pytest
from src.crear_poblacion import crear_poblacion
from src.constantes_mastermind import POBLACION, GENES, VALORES_POSIBLES

def test_crear_poblacion():
    poblacion = crear_poblacion()
    assert len(poblacion) == POBLACION
    for individuo in poblacion:
        assert len(individuo) == GENES
        for gene in individuo:
            assert gene in VALORES_POSIBLES
