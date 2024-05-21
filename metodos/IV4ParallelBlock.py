import numpy as np
from concurrent.futures import ThreadPoolExecutor

class IV4ParallelBlock:
    def __init__(self):
        self.nombreMetodo = "IV4ParallelBlock"

    def algoritmo(self, matriz):
        return self.lV_4ParallelBlock(matriz)

    def lV_4ParallelBlock(self, matriz):
        size = len(matriz)
        bsize = int(np.sqrt(size))
        matrizResultado = np.zeros((size, size))

        def block_multiply(i1, j1, k1):
            for i in range(i1 * bsize, min((i1 + 1) * bsize, size)):
                for j in range(j1, min(j1 + bsize, size)):
                    for k in range(k1, min(k1 + bsize, size)):
                        matrizResultado[i][k] += matriz[i][j] * matriz[j][k]

        with ThreadPoolExecutor() as executor:
            futures = []
            for i1 in range(size // bsize):
                for j1 in range(0, size, bsize):
                    for k1 in range(0, size, bsize):
                        futures.append(executor.submit(block_multiply, i1, j1, k1))

            for future in futures:
                future.result()

        return matrizResultado

# Ejemplo de uso
if __name__ == "__main__":
    matriz = np.random.rand(4, 4)
    algoritmo = IV4ParallelBlock()
    resultado = algoritmo.algoritmo(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz resultado:")
    print(resultado)
