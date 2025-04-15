from __future__ import annotations
from vector import Vector
from matrix import Matrix


class RectangularCuboid:
    def __init__(
            self,
            position: Vector = Vector.null( 3 ),
            rotationMatrix: Matrix = Matrix.identity( 3 ),
            scale: Vector = Vector.one( 3 ),
            mass: float = 1
    ):
        self.position: Vector = position
        self.rotationMatrix: Matrix = rotationMatrix
        self.scale: Vector = scale

        volume: float = scale.x() * scale.y() * scale.z()
        masseVolumique: float = mass / volume

        xdv: float = self.bottomRight().x() - self.topLeft().x()
        ydv: float = self.bottomRight().y() - self.topLeft().y()
        zdv: float = self.bottomRight().z() - self.topLeft().z()
        x2dv: float = ( self.bottomRight().x()**3 - self.topLeft().x()**3 ) / 3
        y2dv: float = ( self.bottomRight().y()**3 - self.topLeft().y()**3 ) / 3
        z2dv: float = ( self.bottomRight().z()**3 - self.topLeft().z()**3 ) / 3

        self.inertiaMatrix: Matrix = Matrix.identity( 3 )
        self.inertiaMatrix[0][0] = masseVolumique * ( ( xdv * y2dv * zdv ) + ( xdv * ydv * z2dv ) )
        self.inertiaMatrix[1][1] = masseVolumique * ( ( x2dv * ydv * zdv ) + ( xdv * ydv * z2dv ) )
        self.inertiaMatrix[2][2] = masseVolumique * ( ( x2dv * ydv * zdv ) + ( xdv * y2dv * zdv ) )
    
    def topLeft( self ) -> Vector: return self.position - ( self.scale / 2 )
    def bottomRight( self ) -> Vector: return self.position + ( self.scale / 2 )


    def CreatePave(self, n: int = 10) -> tuple[list[float], list[float], list[float]]:
        X: list[float] = []
        Y: list[float] = []
        Z: list[float] = []
    
        # Valeurs comprises entre -0.5 et 0.5
        steps = [i / (n - 1) - 0.5 for i in range(n)]
    
        # Les 3 paires d'axes (face constante, axes variables)
        faces = [
            (0, 1, 2),  # face parallèle au plan yz (x constant)
            (1, 0, 2),  # face parallèle au plan xz (y constant)
            (2, 0, 1),  # face parallèle au plan xy (z constant)
        ]
    
        for fixed_axis, axis1, axis2 in faces:
            for sign in (-1, 1):  # face avant/arrière, haut/bas, gauche/droite
                for s1 in steps:
                    for s2 in steps:
                        coords = [0.0, 0.0, 0.0]
                        coords[fixed_axis] = sign * 0.5
                        coords[axis1] = s1
                        coords[axis2] = s2
    
                        local = Vector([
                            coords[0] * self.scale.x(),
                            coords[1] * self.scale.y(),
                            coords[2] * self.scale.z()
                        ])
    
                        rotated = self.rotationMatrix * local
                        global_point = rotated + self.position
    
                        X.append(global_point.x())
                        Y.append(global_point.y())
                        Z.append(global_point.z())
    
        return X, Y, Z

