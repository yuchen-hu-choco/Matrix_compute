import numpy as np
class p5():
    def iterate(self):
        a = np.array([[1., 2., 4., 8.], [1., 3., 9., 27.], [1., 4., 16., 64.], [1., 5., 25., 125.]])

        A = np.dot(a.T, a)

        b = np.dot(a.T,np.array([1, -1, 1, -1], dtype=float))

        x = np.array([0, 0, 0, 0], dtype=float)

        for i in range(80000000):
            x = x - 0.000092*(np.dot(A, x) - b)


        return x

test = p5()
print(test.iterate())
