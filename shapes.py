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

def cylindre(n, r, h):
    w : Matrix = Matrix.null(n, 3)
    k : int = 0

    theta = 360 / n
    thetaR = r / n

    R = 0
    for j in range(n):
        for i in range(n):
            x = R * cos(theta * i * PI / 180)
            y = R * sin(theta * i * PI / 180)
            z = 0
            w[k] = [x, y , z]
        R += thetaR

    return w.T()


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