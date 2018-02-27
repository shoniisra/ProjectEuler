# Project Euler Problem 44: "Pentagon numbers"
# 
# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal
# numbers are:
# 
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# 
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48,
# is not pentagonal.
# 
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are
# pentagonal and D = |Pk - Pj| is minimised; what is the value of D?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import GetPentagonal, CheckIfPentagonal

D = 0
pairFound = False
k = 3
while pairFound == False:
	Pk = GetPentagonal(k)
	for j in range (k - 1, 1, -1):
		Pj = GetPentagonal(j)
		if CheckIfPentagonal(Pk - Pj) and CheckIfPentagonal(Pk + Pj):
			pairFound = True
			D = abs(Pk-Pj)
			break
	k += 1

print ("Smallest D = " + str(D))