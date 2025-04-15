from matrix import Matrix
from vector import Vector

def translate(m: float, f: list[tuple[Vector, Vector]], g: Vector, vG: Vector, h: float) -> tuple[Vector, Vector]:
    sommesForce: Vector = Vector(0, 0, 0)

    for i in range(len(f)):
        sommesForce += f[i][0]

    acceleration: Vector = sommesForce / m

    new_G : Vector = vG * h + g
    new_vG : Vector = acceleration * h + vG

    return new_G, new_vG

                        #force   #point d'application
def rotation(I_inv, F : list[tuple[Vector, Vector]],G : Vector, teta, omega, h):
    somme_moments : Vector = Vector(0, 0, 0)

    for force, pointapp in F:
        GA : Vector = pointapp - G
        somme_moments += GA.cross(force)


force = [
    (Vector(5.0, 0.0, 0.0), Vector(0.0, 0.0, 0.0)),
    (Vector(0.0, 5.0, 0.0), Vector(0.0, 0.0, 0.0))
]
