

from src.mastermind import crear_individuo, GENES, ALELOS
import pytest


def test_crear_individuo():        
    individuo = crear_individuo(GENES, ALELOS)   
    assert len(individuo) == GENES
    for color in individuo:
        assert color in ALELOS        


