from __future__ import annotations
from vector import Vector
from matrix import Matrix
from maths import PI, cos, sin


class HalfCylinder:
    def __init__( self, position: Vector, height: float, radius: float, heightDirection: int, demiType: int, mass: float = 1 ):
        self.position: Vector = position
        self.position[heightDirection] -= height / 2
        self.height: float = height
        self.radius: float = radius
        self.heightDirection: int = heightDirection
        self.xMul: int = -1 if demiType == 0 else 1
        self.mass: float = mass
        self.points: tuple[ list[ float ], list[ float ], list[ float ] ] = ( [], [], [] )
    
    def inertia( self ) -> Matrix:
        density: float = self.mass / ( PI * self.radius**2 * self.height )

        inertiaMatrix: Matrix = Matrix.identity( 3 )
        inertiaMatrix[0][0] = density * ( ( self.radius * self.height )**2 * PI/4 )
        inertiaMatrix[1][1] = density * ( ( ( self.radius * self.height )**2 * PI/2 + self.radius**4 * self.height * self.xMul ) / 2 )
        inertiaMatrix[2][2] = self.xMul * density * ( ( self.radius**4 * self.height ) / 2 )

        return inertiaMatrix

    def create_points( self, pointsCountHeight: int, pointsCountCircle: int ) -> None:
        self.points[0].clear()
        self.points[1].clear()
        self.points[2].clear()

        heightStep: float = self.height / ( pointsCountHeight - 1 )
        circleStep: float = PI / pointsCountCircle

        for i in range( pointsCountCircle ):
            theta: float = i * circleStep
            cosinus: float = self.radius * cos( theta )
            sinus: float = self.radius * sin( theta )
            for j in range( pointsCountHeight ):
                self.points[self.heightDirection].append( self.position[self.heightDirection] + heightStep * j )
                self.points[self.heightDirection-1].append( self.position[self.heightDirection-1] - sinus * self.xMul )
                self.points[self.heightDirection-2].append( self.position[self.heightDirection-2] - cosinus * self.xMul )