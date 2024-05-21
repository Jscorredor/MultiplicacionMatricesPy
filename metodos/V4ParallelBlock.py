import math
import numpy as np
import multiprocessing

class V4ParallelBlock:
    def v_4ParallelBlock(self, matrizA, matrizB, size):
        bsize = int(math.sqrt(size))
        matrizResultado = np.zeros((size, size))
        num_cores = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(num_cores)
        tasks = [(matrizA, matrizB, size, bsize, i) for i in range(num_cores)]
        pool.starmap(self.compute_partial_result, tasks)
        pool.close()
        pool.join()
        return matrizResultado

    def compute_partial_result(self, matrizA, matrizB, size, bsize, core_idx):
        for i1 in range(core_idx, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]
