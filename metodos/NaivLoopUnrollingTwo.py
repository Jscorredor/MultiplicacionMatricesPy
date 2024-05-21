import numpy as np

class NaivLoopUnrollingTwo:
    def __init__(self):
        self.nombreMetodo = "NaivLoopUnrollingTwo"

    def algoritmo(self, matriz):
        return self.naiv_loop_unrolling_two(matriz)

    def naiv_loop_unrolling_two(self, matriz):
        N, P, M = len(matriz), len(matriz[0]), len(matriz)
        resultado = np.zeros((N, M))

        for i in range(N):
            for j in range(M):
                aux = 0.0
                if P % 2 == 0:
                    for k in range(0, P, 2):
                        aux += matriz[i][k] * matriz[k][j] + matriz[i][k + 1] * matriz[k + 1][j]
                else:
                    PP = P - 1
                    for k in range(0, PP, 2):
                        aux += matriz[i][k] * matriz[k][j] + matriz[i][k + 1] * matriz[k + 1][j]
                    aux += matriz[i][PP] * matriz[PP][j]

                resultado[i][j] = aux

        return resultado
