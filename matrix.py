from __future__ import annotations

class Matrix:
    def __init__(self, data: list[list[float]]):
        self.matrix = data
        self.size = len(data)
    def __getitem__(self, i: int) -> list[float]:
        return self.matrix[i]
    
    def __str__(self):
        return str(self.matrix)
    
    def transpose(self) -> list[list[float]]:
        m = [[0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]

        for col in range(len(self.matrix)):  
            for row in range(len(self.matrix[col])):
                m[row][col] = self.matrix[col][row]
            
        return m

    def pop(self, i : int, j : int) -> Matrix:
        B = []
        for k in range(self.size):
            if k != i:
                C = []
                for l in range(self.size):
                    if l != j:
                        C.append(self.matrix[k][l])
                B.append(C)
        return B


def det(matrix : Matrix) -> float:
    j = 0
    d = 0
    if len(matrix.matrix) == 1:
        return matrix[0][0]
    else:
        for i in range(len(matrix.matrix)):
            d += (-1) ** (i + j) * matrix[i][j] * det(matrix.pop(i, j))
        return d
    

#Added----------------------------
def com(A):
    B = []
    n = len(A)
    for i in range(n):
        C = []
        for j in range(n):
            C.append((-1)**(i+j)* det(pop(A,i,j)))
        B.append(C)

    return B

def prodScalMat(A,k):
    n = len(A)
    B = []
    for i in range (n):
        C = []
        for j in range (n):
            C.append(A[i][j] * k)
        B.append(C)
    
    return B

def prodMatMat(A, B):
    C = []
    n1 = len(A[1])
    n2 = len(B[0])
    if n1[1] == n2[0]:
        for i in range(n1):
            D = []
            for j in range(n2):
                D.append(A[i][j] * B[j][i])
            C.append(D)

    return C

def inverse(A):
    return 1 / det(A)*transpose(com(A))

def printMatrix(X):
    for i in range(len(X)):
        for j in range(len(X[0])):
            print(result[j][i])

#Add Finished----------------------------