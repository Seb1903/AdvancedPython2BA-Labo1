# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math 
import scipy
import scipy.integrate as integrate
import scipy.special as special

def fact(n):
	return math.factorial(n)

	
def roots(a, b, c):
	delta = b^2 - 4*a*c
	if delta >= 0 :
		root1 = (-b + math.sqrt(delta))/2*a
		root2 = (-b - math.sqrt(delta))/2*a
		if root1 != root2 : 
			return (root1, root2)
		if root1 == root2 : 
			return (root1)
	if delta < 0 : 
		pass
	

def integrate(function, lower, upper):
	resultat = integrate.quad(lambda x : eval(function), lower, upper)
	return resultat


if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
