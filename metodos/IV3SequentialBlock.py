import numpy as np

class IV3SequentialBlock:
    def __init__(self):
        self.nombreMetodo = "IV3SequentialBlock"

    def algoritmo(self, matriz):
        return self.lV_3SequentialBlock(matriz)

    def lV_3SequentialBlock(self, matriz):
        size = len(matriz)
        bsize = int(np.sqrt(size))
        matrizResultado = np.zeros((size, size))

        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizResultado[i][k] += matriz[i][j] * matriz[j][k]

        return matrizResultado

# Ejemplo de uso
if __name__ == "__main__":
    matriz = np.random.rand(4, 4)
    algoritmo = IV3SequentialBlock()
    resultado = algoritmo.algoritmo(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz resultado:")
    print(resultado)
