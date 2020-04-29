import numpy as np
from BonusProblem import BonusProblem
from scipy.linalg import expm

class exponent(BonusProblem):
    def exponent(self):
        a=expm(self.B)
        return a

#use the code below to test
#test = exponent()
#print(test.exponent())