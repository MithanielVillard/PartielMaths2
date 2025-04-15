from __future__ import annotations

class Matrix:
     
    def __init__(self, size : int):
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size

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