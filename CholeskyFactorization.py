import numpy as np
from BonusProblem import BonusProblem

class CholeskyFactorization(BonusProblem):

    def cholesky(self, x):
        BB1 = np.dot(self.B, self.B.T)
        B1B = np.dot(self.B.T, self.B)
        B1BC = np.linalg.cholesky(B1B)
        BB1C = np.linalg.cholesky(BB1)
        if x == 1:
            print(B1BC)
        else:
            print(BB1C)


#Use the code below to test
#test = CholeskyFactorization()
#test.cholesky(1)
