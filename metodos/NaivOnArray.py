import numpy as np

class NaivOnArray:
    def __init__(self):
        self.nombreMetodo = "NaivOnArray"

    def algoritmo(self, matriz):
        return self.naiv_on_array(matriz)

    def naiv_on_array(self, matriz):
        N = len(matriz)
        resultado = np.zeros((N, N))

        for i in range(N):
            for j in range(N):
                resultado[i][j] = 0.0
                for k in range(N):
                    resultado[i][j] += matriz[i][k] * matriz[k][j]

        return resultado
