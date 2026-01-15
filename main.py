from src.crear_codigo_secreto import crear_codigo_secreto
from src.crear_poblacion import crear_poblacion 
from src.seleccionar_padres import seleccionar_padres
from src.cruzar_padres import cruzar_padres
from src.mutar_individuo import mutar_individuo
from src.evaluar_fitness import evaluar_fitness
from src.es_solucion import es_solucion

from src.constantes_mastermind import GENES, VALORES_POSIBLES, POBLACION, MAX_INTENTOS, TASA_MUTACION, EMOJIS

def convertir_a_emojis(codigo_secreto):
    return [EMOJIS[color] for color in codigo_secreto]


def main():
    # Crear el código secreto y la población inicial
    codigo_secreto = crear_codigo_secreto() 
    print("Código secreto generado:", convertir_a_emojis(codigo_secreto), "¡Comienza el juego!")


    # Crear población inicial
    poblacion = crear_poblacion(poblacion=POBLACION) 
    intentos = 0
    solucion_encontrada = False


    # Bucle principal del algoritmo genético
    while intentos < MAX_INTENTOS and not solucion_encontrada:
        intentos += 1
        print(f"\nIntento {intentos}:")

        
        #Seleccionar los mejores individuos como padres
        padres = seleccionar_padres(poblacion, codigo_secreto) 
          
        #Crear nueva población a partir de los padres
        nueva_poblacion = []
       
        for i in range(POBLACION):
             hijo = cruzar_padres(padres) 
             hijo = mutar_individuo(hijo)
             nueva_poblacion.append(hijo)
        
   
        poblacion = nueva_poblacion
        
        # Buscar el mejor individuo de la poblacion
        mejor_individuo = poblacion[0]
        mejor_fitness = evaluar_fitness(mejor_individuo, codigo_secreto)
       
       
        for individuo in poblacion[1:]:
            fitness_actual = evaluar_fitness(individuo, codigo_secreto)
            if fitness_actual > mejor_fitness:
                mejor_fitness = fitness_actual
                mejor_individuo = individuo
        print("individuo:", " ".join(convertir_a_emojis(mejor_individuo)), f"| Fitness: {mejor_fitness}")
      
        
        #Verificar si se ha encontrado la solución
        if es_solucion(mejor_individuo, codigo_secreto):
            solucion_encontrada = True
            print("\n¡Has encontrado el código secreto en:",
                  intentos, "intentos.")
            print("Mejor individuo:", " ".join(convertir_a_emojis(mejor_individuo)),
              f"| Fitness: {mejor_fitness}")
           
    
    if not solucion_encontrada:
        print("Se han agotado los intentos. El código secreto era:",
              " ".join(convertir_a_emojis(codigo_secreto)))
if __name__ == "__main__":
    main()