from eigenvalues import *
from GaussianElimination import *
from jacobi import *
from GaussSeidel import *
from ConjugateGradient import *
from q5 import *
from determinant import *
from exponent import *
from QRfactorization import *
from SingularValueDecomposition import *
from CholeskyFactorization import *
'''This is the EE510 homework, finished by Yuchen Hu
April, 2020'''

print('Problem 1')
print('==============================\n')
print('The result of Gaussian Elimination:')
test = GaussianElimination()
print(test.Elimination(test.A, test.b))
print('\nThe result of Jacobi iteration with x01 is:')
test = JacobiIteration()
print(test.jacobi(test.x01.copy(), 1000))
print('The result of Jacobi iteration with x02 is:')
test = JacobiIteration()
print(test.jacobi(test.x02.copy(), 1000))
print('\nThe result of Gauss-Seidel iteration with x01 is:')
test = GaussSeidelIteration()
print(test.gaussSeidel(test.x01.copy(), 1000))
print('The result of Gauss-Seidel iteration with x02 is:')
test = GaussSeidelIteration()
print(test.gaussSeidel(test.x02.copy(), 1000))
print('\nThe result of Conjugate Gradient iteration is:')
test = ConjugateGradient()
print(test.gradconj(test.x1, 100, 0.00001))
print('\nThe result of question 5 (coefficient = -0.000092, iterate 80000000 times):')
test = p5()
print(test.iterate())
print('\nProblem 2')
print('==============================\n')
print('The eigen value of B is:')
test = eigenvalues()
test.eigen(1)
print('The eigen value of B transpose is:')
test.eigen(2)
print('\nThe determinant of B is:')
test = determinant()
print(test.det())
print('\nThe exponential matrix of B is:')
test = exponent()
print(test.exponent())
print('\nThe QR factorization of B is:')
test = QrFactorization()
q, r = test.qr()
print('Q:\n', q)
print('R:\n', r)
print('\nSVD of B:')
test = SingularValueDecomposition()
test.svd()
print('\nCholesky Factorization of B\'B')
test = CholeskyFactorization()
test.cholesky(1)
print('Cholesky Factorization of BB\':')
test.cholesky(2)
