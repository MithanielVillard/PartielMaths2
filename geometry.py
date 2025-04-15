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
    return Matrix(W).transpose()


def carre_plein(n,a):
    W=[]
    if n-1 != 0:
        for x in range (int(n ** 0.5)):
            for y in range (int(n ** 0.5)):
                W.append([x*a,0,y*a])
       
    else:
        print("n have to be different")
    return Matrix(W).transpose()

def pave_plein(n, a, b, c) :
    W=[]
    if n-1 != 0:
        res_r = int(n ** (1/3))
        res_a = int(n ** (1/3))
        res_h = int(n ** (1/3))
        for z in range (res_r):
            for x in range (res_a):
                for y in range (res_h):
                    W.append([x*a,z*b,y*c])
       
    else:
        print("n have to be different")

    return Matrix(W).transpose()

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
    return Matrix(W).transpose()
    
def cylindre_plein(n, R, h):
    W = []

    res_r = int(n ** (1/3))
    res_a = int(n ** (1/3))
    res_h = int(n ** (1/3))

    rayon_step = R / res_r
    angle_step = 2 * maths.PI / res_a
    hauteur_step = h / res_h

    for u in range(res_h):
        for i in range(res_r):
            for j in range(res_a):
                rayon = i * rayon_step
                angle = j * angle_step
                hauteur = u * hauteur_step

                x = rayon * maths.cos(angle)
                y = rayon * maths.sin(angle)
                z = hauteur

                W.append([x, y, z])
    return Matrix(W).transpose()