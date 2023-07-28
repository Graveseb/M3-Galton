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
