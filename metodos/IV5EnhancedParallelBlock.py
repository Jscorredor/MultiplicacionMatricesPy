import numpy as np
from concurrent.futures import ThreadPoolExecutor

class IV5EnhancedParallelBlock:
    def __init__(self):
        self.nombreMetodo = "IV5EnhancedParallelBlock"

    def algoritmo(self, matriz):
        return self.alg_IV_5_Enhanced_Parallel_Block(matriz)

    @staticmethod
    def alg_IV_5_Enhanced_Parallel_Block(matriz):
        size = len(matriz)
        matrizRes = np.zeros((size, size))

        def block_multiply(i1, j1, k1):
            for i in range(i1, min(i1 + size, size)):
                for j in range(j1, min(j1 + size, size)):
                    for k in range(k1, min(k1 + size, size)):
                        matrizRes[i][j] += matriz[i][k] * matriz[k][j]

        with ThreadPoolExecutor() as executor:
            futures = []
            for i1 in range(0, size // 2, size):
                for j1 in range(0, size, size):
                    for k1 in range(0, size, size):
                        futures.append(executor.submit(block_multiply, i1, j1, k1))

            for future in futures:
                future.result()

        return matrizRes

# Ejemplo de uso
if __name__ == "__main__":
    matriz = np.random.rand(4, 4)
    algoritmo = IV5EnhancedParallelBlock()
    resultado = algoritmo.algoritmo(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz resultado:")
    print(resultado)
