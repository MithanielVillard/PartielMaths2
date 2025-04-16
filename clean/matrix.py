from __future__ import annotations
from maths import cos, sin


class Matrix:
    def __init__( self, table: list[ list[ float ] ] ):
        self.table: list[ list[ float ] ] = table
        self.rows: int = len( table )
        self.cols: int = len( table[0] )
    
    def copy( self ) -> Matrix: return Matrix( [ [ value for value in row ] for row in self.table ] )
    

    # Default Static Matrices (Null & Identity)

    @staticmethod
    def null( rows: int, cols: int ) -> Matrix: return Matrix( [ [ 0.0 for _ in range( cols ) ] for _ in range( rows ) ] )
    
    @staticmethod
    def identity( size: int ) -> Matrix:
        output: Matrix = Matrix( [ [ 0.0 for _ in range( size ) ] for _ in range( size ) ] )
        for index in range( size ):
            output[index][index] = 1
        return output
    

    # More Complex Static Matrices (Rotation & Translation)

    @staticmethod # TODO Check this method
    def rotation3( angle: float, unitVector: Vector,  ) -> Matrix:
        cosAngle: float = cos( angle )
        sinAngle: float = sin( angle )
        
        u1: Vector = unitVector / unitVector.norm()
        
        u2: Vector = Vector.null( 3 )
        for i in range( 3 ):
            if ( u1[i] != 0 ): u2[i] = 0
            else: u2[i] = 1
        
        u3: Vector = u1.cross( u2 )
        
        P_B1_B2: Matrix = Matrix.null( 3, 3 )
        for iIndex in range( 3 ):
            P_B1_B2[ iIndex ][ 0 ] = u1[ iIndex ]
            P_B1_B2[ iIndex ][ 1 ] = u2[ iIndex ]
            P_B1_B2[ iIndex ][ 2 ] = u3[ iIndex ]
        
        P_B2_B1 = P_B1_B2 ** (-1)
        Mx = Matrix([
            [ 1,        0,         0 ],
            [ 0, cosAngle, -sinAngle ],
            [ 0, sinAngle,  cosAngle ],
        ])
        return P_B1_B2 * Mx * P_B2_B1

    @staticmethod
    def rotation3Bis( angles: Vector ) -> Matrix:
        x : Matrix = Matrix.rotation3( angles.x(), Vector.right(3) )
        y : Matrix = Matrix.rotation3( angles.y(), Vector.up(3) )
        z : Matrix = Matrix.rotation3( angles.z(), Vector.forward(3) )
        return x * y * z
    

    # Testers
    
    def is_square( self ) -> bool: return self.rows == self.cols

    def is_symetric( self ) -> bool:
        if ( self.rows != self.cols ): raise ValueError
        for i in range( self.rows ):
            for j in range( self.cols ):
                if ( self[i][j] != self[j][i] ):
                    return False
        return True
    
    def is_orthogonal( self ) -> bool:
        if ( self.rows != self.cols ): raise ValueError
        
        output: Matrix = self.rotateRight()
        vectors: list[ Vector ] = [ 0 for _ in range( output.cols ) ]
        for j in range( output.cols ):
            vectors[ j ] = Vector( output[ j ] )
            if ( round( vectors[ j ].norm(), 10 ) != 1 ): return False
        
        iLenVectors: int = len( vectors )
        for iVectorIndex in range( iLenVectors ):
            for iNextVectorIndex in range( iVectorIndex + 1, iLenVectors ):
                if ( vectors[ iVectorIndex ] * vectors[ iNextVectorIndex ] != 0 ): return False
        
        return True
    
    
    # Math methods
    
    def determinant( self ) -> float: # Déterminant
        if ( self.rows != self.cols ): raise ValueError
        if ( self.rows == 2 ): return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        
        output: float = 0
        for i in range( self.rows ):
            smaller: Matrix = self.remove( i, 0 )
            output += (-1)**i * smaller.determinant() * self[i][0]
        return output
    
    def minor( self ) -> Matrix: # Comatrice
        if ( self.rows != self.cols ): raise ValueError
        return Matrix( [ [ (-1)**( i + j ) * self.remove( i, j ).determinant() for j in range( self.cols ) ] for i in range( self.rows ) ] )
    
    def transpose( self ) -> Matrix: return Matrix( [ [ self[i][j] for i in range( self.rows ) ] for j in range( self.cols ) ] )

    def inverse( self ) -> Matrix:
        determinant: float = self.determinant()
        if ( determinant == 0 ): raise ValueError
        return self.minor().transpose() / determinant
    

    # Getter & Setter
    
    def __getitem__( self, rowIndex: int ) -> list[ float ]: return self.table[rowIndex]
    def __setitem__( self, rowIndex: int, values: list[ float ] ) -> None: self.table[rowIndex] = values
    

    # Arithmetic magic methods
    
    def __add__( self, other: Matrix ) -> Matrix:
        if ( self.rows != other.rows or self.cols != other.cols ): raise ValueError
        return Matrix( [ [ self[i][j] + other[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ] )
    
    def __sub__( self, other: Matrix ) -> Matrix:
        if ( self.rows != other.rows or self.cols != other.cols ): raise ValueError
        return Matrix( [ [ self[i][j] - other[i][j] for j in range( self.cols ) ] for i in range( self.rows ) ] )
    
    def __mul__( self, other: Matrix | Vector | float ) -> Matrix | Vector: return self.__mul__Matrix( other ) if isinstance( other, Matrix ) else self.__mul__Vector( other ) if isinstance( other, Vector ) else self.__mul__float( other )
    
    def __mul__Matrix( self, other: Matrix ) -> Matrix:
        if ( self.cols != other.rows ): raise ValueError
        output: Matrix = Matrix.null( self.rows, other.cols )
        for i in range( output.rows ):
            for j in range( output.cols ):
                for k in range( self.cols ):
                    output[i][j] += self[i][k] * other[k][j]
        return output
    
    def __mul__Vector( self, other: Vector ) -> Vector:
        if ( not ( self.rows == other.size == self.cols ) ): raise ValueError
        output: Vector = Vector.null( other.size )
        for i in range( output.size ):
            for j in range( self.cols ):
                output[i] += self[i][j] * other[j]
        return output
    
    def __mul__float( self, scalar: float ) -> Matrix: return Matrix( [ [ value * scalar for value in row ] for row in self.table ] )
    
    def __truediv__( self, scalar: float ) -> Matrix: return Matrix( [ [ value / scalar for value in row ] for row in self.table ] )
    
    def __floordiv__( self, scalar: float ) -> Matrix: return Matrix( [ [ value // scalar for value in row ] for row in self.table ] )
    
    def __pow__( self, value: int ) -> Matrix:
        if ( self.rows != self.cols ): raise ValueError
        if ( value < -1 ): raise ValueError
        
        if ( value == -1 ):
            det: float = self.determinant()
            if ( det == 0 ): raise ValueError
            return self.minor().transpose() / det
        
        output: Matrix = Matrix.identity( 3 )
        for _ in range( value ):
            output *= self
        return output
    
    def __neg__( self ) -> Matrix: return Matrix( [ [ -value for value in row ] for row in self.table ] )


    # Assignment magic methods

    def __iadd__( self, other: Matrix ) -> Matrix:
        for i in range( self.rows ):
            for j in range( self.cols ):
                self[i][j] += other[i][j]
        return self
    
    def __isub__( self, other: Matrix ) -> Matrix:
        for i in range( self.rows ):
            for j in range( self.cols ):
                self[i][j] -= other[i][j]
        return self
    
    def __imul__( self, other: Matrix | float ) -> Matrix: return self.__imul__Matrix( other ) if isinstance( other, Matrix ) else self.__imul__float( other )
    
    def __imul__Matrix( self, other: Matrix ) -> Matrix:
        copy: Matrix = self.copy()
        for i in range( self.rows ):
            for j in range( self.cols ):
                self[i][j] = 0.0
                for k in range( self.cols ):
                    self[i][j] += copy[i][k] * other[k][j]
        return self
    
    def __imul__float( self, scalar: float ) -> Matrix:
        for i in range( self.rows ):
            for j in range( self.cols ):
                self[i][j] *= scalar
        return self
    
    def __itruediv__( self, scalar: float ) -> Matrix:
        for i in range( self.rows ):
            for j in range( self.cols ):
                self[i][j] /= scalar
        return self
    
    def __ifloordiv__( self, scalar: float ) -> Matrix:
        for i in range( self.rows ):
            for j in range( self.cols ):
                self[i][j] //= scalar
        return self
    
    # def round( self, value: float ) -> Matrix:
    #     newMatrix: Matrix = self.copy()
    #     for iRowIndex in range( self.rows ):
    #         for iColumnIndex in range( self.cols ):
    #             newMatrix[ iRowIndex ][ iColumnIndex ] = round( newMatrix[ iRowIndex ][ iColumnIndex ], value ) #! Il faut demander si nous avons le droit d'utiliser la fonction round()
    #     return newMatrix
    
    
    # Comparison magic methods
    
    def __eq__( self, other: Matrix ) -> bool:
        if ( self.rows != other.rows or self.cols != other.cols ): return False
        for i in range( self.rows ):
            for j in range( self.cols ):
                if ( self[i][j] != other[i][j] ):
                    return False
        return True
    
    def __ne__( self, other: Matrix ) -> bool:
        if ( self.rows != other.rows or self.cols != other.cols ): return True
        for i in range( self.rows ):
            for j in range( self.cols ):
                if ( self[i][j] != other[i][j] ):
                    return True
        return False
    

    # Logical magic methods

    def __bool__( self ) -> bool:
        for row in self.table:
            for value in row:
                if ( value != 0 ):
                    return True
        return False
    
    
    
    def remove( self, iRow: int, iColumn: int ) -> Matrix:
        #todo <= 0
        newMatrix: Matrix = Matrix.null( self.rows-1, self.cols-1 )
        
        iRowSkip: int = 0
        for iRowIndex in range( newMatrix.rows ):
            if ( iRowIndex == iRow ): iRowSkip += 1
            
            iColumnSkip: int = 0
            for iColumnIndex in range( newMatrix.cols ):
                if ( iColumnIndex == iColumn ): iColumnSkip += 1
                
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iRowIndex + iRowSkip ][ iColumnIndex + iColumnSkip ]
        
        return newMatrix
    
    def rotateLeft( self ) -> Matrix:
        newMatrix: Matrix = Matrix.null( self.cols, self.rows )
        for iRowIndex in range( newMatrix.rows ):
            for iColumnIndex in range( newMatrix.cols ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iColumnIndex ][ self.rows - iRowIndex - 1 ]
        return newMatrix
    
    def rotateRight( self ) -> Matrix:
        newMatrix: Matrix = Matrix.null( self.cols, self.rows )
        for iRowIndex in range( newMatrix.rows ):
            for iColumnIndex in range( newMatrix.cols ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ self.cols - iColumnIndex - 1 ][ iRowIndex ]
        return newMatrix
    

    def __repr__( self ) -> str:
        firstRowCharacter = [ "/", "│", "\\" ]
        lastRowCharacters = [ "\\", "│", "/" ]
        output: str = ""
        for iRowIndex in range( self.rows ):
            iRowCharactersIndex = ( ( iRowIndex + 1 ) // self.rows ) + bool( iRowIndex )
            output += firstRowCharacter[ iRowCharactersIndex ]
            for iColumnIndex in range( self.cols ):
                output += " " + str( self[ iRowIndex ][ iColumnIndex ] )
            output += " " + lastRowCharacters[ iRowCharactersIndex ] + "\n"
        return output


from vector import Vector