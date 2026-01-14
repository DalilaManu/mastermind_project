from src.mutar_individuo import mutar_individuo
from src.crear_individuo import crear_individuo
from src.constantes_mastermind import TASA_MUTACION, POBLACION, VALORES_POSIBLES
import pytest

def test_mutar_individuo():
    # Crear población de 20 individuos
    poblacion = [crear_individuo(4, VALORES_POSIBLES) for _ in range(POBLACION)]
    
    # Mutar cada individuo múltiples veces para garantizar mutaciones con tasa del 1%
    mutaciones_encontradas = False
    for _ in range(50):  # 50 intentos para aumentar probabilidad
        poblacion_mutada = [mutar_individuo(ind.copy(), TASA_MUTACION, VALORES_POSIBLES) for ind in poblacion]
        
        # Verificar que todos los genes están en VALORES_POSIBLES
        for individuo in poblacion_mutada:
            for gen in individuo:
                assert gen in VALORES_POSIBLES
        
        # Verificar si al menos un individuo fue mutado
        for ind_original, ind_mutado in zip(poblacion, poblacion_mutada):
            if ind_original != ind_mutado:
                mutaciones_encontradas = True
                break
        
        if mutaciones_encontradas:
            break
    
    assert mutaciones_encontradas, "Debería haber mutaciones en la población"   
