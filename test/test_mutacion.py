


from src.mastermind import mutacion, VALORES_POSIBLES, TASA_MUTACION
import pytest 




def test_mutacion():
    individuo = ['ROJO', 'AZUL', 'VERDE', 'AMARILLO']
    individuo_mutado = mutacion(individuo, VALORES_POSIBLES,TASA_MUTACION)
    
    assert len(individuo_mutado) == len(individuo)
    for color in individuo_mutado:
        assert color in VALORES_POSIBLES
    # Verificar que al menos un gen ha cambiado si la tasa de mutación es alta
    if TASA_MUTACION > 0.5:
        assert individuo != individuo_mutado
        