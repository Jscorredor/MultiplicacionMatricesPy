import numpy as np

class NaivLoopUnrollingFour:
    def __init__(self):
        self.nombreMetodo = "NaivLoopUnrollingFour"

    def algoritmo(self, matriz):
        return self.naiv_loop_unrolling_four(matriz)

    def naiv_loop_unrolling_four(self, matriz):
        N, P, M = len(matriz), len(matriz[0]), len(matriz)
        resultado = np.zeros((N, M))

        for i in range(N):
            for j in range(M):
                aux = 0.0
                if P % 4 == 0:
                    for k in range(0, P, 4):
                        aux += matriz[i][k] * matriz[k][j] + matriz[i][k + 1] * matriz[k + 1][j] + \
                               matriz[i][k + 2] * matriz[k + 2][j] + matriz[i][k + 3] * matriz[k + 3][j]
                elif P % 4 == 1:
                    PP = P - 1
                    for k in range(0, PP, 4):
                        aux += matriz[i][k] * matriz[k][j] + matriz[i][k + 1] * matriz[k + 1][j] + \
                               matriz[i][k + 2] * matriz[k + 2][j] + matriz[i][k + 3] * matriz[k + 3][j]
                    aux += matriz[i][PP] * matriz[PP][j]
                elif P % 4 == 2:
                    PP = P - 2
                    PPP = P - 1
                    for k in range(0, PP, 4):
                        aux += matriz[i][k] * matriz[k][j] + matriz[i][k + 1] * matriz[k + 1][j] + \
                               matriz[i][k + 2] * matriz[k + 2][j] + matriz[i][k + 3] * matriz[k + 3][j]
                    aux += matriz[i][PP] * matriz[PP][j] + matriz[i][PPP] * matriz[PPP][j]
                else:
                    PP = P - 3
                    PPP = P - 2
                    PPPP = P - 1
                    for k in range(0, PP, 4):
                        aux += matriz[i][k] * matriz[k][j] + matriz[i][k + 1] * matriz[k + 1][j] + \
                               matriz[i][k + 2] * matriz[k + 2][j] + matriz[i][k + 3] * matriz[k + 3][j]
                    aux += matriz[i][PP] * matriz[PP][j] + matriz[i][PPP] * matriz[PPP][j] + \
                           matriz[i][PPPP] * matriz[PPPP][j]

                resultado[i][j] = aux

        return resultado

    @staticmethod
    def Abs(a):
        if a < 0:
            return -a
        return a

    @staticmethod
    def Max(x, y):
        if x < y:
            return y
        else:
            return x

    @staticmethod
    def NormInf(A, N, P):
        Norm = 0.0
        for i in range(N):
            aux = 0.0
            for j in range(P):
                aux += abs(A[i][j])
            Norm = NaivLoopUnrollingFour.Max(Norm, aux)
        return Norm
