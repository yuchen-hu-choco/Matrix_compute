import numpy as np
from BonusProblem import BonusProblem

class SingularValueDecomposition(BonusProblem):

    def svd(self):
        u, s, v = np.linalg.svd(self.B)
        print('u = ',u)
        print('s = ',s)
        print('v = ',v)

#Use the code below to test
#test = SingularValueDecomposition()
#test.svd()
