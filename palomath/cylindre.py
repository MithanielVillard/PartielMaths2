from __future__ import annotations
from vector import Vector
from matrix import Matrix
from maths import PI, cos, sin


class Cylindre:
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
        self.mass: float = mass

        rayon: float = scale.x() * 0.5
        hauteur: float = scale.y()    

        volume: float = PI * rayon**2 * hauteur

        self.inertiaMatrix: Matrix = Matrix.identity( 3 )

        #formule du cours
        self.inertiaMatrix[0][0] = (1 / 12) * mass * (3 * rayon**2 + hauteur**2)
        self.inertiaMatrix[1][1] = (1 / 12) * mass * (3 * rayon**2 + hauteur**2)
        self.inertiaMatrix[2][2] = (1 / 2)  * mass * rayon**2

    def CreateCylinder(self, n: int = 100) -> tuple[list[float], list[float], list[float]]:
        X: list[float] = []
        Y: list[float] = []
        Z: list[float] = []

        angle_steps: int = int(n**0.5)
        height_steps: int = int(n**0.5)

        for i in range(angle_steps):
            theta: float = (i / angle_steps) * 2 * PI
            x: float = (self.scale.x() * 0.5) * cos(theta)
            y: float = (self.scale.x() * 0.5) * sin(theta)

            for j in range(height_steps):
                z = (j / (height_steps - 1)) * (self.scale.y()) - ((self.scale.y()) * 0.5)
                local_point = Vector([x, y, z])
                rotated_point = self.rotationMatrix * local_point
                global_point = rotated_point + self.position

                X.append(global_point.x())
                Y.append(global_point.y())
                Z.append(global_point.z())

        return X, Y, Z
    
    