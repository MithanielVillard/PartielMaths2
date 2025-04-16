import matplotlib.pyplot as plt
from maths import PI
from vector import Vector
from matrix import Matrix
from draw import draw


def translate( position: Vector, speed: Vector, forces: list[ tuple[ Vector, Vector ] ], mass: float, h: float ) -> tuple[ Vector, Vector ]:
    forcesSum: Vector = Vector.null(3)
    
    for force, _ in forces:
        forcesSum += force

    acceleration: Vector = forcesSum / mass

    position += speed * h
    speed += acceleration * h

    return position, speed


def rotate( position: Vector, invInertia: Matrix, theta: Vector, omega: Vector, forces: list[ tuple[ Vector, Vector ] ], h: float) -> tuple[ Vector, Vector ]:
    momentsSum: Vector = Vector.null(3)

    for force, point in forces:
        GA: Vector = point - position
        momentsSum += GA.cross( force )

    omegaPrime: Vector = invInertia * momentsSum

    theta += omega * h
    omega += omegaPrime * h

    return theta, omega


def move( points: Matrix, inertia: Matrix, forces: list[ tuple[ Vector, Vector ] ], translation: Vector, speed: Vector, theta: Vector, omega: Vector, mass: float, t: int, n: int ):
    temp: Matrix = points
    step: float = n / t

    invInertia: Matrix = inertia.inverse()

    translation, speed = translate( translation, speed, forces, 1, step )
    theta, omega = rotate( translation, invInertia, theta, omega, forces, step )

    for i in range(n):
        translation, speed = translate( Vector.null(3), speed, [ ( Vector.null(3), Vector.null(3) ) ], 1, step )

        transpose: Matrix = temp.transpose()
        for k in range( transpose.rows ):
            theta, omega = rotate( Vector( transpose[k] ), invInertia, Vector.null(3), omega, [ ( Vector.null(3), Vector.null(3) ) ], step )
            transpose[k][0] += translation.x()
            transpose[k][1] += translation.y()
            transpose[k][2] += translation.z()
            transpose[k] = ( Matrix.rotation3Bis( theta * PI/180 ) * Vector( transpose[k] ) ).values
        temp = transpose.transpose()

        draw( temp )
    
    plt.show()