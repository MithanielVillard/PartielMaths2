from matrix import Matrix
from vector import Vector

def translate(m: float, f: list[tuple[Vector, Vector]], G: Vector, vG: Vector, h: float) -> tuple[Vector, Vector]:
    sommesForce: Vector = Vector(0, 0, 0)

    for i in range(len(f)):
        sommesForce += f[i][0]

    acceleration: Vector = sommesForce / m

    new_G : Vector = vG * h + G
    new_vG : Vector = acceleration * h + vG

    return new_G, new_vG

                        #force   #point d'application
def rotation(I_inv : Matrix, F : list[tuple[Vector, Vector]], G : Vector, teta : Vector, omega : Vector, h : float):
    somme_moments : Vector = Vector([0, 0, 0])

    for force, pointapp in F:
        GA : Vector = pointapp - G
        somme_moments += GA.cross(force)

    omega_prime : Vector = I_inv * somme_moments

    new_teta : Vector = omega * h + teta
    new_omega : Vector = omega_prime * h + omega

    return new_teta, new_omega

cube : Matrix = Matrix([
    [1/3, 0, 0],
    [0, 1/3, 0],
    [0, 0, 1/3],
])
cube **= -1

force = [
    (Vector([0.0, 10.0, 0.0]), Vector([-1.0, -1.0, 0.0])),
]

teta : Vector = Vector([0.0, 0.0, 0.0])
omega : Vector = Vector([0.0, 0.0, 0.0])

for i in range(100):
    teta, omega = rotation(cube, force, Vector([0.0, 0.0, 0.0]), teta, omega, 0.1)
    print(teta, " omega : ", omega)
