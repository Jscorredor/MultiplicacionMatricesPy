import numpy as np

class WinogradOriginal:
    def WinogradOriginal(self, A, B, N, P, M):
        upsilon = P % 2
        gamma = P - upsilon
        y = np.zeros(M)
        z = np.zeros(N)
        Result = np.zeros((M, N))

        for i in range(M):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += A[i][j] * A[i][j+1]
            y[i] = aux

        for i in range(N):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += B[j][i] * B[j+1][i]
            z[i] = aux

        if upsilon == 1:
            PP = P - 1
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j+1][k]) * (A[i][j+1] + B[j][k])
                    Result[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]
        else:
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j+1][k]) * (A[i][j+1] + B[j][k])
                    Result[i][k] = aux - y[i] - z[k]

        return Result
