import matplotlib.pyplot as plt

from vector import Vector
from matrix import Matrix
from cylindre import Cylindre
from pave import RectangularCuboid
from demicylindre import DemiCylindre

PI : float = 3.14159265359

def Transpose(m1: list[list[float]]) : 
    transpose: list[list[float]] = []
    for i in range(len(m1[0])):
        transpose.append([])
        for j in range(len(m1)):
            transpose[i].append(m1[j][i])
    return transpose

def ligne(n,xmin,xmax):
    W=[]
    dx=(xmax-xmin)/(n-1)
    for x in range (n):
        W.append([x*dx,0,0])
    return(Transpose(W))

def carrevide(n, a):
    W = []
    step = a / (int(n / 4))
    for i in range(int(n / 4)):
        W.append([-a/2 + i * step, -a/2, 0])
    for i in range(int(n / 4)):
        W.append([a/2, -a/2 + i * step, 0])
    for i in range(int(n / 4)):
        W.append([a/2 - i * step, a/2, 0])
    for i in range(int(n / 4)):
        W.append([-a/2, a/2 - i * step, 0])

    return Transpose(W)

def carreplein(n,a):
    W = []
    distance = a
    for x in range(int(n**(1/2))):
        for y in range(int(n**(1/2))):
            W.append([(x * distance), (y * distance), 0])
    
    return(Transpose(W))

def pave_plein(n,a,b,c):

    W = []
    for x in range(int(n**(1/2))):
        for y in range(int(n**(1/2))):
            for z in range(int(n**(1/2))):
                W.append([(x * a) - (a * n)/2, (y * b)-(b * n)/2, (z * c)-(c * n)/2])

    return Transpose(W)


def factorial(n : int) -> float:
    result : int = 1

    for i in range(n) :
        result *= i + 1

    return result

def cosinus(x, n):
    cosin = 0
    for i in range(n):
        cosin += (((-1)**i)*(x**(2*i)/factorial(2*i)))
    return cosin

def sinus(x, n):
    x = 3.14159265 * 0.5 - x
    sin = 0
    for i in range(n):
        sin += (((-1)**i)*(x**(2*i)/factorial(2*i)))
    return sin

def transpose_matrix(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed
        

def translation(X, Y, Z, moveX, moveY, moveZ):
    new_X = []
    new_Y = []
    new_Z = []
    for x in X:
        new_X.append(x + moveX)
    for y in Y:
        new_Y.append(y + moveY)
    for z in Z:
        new_Z.append(z + moveZ)
    return new_X, new_Y, new_Z


def rotateX(Y, Z, angle_rad):
    new_Y = []
    new_Z = []
    cos_a = cosinus(angle_rad, 10)
    sin_a = sinus(angle_rad, 10)
    for y, z in zip(Y, Z):
        new_Y.append(y * cos_a - z * sin_a)
        new_Z.append(y * sin_a + z * cos_a)
    return new_Y, new_Z

def rotateY(X, Z, angle_rad):
    new_X = []
    new_Z = []
    cos_a = cosinus(angle_rad, 10)
    sin_a = sinus(angle_rad, 10)
    for x, z in zip(X, Z):
        new_X.append(x * cos_a + z * sin_a)
        new_Z.append(-x * sin_a + z * cos_a)
    return new_X, new_Z

def rotateZ(X, Y, angle_rad):
    new_X = []
    new_Y = []
    cos_a = cosinus(angle_rad, 10)
    sin_a = sinus(angle_rad, 10)
    for x, y in zip(X, Y):
        new_X.append(x * cos_a - y * sin_a)
        new_Y.append(x * sin_a + y * cos_a)
    return new_X, new_Y

def main():

    roue1 = Cylindre(
    position=Vector([-0.3, -2.5, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.35, 0.2, 0.35]),
    mass=2
    )

    roue2 = Cylindre(
    position=Vector([-0.3, 2.5, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.35, 0.2, 0.35]),
    mass=2
    )

    barreDuMillieu = Cylindre(
    position=Vector([0.0, 0, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 4.7, 0.2]),
    mass=2
    )

    pave1 = RectangularCuboid(
        position=Vector([0.2, -2, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 2, 2]),
    mass=2
    )

    pave2 = RectangularCuboid(
        position=Vector([0.2, 2, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 2, 2]),
    mass=2
    )

    noseFront = DemiCylindre(
        position=Vector([0.2, 3, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 1.2, 2]),
    mass=2
    )

    noseBack = DemiCylindre(
        position=Vector([0.2, -3, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 1.2, 2]),
    mass=2
    )

    noseMidLeft = DemiCylindre(
        position=Vector([0.2, -1, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 1.2, 2]),
    mass=2
    )

    noseMidRight = DemiCylindre(
        position=Vector([0.2, 1, 0]),
    rotationMatrix=Matrix.identity(3),
    scale=Vector([0.2, 1.2, 2]),
    mass=2
    )

    Roue1X, Roue1Y, Roue1Z = roue1.CreateCylinder(n=100)
    Roue2X, Roue2Y, Roue2Z = roue2.CreateCylinder(n=100)

    barreDuMillieuX, barreDuMillieuY, barreDuMillieuZ = barreDuMillieu.CreateCylinder(n=100)
    barreDuMillieuY, barreDuMillieuZ = rotateX(barreDuMillieuY, barreDuMillieuZ, PI/2)

    pave1X, pave1Y, pave1Z = pave1.CreatePave(10)
    pave2X, pave2Y, pave2Z = pave2.CreatePave(10)

    noseFrontX, noseFrontY, noseFrontZ = noseFront.CreateDemiCylinder(1000)
    noseBackX, noseBackY, noseBackZ = noseBack.CreateDemiCylinder(1000)

    noseMidLeftX, noseMidLeftY, noseMidLeftZ = noseMidLeft.CreateDemiCylinder(1000)
    noseMidRightX, noseMidRightY, noseMidRightZ = noseMidRight.CreateDemiCylinder(1000)
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter3D(Roue1X, Roue1Y, Roue1Z, c='r')
    ax.scatter3D(Roue2X, Roue2Y, Roue2Z, c='r')

    ax.scatter3D(barreDuMillieuX, barreDuMillieuY, barreDuMillieuZ, c='g')

    ax.scatter3D(pave1X, pave1Y, pave1Z, c='black')
    ax.scatter3D(pave2X, pave2Y, pave2Z, c='black')

    ax.scatter3D(noseFrontX, noseFrontY, noseFrontZ, c='orange')
    ax.scatter3D(noseBackX, noseBackY, noseBackZ, c='orange')

    ax.scatter3D(noseMidLeftX, noseMidLeftY, noseMidLeftZ, c='orange')
    ax.scatter3D(noseMidRightX, noseMidRightY, noseMidRightZ, c='orange')


    ax.set_aspect('auto')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    
    plt.show()



main()

# plt.figure(figsize=(6, 6))
#     plt.plot(pointX, pointY, label=f"Ellipse (centre=({xC}, {yC}), a={a}, b={b})")
#     plt.axis("equal")
#     plt.legend()
#     plt.title("Tracé d'une ellipse")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.grid()
#     plt.show()

