import numpy as np
from BonusProblem import BonusProblem

class QrFactorization(BonusProblem):
    def qr(self):
        A = self.B
        m, n = A.shape
        Q = np.zeros((m, n))
        R = np.zeros((n, n))
        A=np.transpose(A)
        R[0][0]=np.linalg.norm(A[0], 2)
        Q[:,0]=A[0]/R[0][0]
        for i in range(1,n):
            Q[:,i]=A[i]
            for j in range(0,i):
                R[j][i]=np.matmul(Q[:,j], Q[:,i])
                Q[:,i]=Q[:,i]-(R[j][i] * Q[:,j])
            R[i][i]=np.linalg.norm(Q[:,i], 2)
            Q[:,i]=Q[:,i]/R[i][i]
        return Q, R

#Use the code below to test
#test = QrFactorization()
#q, r = test.qr()
#print('Q:\n', q)
#print('R:\n', r)