from BonusProblem import BonusProblem
import numpy as np


def diagonal(c):

    for i in range(0, np.size(c, 0)):
        for j in range(0, np.size(c, 1)):
            if i != j:
                c.itemset((i, j), 0)
            else:
                continue
    return c


def upperTriangle(d):
    for i in range(0, np.size(d, 0)):
        for j in range(0, np.size(d, 1)):
            if i >= j:
                d.itemset((i, j), 0)
    return d

def leftTriangle(d):
    for i in range(0, np.size(d, 0)):
        for j in range(0, np.size(d, 1)):
            if i <= j:
                d.itemset((i, j), 0)
    return d

class JacobiIteration(BonusProblem):

    def jacobi(self, x, n):
        D = diagonal(self.A.copy())
        T = -upperTriangle(self.A.copy()) - leftTriangle(self.A.copy())
        D1 = np.linalg.inv(D)
        B = D1*T
        #add print(B) to check if it converges
        count = 0
        while count < n:
            x = B*x + D1*self.b
            count = count+1
        return x

#to test, add the code below
#test = JacobiIteration()
#print(test.jacobi(test.x01.copy(), 100))




