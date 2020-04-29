import numpy as np
from BonusProblem import BonusProblem

class eigenvalues(BonusProblem):
    def eigen(self, x):
        x1, y1 = np.linalg.eig(self.B)
        x2, y2 = np.linalg.eig(self.B.T)
        if x == 1:
            print(x1)
        else:
            print(x2)


#Use the code below to test
#test = eigenvalues()
#test.eigen()

