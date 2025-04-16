import matplotlib.pyplot as plt
from matrix import Matrix


fig1 = plt.figure()
ax1 = plt.axes( projection="3d" )

fig2 = plt.figure()
ax2 = plt.axes( projection="3d" )

def draw( points: Matrix ):
   X, Z, Y = points[0], points[1], points[2]

   ax1.cla()
   ax1.scatter3D( X, Y, Z, color="red" )
   ax1.set_aspect('equal')

   ax2.cla()
   ax2.scatter3D( X, Y, Z, color="red" )
   ax2.set_xlim( [ 0, 225 ] )
   ax2.set_ylim( [ -50, 50 ] )
   ax2.set_zlim( [ 0, 170 ] )

   plt.draw()
   plt.pause(0.01)
   pass