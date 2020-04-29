from jacobi import *
import numpy as np

class GaussSeidelIteration(JacobiIteration):
    def gaussSeidel(self, x, n):
        D = diagonal(self.A.copy())
        L = leftTriangle(self.A.copy())
        U = upperTriangle(self.A.copy())
        B = np.linalg.inv(D + L)*(-U)
        #add print(B) to check if it converges
        count = 0
        while count < n:
            x = B*x + np.linalg.inv(D+L)*self.b
            count = count+1
        return x

#to test, add the code below
#test = GaussSeidelIteration()
#print(test.gaussSeidel(test.x01.copy(), 1000))

