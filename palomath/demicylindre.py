from __future__ import annotations
from vector import Vector
from matrix import Matrix
from maths import PI, cos, sin


class DemiCylindre:
    def __init__(
        self,
        position: Vector = Vector.null(3),
        rotationMatrix: Matrix = Matrix.identity(3),
        scale: Vector = Vector.one(3),
        mass: float = 1
    ):
        self.position: Vector = position
        self.rotationMatrix: Matrix = rotationMatrix
        self.scale: Vector = scale
        self.mass: float = mass

        rayon: float = scale.x() * 0.5
        hauteur: float = scale.y()

        self.inertiaMatrix: Matrix = Matrix.identity(3)

        self.inertiaMatrix[0][0] = (1 / 12) * mass * (3 * rayon**2 + hauteur**2) / 2
        self.inertiaMatrix[1][1] = (1 / 12) * mass * (3 * rayon**2 + hauteur**2) / 2
        self.inertiaMatrix[2][2] = (1 / 2) * mass * rayon**2 / 2

    def CreateDemiCylinder(self, n: int = 1000) -> tuple[list[float], list[float], list[float]]:
        X: list[float] = []
        Y: list[float] = []
        Z: list[float] = []

        radial_steps: int = int(n ** (1/3))
        angle_steps: int = int(n ** (1/3))
        height_steps: int = int(n ** (1/3))

        for i in range(radial_steps):
            r = (i / (radial_steps - 1)) * 0.5  # rayon standardisé

            for j in range(angle_steps):
                theta = (j / (angle_steps - 1)) * PI

                x = r * cos(theta)
                y = r * sin(theta)

                for k in range(height_steps):
                    z = (k / (height_steps - 1)) - 0.5  # valeur de z standardisée entre -0.5 et 0.5

                    # Mise à l'échelle personnalisée sur les 3 axes
                    local_point = Vector([
                        x * self.scale.x(),
                        y * self.scale.y(),
                        z * self.scale.z()
                    ])

                    rotated_point = self.rotationMatrix * local_point
                    global_point = rotated_point + self.position

                    X.append(global_point.x())
                    Y.append(global_point.y())
                    Z.append(global_point.z())

        return X, Y, Z
