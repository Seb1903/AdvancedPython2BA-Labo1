# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math 
from cmath import sqrt
import scipy
import scipy.integrate as integrate2
import scipy.special as special

def fact(n):
	return math.factorial(n)

	
def roots(a, b, c):
	delta = b^2 - 4*a*c
	root1 = (-b + sqrt(delta))/(2*a)
	root2 = (-b - sqrt(delta))/(2*a)
	if root1 != root2 : 	
		if b==c==0 : 
			return 0 
		elif a == c == 0 : 
			return 0 
		return (root1, root2)
	elif root1 == root2 : 
		return (root1)
	else : 
		"il y a une erreur"


	

def integrate(function, lower, upper):
	resultat = integrate2.quad(lambda x : eval(function), lower, upper)
	return resultat[0]


if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
