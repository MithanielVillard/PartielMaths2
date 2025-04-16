from __future__ import annotations
from vector import Vector
from matrix import Matrix


class RectangularCuboid:
    def __init__( self, position: Vector, edges: Vector, mass: float = 1.0 ):
        self.position: Vector = Vector( [ position.x() - edges.x() / 2, position.y() - edges.y() / 2, position.z() - edges.z() / 2 ] )
        self.edges: Vector = edges
        self.mass: float = mass
        self.points: tuple[ list[ float ], list[ float ], list[ float ] ] = ( [], [], [] )
    
    def inertia( self ) -> Matrix:
        density: float = self.mass / ( self.edges.x() * self.edges.y() * self.edges.z() )
        
        xdv: float = self.edges.x()
        ydv: float = self.edges.y()
        zdv: float = self.edges.z()
        x2dv: float = ( ( self.position.x() + self.edges.x() )**3 - self.position.x()**3 ) / 3
        y2dv: float = ( ( self.position.y() + self.edges.y() )**3 - self.position.y()**3 ) / 3
        z2dv: float = ( ( self.position.z() + self.edges.z() )**3 - self.position.z()**3 ) / 3

        inertiaMatrix: Matrix = Matrix.identity( 3 )
        inertiaMatrix[0][0] = density * ( ( xdv * y2dv * zdv ) + ( xdv * ydv * z2dv ) )
        inertiaMatrix[1][1] = density * ( ( x2dv * ydv * zdv ) + ( xdv * ydv * z2dv ) )
        inertiaMatrix[2][2] = density * ( ( x2dv * ydv * zdv ) + ( xdv * y2dv * zdv ) )

        return inertiaMatrix
    
    def create_points( self, pointsCountX: int, pointsCountY: int, pointsCountZ: int ) -> None:
        self.points[0].clear()
        self.points[1].clear()
        self.points[2].clear()
        
        stepX: float = self.edges.x() / ( pointsCountX - 1 )
        stepY: float = self.edges.y() / ( pointsCountY - 1 )
        stepZ: float = self.edges.z() / ( pointsCountZ - 1 )
        
        for x in range( pointsCountX ):
            for y in range( pointsCountY ):
                for z in range( pointsCountZ ):
                    self.points[0].append( self.position.x() + stepX * x )
                    self.points[1].append( self.position.y() + stepY * y )
                    self.points[2].append( self.position.z() + stepZ * z )