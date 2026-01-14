from src.cruzar_padres import cruzar_padres
import pytest

def test_cruzar_padres():
    padres = [
        ['R', 'G', 'B', 'Y'],
        ['Y', 'B', 'G', 'R']
    ]
    hijo = cruzar_padres(padres, genes=4)
    assert len(hijo) == 4
    # Verificar que el hijo contiene genes de ambos padres
    assert all(gene in ['R', 'G', 'B', 'Y'] for gene in hijo)
