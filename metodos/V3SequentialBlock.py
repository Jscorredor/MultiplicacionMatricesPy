import math

class V3SequentialBlock:
    def v_3SequentialBlock(self, matrizA, matrizB, size):
        bsize = int(math.sqrt(size))
        matrizResultado = [[0.0 for _ in range(size)] for _ in range(size)]
        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]
        return matrizResultado
