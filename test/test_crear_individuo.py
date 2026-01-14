from src.crear_individuo import crear_individuo
from src.constantes_mastermind import GENES, VALORES_POSIBLES
import pytest


def test_crear_individuo():        
    individuo = crear_individuo(GENES, VALORES_POSIBLES)   
    assert len(individuo) == GENES
    for color in individuo:
        assert color in VALORES_POSIBLES

