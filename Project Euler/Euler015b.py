# Project Euler Problem 15: "Lattice paths"
# 
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20x20 grid?

import sys
sys.path.insert(0, './Utils')
import benchmark

# Project Euler has the capability to make you feel stupid.
# It appears that my first notion that the valid routes can be presented in binary with exact
# number of ones and zeros is actually the fastest solution there is. I just did not know how to
# represent the concept mathematically. In Problem 15 overview PDF the solution is represented
# as combinatorial product sequence PI(i=1 -> n)(n+1)/i. This solves the problem in 0.8 ms.
# Into the shame box you go, I say to myself.

gridDimension = 20

print ("Calculating routes for " + str(gridDimension) + "x" + str(gridDimension) + " grid.")
routes = 1
for i in range (1, gridDimension + 1):
	routes = routes*(gridDimension + i)/i

print (str(routes) + " routes found.")