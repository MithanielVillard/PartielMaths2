import matplotlib.pyplot as plt
from maths import PI
from vector import Vector
from matrix import Matrix
from cube import Cube
from rectangular_cuboid import RectangularCuboid
from half_cylinder import HalfCylinder
from cylinder import Cylinder
from movements import move


paveBack: RectangularCuboid =  RectangularCuboid( Vector( [ -2.5, 0.1, 0 ] ), Vector( [ 2, 0.2, 2 ] ) )
paveFront: RectangularCuboid = RectangularCuboid( Vector( [  2.5, 0.1, 0 ] ), Vector( [ 2, 0.2, 2 ] ) )

roundBack: HalfCylinder = HalfCylinder( Vector( [ -3.5, 0.1, 0 ] ), 0.2, 1, 1, 0 )
roundFront: HalfCylinder = HalfCylinder( Vector( [ 3.5, 0.1, 0 ] ), 0.2, 1, 1, 1 )
roundMiddleBack: HalfCylinder = HalfCylinder( Vector( [ -1.5, 0.1, 0 ] ), 0.2, 1, 1, 1 )
roundMiddleFront: HalfCylinder = HalfCylinder( Vector( [ 1.5, 0.1, 0 ] ), 0.2, 1, 1, 0 )

backWheel: Cylinder  = Cylinder( Vector( [ -3.0, -0.3, 0 ] ), 0.2, 0.3, 2 )
frontWheel: Cylinder = Cylinder( Vector( [  3.0, -0.3, 0 ] ), 0.2, 0.3, 2 )

middleBar: Cylinder = Cylinder( Vector( [ 0, 0, 0 ] ), 5, 0.1, 0 )

# cylinder: Cylinder = Cylinder( Vector.one(3), 100, 50, 1 )
# rectangularCuboid: RectangularCuboid = RectangularCuboid( Vector.one(3), Vector( [ 4, 2, 6 ] ) )


points: tuple[ list[ float ], list[ float ], list[ float ] ] = ( [], [], [] )

paveBack.create_points( 12, 2, 10 )
points[0].extend( paveBack.points[0] )
points[1].extend( paveBack.points[1] )
points[2].extend( paveBack.points[2] )

paveFront.create_points( 12, 2, 10 )
points[0].extend( paveFront.points[0] )
points[1].extend( paveFront.points[1] )
points[2].extend( paveFront.points[2] )

roundBack.create_points( 2, 18 )
points[0].extend( roundBack.points[0] )
points[1].extend( roundBack.points[1] )
points[2].extend( roundBack.points[2] )

roundFront.create_points( 2, 18 )
points[0].extend( roundFront.points[0] )
points[1].extend( roundFront.points[1] )
points[2].extend( roundFront.points[2] )

roundMiddleBack.create_points( 2, 18 )
points[0].extend( roundMiddleBack.points[0] )
points[1].extend( roundMiddleBack.points[1] )
points[2].extend( roundMiddleBack.points[2] )

roundMiddleFront.create_points( 2, 18 )
points[0].extend( roundMiddleFront.points[0] )
points[1].extend( roundMiddleFront.points[1] )
points[2].extend( roundMiddleFront.points[2] )

backWheel.create_points( 2, 12 )
points[0].extend( backWheel.points[0] )
points[1].extend( backWheel.points[1] )
points[2].extend( backWheel.points[2] )

frontWheel.create_points( 2, 12 )
points[0].extend( frontWheel.points[0] )
points[1].extend( frontWheel.points[1] )
points[2].extend( frontWheel.points[2] )

middleBar.create_points( 24, 6 )
points[0].extend( middleBar.points[0] )
points[1].extend( middleBar.points[1] )
points[2].extend( middleBar.points[2] )


inertia: Matrix = Matrix.null( 3, 3 )
inertia += paveBack.inertia()
inertia += paveFront.inertia()
inertia += roundBack.inertia()
inertia += roundFront.inertia()
inertia += roundMiddleBack.inertia()
inertia += roundMiddleFront.inertia()
inertia += backWheel.inertia()
inertia += frontWheel.inertia()
inertia += middleBar.inertia()


forces: list[ tuple[ Vector, Vector ] ] = [
    ( Vector( [ 0, 1, 0 ] ), Vector( [ 0, 0, 0 ] ) ),
    ( Vector( [ 0, 0, 10 ] ), Vector( [ 4, 0, 0 ] ) ),
    ( Vector( [ 0, 0, -10 ] ), Vector( [ -4, 0, 0 ] ) )
]

move( Matrix( [ *points ] ), inertia, forces, Vector.null(3), Vector.null(3), Vector.null(3), Vector.null(3), 1, 20, 50 )