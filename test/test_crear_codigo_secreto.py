


from src.mastermind import crear_codigo_secreto, GENES, ALELOS
import pytest


def test_crear_codigo_secreto():
    codigo = crear_codigo_secreto(GENES, ALELOS)
    assert len(codigo) == GENES
    for color in codigo:
        assert color in ALELOS





    
