from matrix import Matrix
from vector import Vector
from shapes import cube, cylindre, draw
from maths import PI

import matplotlib.pyplot as plt

def translate(m: float, f: list[tuple[Vector, Vector]], G: Vector, vG: Vector, h: float) -> tuple[Vector, Vector]:
    sommesForce: Vector = Vector([0, 0, 0])

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

def mouvement(W : Matrix, m : float, I : Matrix, F : list[tuple[Vector, Vector]], G : Vector, vG : Vector, teta : Vector, omega : Vector, t : int, n : int):

    temp : Matrix = W
    step : float = n/t

    G, vG = translate(1, F, G, vG, step)
    teta, omega = rotation(I**-1, F, G, teta, omega, step)

    for i in range(n):
        G, vG = translate(1, [(Vector([0,0,0]), Vector([0,0,0]))], Vector.null(3), vG, step)

        transpose : Matrix = temp.T()
        print(teta)

        for k in range(transpose.iRows):
            teta, omega = rotation(I ** -1, [(Vector([0,0,0]), Vector([0,0,0]))], Vector(transpose[k]), Vector.null(3), omega, step)

            transpose[k][0] += G.x()
            transpose[k][1] += G.y()
            transpose[k][2] += G.z()
            transpose[k] = (Matrix.rotation3Bis(teta * PI/180) * Vector(transpose[k])).lValues
            #transpose[k][0], transpose[k][1], transpose[k][2], _ = (Matrix.translation(G) * Vector([*transpose[k], 1.0])).lValues
            #transpose[k] = [transpose[k][0] + G.x(), transpose[k][1] + G.y(), transpose[k][2] + G.z()]

        temp = transpose.T()
        draw(temp)
    plt.show()

cube_ : Matrix = Matrix([
    [1/3, 0, 0],
    [0, 1/3, 0],
    [0, 0, 1/3],
])
cube_ **= -1

force = [
    #(Vector([0.0, 2.0, 0.0]), Vector([0.0, 0.0, 0.0])),
    #(Vector([1.0, 0.0, 0.0]), Vector([0.0, 0.0, 1.0])),
    #(Vector([-1.0, 0.0, 0.0]), Vector([0.0, 0.0, -1.0])),
    (Vector([2.0, 0.0, 0.0]), Vector([0.0, 0.0, -1.0])),
]

teta : Vector = Vector([0.0, 0.0, 0.0])
omega : Vector = Vector([0.0, 0.0, 0.0])

g : Vector = Vector([0.0, 0.0, 0.0])
vG: Vector = Vector([0.0, 0.0, 0.0])

mouvement(cube(64, 100), 1, cube_, force, g, vG, teta, omega, 20, 50)
