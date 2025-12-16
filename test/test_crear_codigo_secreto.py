


from src.mastermind import crear_codigo_secreto, GENES, VALORES_POSIBLES
import pytest


def test_crear_codigo_secreto():
    codigo_secreto = crear_codigo_secreto(GENES, VALORES_POSIBLES)
    assert len(codigo_secreto) == GENES
    for color in codigo_secreto:
        assert color in VALORES_POSIBLES


    
