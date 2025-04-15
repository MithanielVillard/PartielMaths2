import matrix
from matrix import *
import maths
from maths import *

def ligne(n,xmin,xmax):
    W=[]
    if n-1 != 0:
        dx=(xmax-xmin)/(n-1)
        for x in range (n):
            W.append([x*dx,0,0])
    else:
        print("n have to be different")
    return(matrix.transpose(W))


def carre_plein(n,a):
    W=[]
    if n-1 != 0:
        for x in range (int(n ** 0.5)):
            for y in range (int(n ** 0.5)):
                W.append([x*a,0,y*a])
       
    else:
        print("n have to be different")
    return(matrix.transpose(W))

def pave_plein(n, a, b, c) :
    W=[]
    if n-1 != 0:
        for z in range (int (n ** 0.5)):
            for x in range (int(n ** 0.5)):
                for y in range (int(n ** 0.5)):
                    W.append([x*a,z*a,y*a])
       
    else:
        print("n have to be different")
    return(matrix.transpose(W))

def cercle_plein(n, R):
    if n <= 1:
        print("n must be greater than 1.")
        return None
    
    W = []
    rayon_step = R / n
    angle_step = 2 * maths.PI / n
    
    for i in range(n):
        for j in range(n):
            rayon = i * rayon_step
            angle = j * angle_step

            x = rayon * maths.cos(angle)
            y = rayon * maths.sin(angle)
            z = 0

            W.append([x, y, z])
    return transpose(W)
    
def cylindre_plein(n, R, h):
    if n <= 1:
        print("n must be greater than 1.")
        return None
    if h == 0:
        print("h must not be equal to 0.")
        return None

    W = []
    rayon_step = R / n
    angle_step = 2 * maths.PI / n
    hauteur_step = h / n

    for u in range(h):
        for i in range(n):
            for j in range(n):
                rayon = i * rayon_step
                angle = j * angle_step
                hauteur = u * hauteur_step

                x = rayon * cos(angle)
                y = rayon * sin(angle)
                z = hauteur

                W.append([x, y, z])

    m = Matrix(W)
    return m.transpose()