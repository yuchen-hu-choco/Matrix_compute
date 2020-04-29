from BonusProblem import BonusProblem
import numpy as np

class GaussianElimination(BonusProblem):
    def Elimination(self, A, b):
        ab = np.hstack((A, b))
        numRows = np.size(ab, 0)
        numColumns = np.size(ab, 1)
        #Make the down triangular of Ab matrix;
        for i in range(0, numRows):
            ab[i, :] = ab[i, :]/ab[i, i]
            if i!=numRows:
                for j in range(i+1, numRows):
                    ab[j, :] = ab[j, :] - ab[j, i]/ab[i, i]*ab[i, :]
        for z in range(1,numRows):
            i = numRows-z
            max = i
            k=0
            while k<max:
                ab[k, :] = ab[k, :] - ab[k, i]/ab[i,i]*ab[i, :]
                k = k+1
        return ab[:, 4]

#to test, add the code below
#test = GaussianElimination()
#print(test.Elimination(test.A, test.b))