import random 
TAMANHO_GENES = 4
VALORES_POSIBLES = ['AMARILLO', 'AZUL', 'ROJO', 'VERDE', 'NARANJA', 'MORADO']
TAMANHO_POBLACION = 100
TASA_MUTACION = 0.1 



def crear_codigo_secreto(tamanho_genes=TAMANHO_GENES, valores_posibles=VALORES_POSIBLES):
    codigo = []                                      # Creamos una lista vacia donde se van guardando los colores del código secreto
    for posicion in range(tamanho_genes):            # Repite el proceso las veces que indique tamaño_genes (en este caso, 4) La variable posicion tomarán los valores 0,1,2,3,4
        valor = random.choice(valores_posibles)      # Selecciona al azar uno de los elementos de valores_posibles, pudiendo repetirse colores **COMO NO REPETIR COLORES**
        codigo.append(valor)                         # Inserta el color elegido al final de la lista de codigo
    return codigo                                    # Devuelve 4 colores aleatorios


def crear_individuo(TAMANHO_GENES=TAMANHO_GENES, VALORES_POSIBLES=VALORES_POSIBLES):                            
    individuo = []                                  
    for posicion in range(TAMANHO_GENES):           
        valor = random.choice(VALORES_POSIBLES)
        individuo.append(valor)
    return individuo

# Uno crea el código secreto a adivinar y el otro crea un individuo de la población que intentará adivinarlo.

def crear_poblacion ():
    poblacion = []                                  # Creamos una lista vacia donde se van guardando los individuos
    for individuo in range(TAMANHO_POBLACION):      # Repite el proceso las veces que indique tamaño_poblacion (en este caso, 100)
        individuo = crear_individuo ()              # Crea un individuo llamando a la función crear_individuo
        poblacion.append(individuo)                 # Inserta el individuo creado al final de la lista de población
    return poblacion                                # Devuelve una lista con 100 individuos aleatorios     

 


def mutacion(individuo, valores_posibles, tasa_mutacion):
    individuo_mutado = individuo.copy()     # Creamos una copia del individuo original para no modificarlo directamente

    for i in range(len(individuo_mutado)): # Recorremos cada gen del individuo
        if random.random() < tasa_mutacion: #Compara ese número con tasa_mutacion. Si es menor, decidimos mutar el gen en la posición i.
            individuo_mutado[i] = random.choice(valores_posibles) # Si se muta, se asigna un nuevo valor aleatorio del conjunto de valores posibles
                                                                        #  tasa_mutacion = 0.1, hay 10% de probabilidad de mutar cada gen en cada llamada.
    return individuo_mutado                                                     # Devuelve el individuo mutado

def evaluar_fitness(individuo, codigo_secreto):
    aciertos = 0
    for i in range(len(individuo)):
        if individuo[i] == codigo_secreto[i]:
            aciertos += 1
    return aciertos



