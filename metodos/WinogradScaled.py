import numpy as np

class WinogradScaled(WinogradOriginal):
    def WinogradScaled(self, A, B, N, P, M):
        CopyA = np.zeros((N, P))
        CopyB = np.zeros((P, M))

        a = self.NormInf(A, N, P)
        b = self.NormInf(B, P, M)
        lambda_val = int(np.floor(0.5 + np.log(b/a)/np.log(4)))

        self.MultiplyWithScalar(A, CopyA, N, P, 2 ** lambda_val)
        self.MultiplyWithScalar(B, CopyB, P, M, 2 ** (-lambda_val))

        return self.WinogradOriginal(CopyA, CopyB, N, P, M)

    def MultiplyWithScalar(self, A, B, N, M, scalar):
        B[:] = A * scalar

    def NormInf(self, A, N, M):
        return np.max(np.sum(np.abs(A), axis=1))
