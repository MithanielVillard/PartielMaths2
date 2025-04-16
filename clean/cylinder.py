from __future__ import annotations
from vector import Vector
from matrix import Matrix
from maths import PI, cos, sin


class Cylinder:
    def __init__( self, position: Vector, height: float, radius: float, heightDirection: int, mass: float = 1 ):
        self.position: Vector = position
        self.position[heightDirection] -= height / 2
        self.height: float = height
        self.radius: float = radius
        self.heightDirection: int = heightDirection
        self.mass: float = mass
        self.points: tuple[ list[ float ], list[ float ], list[ float ] ] = ( [], [], [] )
    
    def inertia( self ) -> Matrix:
        density: float = self.mass / ( PI * self.radius**2 * self.height )

        inertiaMatrix: Matrix = Matrix.identity( 3 )
        inertiaMatrix[self.heightDirection][self.heightDirection] = density * ( self.radius**2 / 2 )
        inertiaMatrix[self.heightDirection-1][self.heightDirection-1] = density * ( self.radius**2 / 4 + self.height**2 / 3 )
        inertiaMatrix[self.heightDirection-2][self.heightDirection-2] = density * ( self.radius**2 / 4 + self.height**2 / 3 )

        return inertiaMatrix

    def create_points( self, pointsCountHeight: int, pointsCountCircle: int ) -> None:
        self.points[0].clear()
        self.points[1].clear()
        self.points[2].clear()

        heightStep: float = self.height / ( pointsCountHeight - 1 )
        circleStep: float = ( 2.0 * PI ) / pointsCountCircle

        for i in range( pointsCountCircle ):
            theta: float = i * circleStep
            cosinus: float = self.radius * cos( theta )
            sinus: float = self.radius * sin( theta )
            for j in range( pointsCountHeight ):
                self.points[self.heightDirection].append( self.position[self.heightDirection] + heightStep * j )
                self.points[self.heightDirection-1].append( self.position[self.heightDirection-1] + sinus )
                self.points[self.heightDirection-2].append( self.position[self.heightDirection-2] + cosinus )