from src.genetico import (
    crear_codigo_secreto,
      crear_poblacion, 
      evaluar_fitness, 
      seleccionar_padres, 
      cruzar_padres, 
      mutar_individuo,
        es_solucion)
from src.constantes_mastermind import GENES, VALORES_POSIBLES, POBLACION, MAX_INTENTOS, TASA_MUTACION

def main():
    # Crear el código secreto y la población inicial
    codigo_secreto = crear_codigo_secreto() 
    print("Código secreto generado. ¡Comienza el juego!")
    
    poblacion = crear_poblacion(poblacion=POBLACION) 
    intentos = 0
    solucion_encontrada = False
    
    while intentos < MAX_INTENTOS and not solucion_encontrada:
        intentos += 1
        print(f"\nIntento {intentos}:")
        
        #Seleccionar padres
        padres = seleccionar_padres(poblacion, codigo_secreto) 
            #Cruzar y mutar para crear un nuevo individuo
        hijos= []
        for i in range(POBLACION):
             hijo = cruzar_padres(padres) 
             hijo = mutar_individuo(hijo)
             hijos.append(hijo)
        
       #Sustituir la población por el nuevo hijo
        poblacion = hijos
        
        #Evaluar el mejor individuo de la población
        mejor_individuo = poblacion[0]
        mejor_fitness = evaluar_fitness(mejor_individuo, codigo_secreto)
        for individuo in poblacion[1:]:
            fitness_actual = evaluar_fitness(individuo, codigo_secreto)
            if fitness_actual > mejor_fitness:
                mejor_fitness = fitness_actual
                mejor_individuo = individuo
          
        
        #Verificar si se ha encontrado la solución
        if es_solucion(mejor_individuo, codigo_secreto):
            solucion_encontrada = True
            print(f"¡Solución encontrada! Código secreto: {codigo_secreto}")
            break
    
    if not solucion_encontrada:
        print(f"Se han agotado los intentos. El código secreto era: {codigo_secreto}")

if __name__ == "__main__":
    main()