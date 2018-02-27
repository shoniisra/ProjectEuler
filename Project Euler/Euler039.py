# Project Euler Problem 39: "Integer right triangles"
# 
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p <= 1000, is the number of solutions maximised?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import AreCoprimes

# Let's find primitive pythagorean triplets. Pythagorean triple, then so is
# (k*a, k*b, k*c) for any positive integer k.

# Euclid's formula[1] is a fundamental formula for generating Pythagorean triples given
# an arbitrary pair of integers m and n with m > n > 0. The formula states that the integers
# a = m^2 - n^2, b = 2*m*n, c = m^2 + n^2
# The triple generated by Euclid's formula is primitive if and only if m and n are coprime
# and not both odd.

maxPerimeter = 1000
solutionsPerPerimeter = [0]*(maxPerimeter + 1)

triplets = []
# The smallest primitive triplet is (3, 4, 5), when m = 2 and n = 1.
# When m = 22 and n = 1, perimeter is 1014. This gives us reasonable limits for m and n.
for m in range(2, 22):
	mIsOdd = (m % 2 != 0)
	for n in range(1, m):
		nIsOdd = (n % 2 != 0)
		if AreCoprimes(m, n):
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			
			p = a + b + c
			if mIsOdd & nIsOdd == 0:
				i = 1
				while True:
					if (p * i) <= maxPerimeter:
						if ([a*i, b*i, c*i] in triplets) == False:
							solutionsPerPerimeter[p*i] += 1
							triplets.append([a*i, b*i, c*i])
						i += 1
					else:
						break
			else:
				p //= 2
				if ([a, b, c] in triplets) == False:
					solutionsPerPerimeter[p] += 1
					triplets.append([a, b, c])


maxSolutions = max(solutionsPerPerimeter)
maxSolutionsIndex = solutionsPerPerimeter.index(max(solutionsPerPerimeter))
print ("Most solutions ("+ str(maxSolutions) + ") are for p = " + str(maxSolutionsIndex))