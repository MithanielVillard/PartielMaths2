from matrix import Matrix
from maths import *
import matplotlib.pyplot as plt

def cube(n, a):
    w : Matrix = Matrix.null(n, 3)
    k : int = 0

    n2 = int(round(n**(1/3)))
    dx = a/(n2-1)
    for z in range(n2):
        for y in range(n2):
            for x in range(n2):
                w[k] = [x * dx - a/2, y * dx - a/2, z * dx - a/2]
                k += 1

    return w.T()


def cylindre(n: int, r, H):
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
                w[k] = [x, y , z]
                k += 1

    return w.T()

def triangle(n, c):
    totalPoints: int = int(n ** (1 / 3))
    W : Matrix = Matrix.null(n, 3)
    k : int = 0

    for z in range(totalPoints):
        for y in range(totalPoints):
            for x in range(totalPoints):

                u = x / (totalPoints - 1) * c
                v = y / (totalPoints - 1)

                dx = c / (totalPoints - 1)
                dy = u / c * c

                W[k] = [x * dx - c/2, dy * v - c/2, z * dx - c/2]
                k += 1
    return W.T()

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