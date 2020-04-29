from BonusProblem import BonusProblem

import numpy as np
from numpy.linalg import norm

class ConjugateGradient(BonusProblem):
  def gradconj(self,x0,N,TOL):
      A = np.dot(self.A1.copy().T, self.A1.copy())
      b = np.dot(self.A1.copy().T, self.b1.copy())
      d0 = b - np.dot(A,x0)
      r0 = d0
      x1 = x0
      k=1
      while(k<N):
          a0 = np.dot(r0,r0) / np.dot(np.dot(d0,A),d0)
          x1 = x0 + np.dot(a0,d0)
          r1 = r0 - np.dot(np.dot(a0,A),d0)
          if(norm(r1) <= TOL):
              break
          b0 = np.dot(r1,r1) / np.dot(r0,r0)
          d1 = r1 + np.dot(b0,d0)
          x0, d0, r0 = x1, d1, r1
          k+=1
      return x1

#Use the code below to test it
test = ConjugateGradient()
print(test.gradconj(test.x1, 100, 0.00001))





