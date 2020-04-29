import numpy as np
from BonusProblem import BonusProblem

class determinant(BonusProblem):
    def det(self):
        x = np.linalg.det(self.B)
        #print(self.B)
        print(x)

#use the code below to test
#test = determinant()
#print(test.det())