from matrix import Matrix
from maths import *
import matplotlib.pyplot as plt

def cube(n, L, l, h, pos : tuple[float, float, float]):
    w : Matrix = Matrix.null(n, 3)
    k : int = 0

    n2 = int(round(n**(1/3)))
    dx = L/(n2-1)
    dy = h/(n2-1)
    dz = l/(n2-1)
    for z in range(n2):
        for y in range(n2):
            for x in range(n2):
                w[k] = [pos[0] + x * dx - L/2, pos[1] + y * dy - h/2, pos[2] + z * dz - l/2]
                k += 1

    return w.T()


def cylindre(n: int, r, H, pos : tuple[float, float, float]):
    totalPoints: int = int(n ** (1 / 3))

    w : Matrix = Matrix.null(n, 3)
    theta = 360 / totalPoints
    thetaR = r / (totalPoints - 1)

    k : int = 0

    for h in range(totalPoints):
        for j in range(totalPoints):
            for i in range(totalPoints):
                x = thetaR * j * cos(theta * i * PI / 180)
                y = thetaR * j * sin(theta * i * PI / 180)
                z = h * H / (totalPoints - 1)
                w[k] = [pos[0] + x, pos[1] + y , pos[2] + z]
                k += 1

    return w.T()

def triangle(n, L, l, h, pos : tuple[float, float, float]):
    totalPoints: int = int(n ** (1 / 3))
    W : Matrix = Matrix.null(n, 3)
    k : int = 0

    dz = l / (totalPoints - 1)
    for z in range(totalPoints):
        for y in range(totalPoints):
            for x in range(totalPoints):

                u = x / (totalPoints - 1) * L
                v = y / (totalPoints - 1)

                dx = L / (totalPoints - 1)
                dy = u / L * h

                W[k] = [pos[0] + x * dx - L/2, pos[1] + dy * v - h/2, pos[2] + z * dz - l/2]
                k += 1
    return W.T()

def geo() -> Matrix:
    base = cube(256, 200, 100, 100, (0, 0, 0)).T().lliValues
    top = cube(128, 50, 100, 100, (-25, 100, 0)).T().lliValues
    avant = triangle(128, 50, 100, 100, (-75, 100, 0)).T().lliValues

    roue_br = cylindre(1000, 25, 30, (100, -25, 50)).T().lliValues
    roue_bl = cylindre(1000, 25, 30, (100, -25, -75)).T().lliValues
    roue_fr = cylindre(1000, 25, 30, (-100, -25, 50)).T().lliValues
    roue_fl = cylindre(1000, 25, 30, (-100, -25, -75)).T().lliValues

    base.extend(top)
    base.extend(avant)
    base.extend(roue_br)
    base.extend(roue_bl)
    base.extend(roue_fr)
    base.extend(roue_fl)
    return Matrix(base).T()

fig = plt.figure()
plt.rcParams['axes3d.mouserotationstyle'] = 'azel'
ax = plt.axes(projection='3d')

def draw(points : Matrix):
   X, Z, Y = points[0], points[1], points[2]

   ax.cla()
   ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
   ax.set_xlim([-500, 500])
   ax.set_ylim([-500, 500])
   ax.set_zlim([-500, 500])

   plt.draw()
   plt.pause(0.01)
   pass