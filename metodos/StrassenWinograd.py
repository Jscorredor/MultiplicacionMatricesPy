class StrassenWinograd(NaivStandar):
    def max(self, N, P):
        if N < P:
            return P
        else:
            return N

    def StrassenWinograd(self, matrizA, matrizB, matrizC, N, P, M):
        MaxSize = self.max(N, P)
        MaxSize = self.max(MaxSize, M)
        if MaxSize < 16:
            MaxSize = 16  # de lo contrario no es posible calcular k
        k = int((math.log(MaxSize) / math.log(2)) - 4)
        m = int((MaxSize * (2 ** -k)) + 1)
        NewSize = m * (2 ** k)

        # agregar filas y columnas de cero para usar el algoritmo de Strassens
        NewA = [[0.0] * NewSize for _ in range(NewSize)]
        NewB = [[0.0] * NewSize for _ in range(NewSize)]
        AuxResult = [[0.0] * NewSize for _ in range(NewSize)]

        for i in range(N):
            for j in range(P):
                NewA[i][j] = matrizA[i][j]

        for i in range(P):
            for j in range(M):
                NewB[i][j] = matrizB[i][j]

        self.StrassenWinogradStep(NewA, NewB, AuxResult, NewSize, m)

        # extraer el resultado
        for i in range(N):
            for j in range(M):
                matrizC[i][j] = AuxResult[i][j]

    def Minus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] - B[i][j]

    def Plus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] + B[i][j]

    def StrassenWinogradStep(self, A, B, Result, N, m):
        if N % 2 == 0 and N > m:
            NewSize = N // 2

            A1 = [row[:NewSize] for row in A[:NewSize]]
            A2 = [row[:NewSize] for row in A[NewSize:]]
            B1 = [row[:NewSize] for row in B[:NewSize]]
            B2 = [row[:NewSize] for row in B[NewSize:]]

            A11 = [row[:NewSize] for row in A1]
            A12 = [row[NewSize:] for row in A1]
            A21 = [row[:NewSize] for row in A2]
            A22 = [row[NewSize:] for row in A2]
            B11 = [row[:NewSize] for row in B1]
            B12 = [row[NewSize:] for row in B1]
            B21 = [row[:NewSize] for row in B2]
            B22 = [row[NewSize:] for row in B2]

            ResultPart11 = [[0.0] * NewSize for _ in range(NewSize)]
            ResultPart12 = [[0.0] * NewSize for _ in range(NewSize)]
            ResultPart21 = [[0.0] * NewSize for _ in range(NewSize)]
            ResultPart22 = [[0.0] * NewSize for _ in range(NewSize)]

            Helper1 = [[0.0] * NewSize for _ in range(NewSize)]
            Helper2 = [[0.0] * NewSize for _ in range(NewSize)]

            Aux1 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux2 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux3 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux4 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux5 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux6 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux7 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux8 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux9 = [[0.0] * NewSize for _ in range(NewSize)]

            self.Minus(A11, A21, A1, NewSize, NewSize)
            self.Minus(A22, A1, A2, NewSize, NewSize)
            self.Minus(B22, B12, B1, NewSize, NewSize)
            self.Plus(B1, B11, B2, NewSize, NewSize)

            self.StrassenWinogradStep(A11, B11, Aux1, NewSize, m)
            self.StrassenWinogradStep(A12, B21, Aux2, NewSize, m)
            self.StrassenWinogradStep(A2, B2, Aux3, NewSize, m)
            self.Plus(A21, A22, Helper1, NewSize, NewSize)
            self.Minus(B12, B11, Helper2, NewSize, NewSize)
            self.Str
