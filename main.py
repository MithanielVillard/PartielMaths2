import sys
import matplotlib.pyplot as plt
import geometry as geo
from geometry import *
from math import *

#Some thinking : isn't it worth to make 2 full circles (bottom and up)
# and multiple empty circle ? Less points to calculate

#plt.rcParams['axes3d.mouserotationstyle'] = 'azel'

X = [[-1,2],
    [0 ,1],
    [3 ,4]]

result = [[0,0,0],
         [0,0,0]]




A = [1,3]

#(X,Y,Z)=ligne(20,-5,5)
#(X,Y,Z)=carre_plein(10000,60)
# (X,Y,Z)=pave_plein(2000, 60, 60, 60)
#(X,Y,Z)=cercle_plein(300,5)

(X,Y,Z)=geo.cylindre_plein(20, 5, 10)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')
plt.ylabel('Oskour Studio')
plt.show()

# print(factoriel(6))
# print(sin(1/2))

# print(X)
# transpose(X)
# print(result)
# result = ligne(2, 10, 20)
# plt.plot(result)
# plt.show()

print("Hello World")
