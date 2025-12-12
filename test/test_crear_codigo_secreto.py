


from src.mastermind import crear_codigo_secreto, TAMANHO_GENES, VALORES_POSIBLES
import pytest


def test_crear_codigo_secreto():
    codigo = crear_codigo_secreto(TAMANHO_GENES, VALORES_POSIBLES)
    assert len(codigo) == TAMANHO_GENES
    for color in codigo:
        assert color in VALORES_POSIBLES





    
