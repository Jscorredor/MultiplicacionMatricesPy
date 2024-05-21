class StrassenNaiv:
    def __init__(self):
        self.nombreMetodo = "StrassenNaiv"

    def algoritmo(self, matriz):
        return self.strassen_naiv(matriz)

    def strassen_naiv(self, matriz):
        N, P, M = len(matriz), len(matriz[0]), len(matriz)
        resultado = [[0 for _ in range(M)] for _ in range(N)]

        MaxSize = max(N, P)
        if MaxSize < 16:
            MaxSize = 16
        k = int((MaxSize / 2 ** 4) - 1)
        m = int((MaxSize * (2 ** (-k))) + 1)
        NewSize = m * 2 ** k

        NewA = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        NewB = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        AuxResult = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

        for i in range(N):
            for j in range(P):
                NewA[i][j] = matriz[i][j]

        for i in range(P):
            for j in range(M):
                NewB[i][j] = matriz[i][j]

        self.strassen_naiv_step(NewA, NewB, AuxResult, NewSize, m)

        for i in range(N):
            for j in range(M):
                resultado[i][j] = AuxResult[i][j]

        return resultado

    def max(self, N, P):
        if N < P:
            return P
        else:
            return N

    def minus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] - B[i][j]

    def plus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] + B[i][j]

    def strassen_naiv_step(self, A, B, Result, N, m):
        if N % 2 == 0 and N > m:
            NewSize = N // 2

            A11 = [row[:NewSize] for row in A[:NewSize]]
            A12 = [row[NewSize:] for row in A[:NewSize]]
            A21 = [row[:NewSize] for row in A[NewSize:]]
            A22 = [row[NewSize:] for row in A[NewSize:]]
            B11 = [row[:NewSize] for row in B[:NewSize]]
            B12 = [row[NewSize:] for row in B[:NewSize]]
            B21 = [row[:NewSize] for row in B[NewSize:]]
            B22 = [row[NewSize:] for row in B[NewSize:]]

            ResultPart11 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            ResultPart12 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            ResultPart21 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            ResultPart22 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

            Helper1 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Helper2 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

            Aux1 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Aux2 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Aux3 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Aux4 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Aux5 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Aux6 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
            Aux7 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

            self.plus(A11, A22, Helper1, NewSize, NewSize)
            self.plus(B11, B22, Helper2, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, Helper2, Aux1, NewSize, m)

            self.plus(A21, A22, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, B11, Aux2, NewSize, m)

            self.minus(B12, B22, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(A11, Helper1, Aux3, NewSize, m)

            self.minus(B21, B11, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(A22, Helper1, Aux4, NewSize, m)

            self.plus(A11, A12, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, B22, Aux5, NewSize, m)

            self.minus(A21, A11, Helper1, NewSize, NewSize)
            self.plus(B11, B12, Helper2, NewSize, NewSize)
            self
