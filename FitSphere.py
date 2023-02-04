""" 
This code runs in Rhino 8, thanks to RhinoCode. NOT in Rhino 7.
Inputs:
	- Points = List of Points3d
Output:
	- Center = Center of the sphere (Point3d)
	- Radius = Radius of the sphere (Double)
"""

# requirements: numpy

#  Import packages
import numpy as np
import math as m
import Rhino.Geometry as rg

#  Creation of X, Y and Z values arrays.
ptsX = [pt.X for pt in Points]
ptsY = [pt.Y for pt in Points]
ptsZ = [pt.Z for pt in Points]

#  SphereFit definition
def sphereFit(spX, spY, spZ):

    #   Assemble the A matrix
    spX = np.array(spX)
    spY = np.array(spY)
    spZ = np.array(spZ)
    A = np.zeros((len(spX), 4))
    A[:, 0] = spX * 2
    A[:, 1] = spY * 2
    A[:, 2] = spZ * 2
    A[:, 3] = 1

    #   Assemble the f matrix
    f = np.zeros((len(spX), 1))
    f[:, 0] = (spX * spX) + (spY * spY) + (spZ * spZ)
    C, residules, rank, singval = np.linalg.lstsq(A, f)

    #   solve for the radius
    t = (C[0] * C[0]) + (C[1] * C[1]) + (C[2] * C[2]) + C[3]
    radius = np.sqrt(t)

    return radius, C[0], C[1], C[2]


Radius, X, Y, Z = sphereFit(ptsX, ptsY, ptsZ)

Center = rg.Point3d(X[0], Y[0], Z[0])
