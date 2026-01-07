from src.genetico import es_solucion
import pytest

def test_es_solucion_true():
    # Individuo igual al código secreto debe retornar True
    codigo_secreto = ["ROJO", "AZUL", "VERDE", "AMARILLO"]
    individuo = ["ROJO", "AZUL", "VERDE", "AMARILLO"]
    assert es_solucion(individuo, codigo_secreto) == True

def test_es_solucion_false():
    # Individuo diferente al código secreto debe retornar False
    codigo_secreto = ["ROJO", "AZUL", "VERDE", "AMARILLO"]
    individuo = ["ROJO", "AZUL", "AMARILLO", "VERDE"]
    assert es_solucion(individuo, codigo_secreto) == False




