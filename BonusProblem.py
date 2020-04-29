import numpy as np

class BonusProblem:
    def __init__(self):
        self.A = np.mat([[1, 2, 4, 8],[1, 3, 9, 27],[1, 4, 16, 64],[1, 5, 25, 125]], dtype=float)
        self.A1 = np.array([[1, 2, 4, 8],[1, 3, 9, 27],[1, 4, 16, 64],[1, 5, 25, 125]], dtype=float)
        self.b = np.mat([[1],[-1],[1],[-1]], dtype=float)
        self.b1 = np.array([1,-1,1,-1], dtype=float)
        self.x01 = np.mat([[0],[0],[0],[0]], dtype=float)
        self.x1 = np.array([0, 0, 0, 0], dtype=float)
        self.x02 = np.mat([[1],[1],[1],[1]], dtype=float)
        self.x2 = np.array(np.array([1, 1, 1, 1], dtype=float))

        self.B = np.dot(np.array([[1, 2, 4, 8],[1, 3, 9, 27],[1, 4, 16, 64],[1, 5, 25, 125]], dtype=float)\
                        , np.linalg.inv(np.array([[4, 0, 0, 0],[0, 14, 0, 0], [0, 0, 54, 0],[0, 0, 0, 224]]))
                        )