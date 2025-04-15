import sys
import matplotlib.pyplot as plt
import geometry as geo
from geometry import *
from math import *

#Some thinking : isn't it worth to make 2 full circles (bottom and up)
# and multiple empty circle ? Less points to calculate

#plt.rcParams['axes3d.mouserotationstyle'] = 'azel'

def translate_points(points, dx=0, dy=0, dz=0):
    return [[x + dx, y + dy, z + dz] for x, y, z in points]

def solide(n):
    pave = pave_plein(n, 500, 500, 500)
    cylindre1 = cylindre_plein(n, 5, 10)
    cylindre2 = cylindre_plein(n, 5, 10)
    cylindre3 = cylindre_plein(n, 5, 10)
    cylindre4 = cylindre_plein(n, 5, 10)

    all_points = [*zip(*pave), *zip(*cylindre1), *zip(*cylindre2), *zip(*cylindre3), *zip(*cylindre4)]
    return all_points
    
def afficher_solide_3d(points):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    x = [p[0] for p in points]
    y = [p[1] for p in points]
    z = [p[2] for p in points]
    ax.scatter(x, y, z, c='b', s=1500)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])
    ax.set_title(f'Solide 3D ({len(points)} points)')
    plt.tight_layout()
    plt.show()

points = solide(500)
afficher_solide_3d(points)


