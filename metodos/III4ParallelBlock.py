import numpy as np
from concurrent.futures import ThreadPoolExecutor

class III4ParallelBlock:
    def __init__(self):
        self.nombreMetodo = "III4ParallelBlock"

    def algoritmo(self, matriz):
        return self.lll_4ParallelBlock(matriz)

    def lll_4ParallelBlock(self, matriz):
        size = len(matriz)
        bsize = int(np.sqrt(size))
        matrizResultado = np.zeros((size, size))

        def block_multiply(i1, j1, k1):
            for i in range(i1, min(i1 + bsize, size)):
                for j in range(j1, min(j1 + bsize, size)):
                    for k in range(k1, min(k1 + bsize, size)):
                        matrizResultado[i][j] += matriz[i][k] * matriz[k][j]

        with ThreadPoolExecutor() as executor:
            futures = []
            for i1 in range(0, size, bsize):
                for j1 in range(0, size, bsize):
                    for k1 in range(0, size, bsize):
                        futures.append(executor.submit(block_multiply, i1, j1, k1))

            for future in futures:
                future.result()

        return matrizResultado

# Ejemplo de uso
if __name__ == "__main__":
    matriz = np.random.rand(4, 4)
    algoritmo = III4ParallelBlock()
    resultado = algoritmo.algoritmo(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz resultado:")
    print(resultado)
