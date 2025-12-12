# mastermind_project

Juego de Mastermind


El Mastermind es un juego de habilidad y lógica para dos jugadores, en el que uno crea un código secreto de colores y el otro intenta descifrarlo en el menor número de intentos posibles.

**Objetivo del Juego**

El objetivo es ser el jugador que consiga adivinar el código secreto de su oponente en el menor número de jugadas a lo largo de una serie de partidas. 

**Componentes**

El juego incluye:
- Un tablero de juego con orificios grandes para las clavijas de código y orificios pequeños para las clavijas de pista.
- Clavijas de código grandes de varios colores, se puede elegir 6 o 8 pero en este caso decidimos 6 colores.
- Clavijas de pista pequeñas, en este caso negras y blancas.
- Un escudo para ocultar el código secreto. 

**Cómo se Juega**

La partida se desarrolla en turnos alternos y los jugadores asumen los roles de "Creador del Código" (Codemaker) y "Descifrador del Código" (Codebreaker). 

Creación del Código: El Creador del Código elige una combinación secreta de cuatro clavijas de colores y la oculta tras el escudo. Se pueden repetir colores si se desea.

Intentos del Descifrador: El Descifrador del Código realiza su primer intento colocando una fila de cuatro clavijas de colores en el tablero.
Pistas del Creador del Código: Tras cada intento, el Creador del Código proporciona pistas utilizando las clavijas pequeñas:
Coloca una clavija negra (o del color equivalente) por cada color que sea correcto y esté en la posición correcta.
Coloca una clavija blanca (o del color equivalente) por cada color que sea correcto pero esté en la posición incorrecta.
No coloca clavija si el color no está en el código secreto.

Importante: El orden de las clavijas de pista no indica qué colores específicos son correctos, solo la cantidad de aciertos.

Deducción y Nuevos Intentos: El Descifrador utiliza estas pistas para deducir el código y realiza un nuevo intento en la siguiente fila.
Fin de la Partida: El juego continúa hasta que el Descifrador acierta el código exacto (indicado por cuatro clavijas negras) o se queda sin intentos. 


