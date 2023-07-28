# M3-Galton
Tarea de Ucamp

Este Programa me dio un reto mas grande personalmente
Tuve muchas dificultades con tan solo aprender y entender que necesitaba hacer ya que los demos 
incluyen “numpy” y “matplotlib” y por alguna razón yo no los podía instalar desde la terminal incluso 
estuve investigando otros métodos para su instalación, topandome con anaconda pero tampoco me generó resultados, 
llegó a cierto punto donde borre VS y lo volvi a instalar, modifique los “environments” y aun asi no me dejo, 
Al final lo logré al instalar otra función cuyo nombre no me acuerdo bien e instalando numpy con la función
especial en la terminal, pero terminando aun me topaba con el reto de entender que me pedía la tarea,
para empezar no tenía bien en claro la simulación de galton ya que la imagen de abajo no se parecía a lo que había
entendido pero asumi que solo era un ejemplo de que tipo de imagen se quería obtener como resultado ya que los ejemplos
dados mostraban cosas distintas, por otra parte no entendi muy bien los ejemplos dados, particularmente con la función
normal incluso llegó a cierto punto donde cambié mi codigo original porque creí que los estaba usando  pero eso me llevó a 
aprender como mejorar mi código hasta lograr algo de lo que me siento mas orgulloso, mi ultimo y unico pendiente 
es si el 0 cuenta como factor ya que la tarea pide 12 pero asumiendo que la imagen de referencia lo tenia y se reprentaba mejor
entre mas barras, agregue el cero y movi la grafica para representar -6 a 6 para ahorrarme el lio 




anexo el codigo aparte por si las dudas

#SEBASTIAN_GARCIA_proyectoM3.py
import numpy as np
import matplotlib.pyplot as plt

def simulacion_galton(num_canicas, num_niveles):
    resultados = np.zeros(num_niveles + 1, dtype=int)
    
    for _ in range(num_canicas):
        pos = num_niveles // 2  # Posición inicial en el centro del primer nivel
        for nivel in range(num_niveles):
            if np.random.rand() < 0.5:
                pos -= 1  # Caer hacia la izquierda
            else:
                pos += 1  # Caer hacia la derecha
            pos = np.clip(pos, 0, num_niveles)  # ASEGURAR pos sea valido
        
        resultados[pos] += 1  # Incrementar el contenedor correspondiente
    
    return resultados

def graficar_histograma(resultados):
    num_contenedores = len(resultados)
    contenedores = np.arange(0, num_contenedores) - num_contenedores // 2
    
    plt.bar(contenedores, resultados)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de Máquina de Galton')
    plt.show()

if __name__ == "__main__":
    num_canicas = 3000
    num_niveles = 12
    
    resultados = simulacion_galton(num_canicas, num_niveles)
    graficar_histograma(resultados)
