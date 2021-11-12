import numpy as np
import sympy as sp
import numpy.random

def xsample(n, a=0, b=1):
	return np.linspace(a,b,n)

def ysample(x,f,e=1):
	vector = []
	for i in x:
		vector.append([f(i)+(numpy.random.normal(0,1,1)[0])])
	vector = np.asarray(vector)	
	return vector	

def main():
	x = sp.symbols('s')
	def f(x): return 2*x
	print(xsample(8))
	print(ysample(xsample(5000),f))

main()
