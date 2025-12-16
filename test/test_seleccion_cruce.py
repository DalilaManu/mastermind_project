from src.mastermind import cruce, TAMANHO_GENES, VALORES_POSIBLES
import pytest

def test_cruce():
    padre1 = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']
    padre2 = ['NARANJA', 'MORADO', 'AZUL', 'VERDE']
    hijo1, hijo2 = cruce(padre1, padre2)
    
    assert len(hijo1) == TAMANHO_GENES
    assert len(hijo2) == TAMANHO_GENES
    for color in hijo1:
        assert color in VALORES_POSIBLES
    for color in hijo2:
        assert color in VALORES_POSIBLES