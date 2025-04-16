from __future__ import annotations
from vector import Vector
from matrix import Matrix


class Cube:
    def __init__( self, position: Vector, edge: float, mass: float = 1.0 ):
        self.position: Vector = Vector.one(3)
        self.position *= -edge/2
        self.position += position
        self.edge: float = edge
        self.mass: float = mass
        self.points: tuple[ list[ float ], list[ float ], list[ float ] ] = ( [], [], [] )
    
    def inertia( self ) -> Matrix:
        density: float = self.mass / ( self.edge**3 )
        
        x2dv: float = ( ( self.position.x() + self.edge )**3 - self.position.x()**3 ) / 3
        y2dv: float = ( ( self.position.y() + self.edge )**3 - self.position.y()**3 ) / 3
        z2dv: float = ( ( self.position.z() + self.edge )**3 - self.position.z()**3 ) / 3

        inertiaMatrix: Matrix = Matrix.identity( 3 )
        inertiaMatrix[0][0] = density * ( ( y2dv + z2dv ) * self.edge**2 )
        inertiaMatrix[1][1] = density * ( ( x2dv + z2dv ) * self.edge**2 )
        inertiaMatrix[2][2] = density * ( ( x2dv + y2dv ) * self.edge**2 )

        return inertiaMatrix
    
    def create_points( self, pointsCount: int ) -> None:
        self.points[0].clear()
        self.points[1].clear()
        self.points[2].clear()
        
        n: int = int( round( pointsCount**( 1/3 ) ) )
        
        step: float = self.edge / ( n - 1 )
        
        for x in range( n ):
            for y in range( n ):
                for z in range( n ):
                    self.points[0].append( self.position.x() + step * x )
                    self.points[1].append( self.position.y() + step * y )
                    self.points[2].append( self.position.z() + step * z )