import os
import time

class TiempoEjecucion:
    def __init__(self, nombreMetodo):
        self.nombreMetodo = nombreMetodo

    def ejecutar(self, matriz):
        tiempoInicio = time.time_ns()
        matrizResultante = self.algoritmo(matriz)
        tiempoFinal = time.time_ns()
        tiempoEjecucion = tiempoFinal - tiempoInicio
        self.escribirArchivo(matrizResultante)
        guardarTiempo(self.nombreMetodo, tiempoEjecucion, f"{len(matriz)}x{len(matriz)}")

    def escribirArchivo(self, matriz):
        filename = f"{self.nombreMetodo}{len(matriz)}x{len(matriz)}.txt"
        carpetaResultado = "resultados"
        carpetaMetodo = os.path.join("resultados", self.nombreMetodo)
        os.makedirs(carpetaResultado, exist_ok=True)
        os.makedirs(carpetaMetodo, exist_ok=True)
        try:
            with open(os.path.join(carpetaMetodo, filename), "w") as writer:
                for fila in matriz:
                    writer.write("\t".join(map(str, fila)) + "\n")
        except IOError as e:
            print(f"Error al crear el archivo: {e}")

    def algoritmo(self, matriz):
        pass  # Este método debe ser implementado en las subclases
