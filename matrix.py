class Matrix:
     
    def __init__(self):
        self.matrix = []

    def __getitem__(self, i: int) -> list[list[float]]:
        return self.matrix[i]
    
    def __str__(self):
        return str(self.matrix)
    
    def transpose(self) -> list[list[float]]:
        m = [[0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]

        for col in range(len(self.matrix)):  
            for row in range(len(self.matrix[col])):
                m[row][col] = self.matrix[col][row]
            
        return m
    
    def append(self, row : list[float]) -> list[list[float]]:
        self.matrix.append(row)
        return self.matrix