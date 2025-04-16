from __future__ import annotations


class Vector:
    def __init__( self, values: list[ float ] ):
        self.values: list[ float ] = values
        self.size: int = len( values )
    
    def copy( self ) -> Vector: return Vector( [ value for value in self.values ] )
    

    # Default Static Vectors (Null & Identity)

    @staticmethod
    def null( size: int ) -> Vector: return Vector( [ 0.0 for _ in range( size ) ] )
    
    @staticmethod
    def one( size: int ) -> Vector: return Vector( [ 1.0 for _ in range( size ) ] )

    @staticmethod
    def right( size: int ) -> Vector:
        output: Vector = Vector.null( size )
        output[0] = 1.0
        return output

    @staticmethod
    def up( size: int ) -> Vector:
        output: Vector = Vector.null( size )
        output[1] = 1.0
        return output

    @staticmethod
    def forward( size: int ) -> Vector:
        output: Vector = Vector.null( size )
        output[2] = 1.0
        return output
    
    
    # Math methods

    def dot( self, other: Vector ) -> float:
        if ( self.size != other.size ): raise ValueError
        output: float = 0.0
        for i in range( self.size ):
            output += self[i] * other[i]
        return output
    
    def cross( self, other: Vector ) -> Vector:
        if ( not ( self.size == other.size == 3 ) ): raise ValueError
        output: Vector = Vector.null( self.size )
        for i in range( -2, 1 ):
            output[i] = self[i+1] * other[i+2] - self[i+2] * other[i+1]
        return output
    
    def norm( self ) -> float:
        output: float = 0.0
        for i in range( self.size ):
            output += self[i] * self[i]
        return output**0.5
    
    def norm_squared( self ) -> float:
        output: float = 0.0
        for i in range( self.size ):
            output += self[i] * self[i]
        return output
    
    def normalize( self ) -> Vector:
        norm: float = self.norm()
        return Vector( [ value / norm for value in self.values ] )
    
    def normalize_self( self ) -> None:
        norm: float = self.norm()
        for i in range( self.size ):
            self.values[i] /= norm
    
    
    # Getter & Setter
    
    def x( self ) -> float: return self.values[0]
    def y( self ) -> float: return self.values[1]
    def z( self ) -> float: return self.values[2]
    
    def __getitem__( self, index: int ) -> float: return self.values[index]
    def __setitem__( self, index: int, value: float ): self.values[index] = value
    
    
    # Arithmetic magic methods
    
    def __add__( self, other: Vector ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        return Vector( [ self[i] + other[i] for i in range( self.size ) ] )
    
    def __sub__( self, other: Vector | float ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        return Vector( [ self[i] - other[i] for i in range( self.size ) ] )
    
    def __mul__( self, other: Vector | float ) -> Vector: return self.__mul__Vector( other ) if isinstance( other, Vector ) else self.__mul__float( other )
    
    def __mul__Vector( self, other: Vector ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        return Vector( [ self[i] * other[i] for i in range( self.size ) ] )
    
    def __mul__float( self, scalar: float ) -> Vector: return Vector( [ value * scalar for value in self.values ] )
    
    def __truediv__( self, other: Vector | float ) -> Vector: return self.__truediv__Vector( other ) if isinstance( other, Vector ) else self.__truediv__float( other )
    
    def __truediv__Vector( self, other: Vector ) -> Vector: return Vector( [ self[i] / other[i] for i in range( self.size ) ] )
    
    def __truediv__float( self, scalar: float ) -> Vector: return Vector( [ value / scalar for value in self.values ] )
    
    def __floordiv__( self, scalar: float ) -> Vector: return Vector( [ value // scalar for value in self.values ] )

    def __pow__( self, power: int ) -> Vector:
        output: Vector = Vector.one( self.size )
        for _ in range( power ):
            output *= power
        return output

    def __neg__( self ) -> Vector: return Vector( [ -value for value in self.values ] )
    

    # Assignment magic methods

    def __iadd__( self, other: Vector ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        for i in range( self.size ):
            self[i] += other[i]
        return self

    def __isub__( self, other: Vector ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        for i in range( self.size ):
            self[i] -= other[i]
        return self
    
    def __imul__( self, other: Vector | float ) -> Vector: return self.__imul__Vector( other ) if isinstance( other, Vector ) else self.__imul__float( other )

    def __imul__Vector( self, other: Vector ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        for i in range( self.size ):
            self[i] *= other[i]
        return self

    def __imul__float( self, scalar: float ) -> Vector:
        for i in range( self.size ):
            self[i] *= scalar
        return self

    def __itruediv__( self, other: Vector | float ) -> Vector: return self.__itruediv__Vector( other ) if isinstance( other, Vector ) else self.__itruediv__float( other )
    
    def __itruediv__Vector( self, other: Vector ) -> Vector:
        if ( self.size != other.size ): raise ValueError
        for i in range( self.size ):
            self[i] *= other[i]
        return self

    def __itruediv__float( self, scalar: float ) -> Vector:
        for i in range( self.size ):
            self[i] /= scalar
        return self
    
    def __ifloordiv__( self, scalar: float ) -> Vector:
        for i in range( self.size ):
            self[i] //= scalar
        return self

    def __ipow__( self, power: int ) -> Vector:
        copy: Vector = self.copy()
        for _ in range( power ):
            self *= copy
        return self
    
    
    # Comparison magic methods
    
    def __eq__( self, other: Vector ) -> bool:
        if ( self.size != other.size ): return False
        for i in range( self.size ):
            if ( self[i] != other[i] ):
                return False
        return True
    
    def __eq__( self, other: Vector ) -> bool:
        if ( self.size != other.size ): return True
        for i in range( self.size ):
            if ( self[i] != other[i] ):
                return True
        return False
    

    # Logical magic methods
    
    def __bool__( self ) -> bool:
        for value in self.values:
            if ( value != 0.0 ):
                return True
        return False
    
    
    def __repr__( self ) -> str:
        sPrint = "("
        if ( self.size > 0 ):
            sPrint += str( self.values[ 0 ] )
            for iIndex in range( 1, self.size ):
                sPrint += ", " + str( self.values[ iIndex ] )
        sPrint += ")"
        return sPrint


from matrix import Matrix