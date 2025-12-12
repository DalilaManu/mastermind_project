


from src.mastermind import crear_individuo, TAMANHO_GENES, VALORES_POSIBLES
import pytest


def test_crear_individuo():        
    individuo = crear_individuo(TAMANHO_GENES, VALORES_POSIBLES)   
    assert len(individuo) == TAMANHO_GENES
    for color in individuo:
        assert color in VALORES_POSIBLES        
