from src.mastermind import cruce, GENES, ALELOS
import pytest

def test_cruce():
    padre1 = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']
    padre2 = ['NARANJA', 'MORADO', 'AZUL', 'VERDE']
    hijo1, hijo2 = cruce(padre1, padre2)
    
    assert len(hijo1) == GENES
    assert len(hijo2) == GENES
    for color in hijo1:
        assert color in ALELOS
    for color in hijo2:
        assert color in ALELOS