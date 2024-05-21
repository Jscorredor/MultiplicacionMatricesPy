class NaivStandar:
    def NaivStandard(self, matrizA, matrizB, matrizC, N, P, M):
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(P):
                    aux += matrizA[i][k] * matrizB[k][j]
                matrizC[i][j] = aux
