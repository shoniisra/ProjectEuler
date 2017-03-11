# Project Euler Problem 4: "Largest palindrome product"
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import benchmark

def IsPalindrome(number):
	palindromeFound = True
	numberString = str(number)
	length = len(numberString)
	for i in range (0, length//2):
		if numberString[i] != numberString[length - i - 1]:
			palindromeFound = False
			break
	return palindromeFound

largest = 0
largesta = 0
largestb = 0
valueRange = range (1000, 900, -1)
for a in valueRange:
	for b in valueRange:
		product = a*b
		if IsPalindrome(product) and (product > largest):
			largest = product
			largesta = a
			largestb = b

print ("Largest product is " + str(largesta) + " x " + str(largestb) + " = " + str(largest))