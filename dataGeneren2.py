import numpy as np
import sympy as sp
import numpy.random

def xsample(n, a=0, b=1):
	vector = []
	v = numpy.random.normal(a,b,n)
	for i in v:
		vector.append([i]) 
	vector = np.asarray(vector)
	return vector


def ysample(x,f,e=1):
	vector = []
	for i in x:
		for j in i:
			vector.append([f(j)+(numpy.random.normal(0,1,1)[0])])
	vector = np.asarray(vector)	
	return vector	
def main():
	x = sp.symbols('s')
	def f(x): return 2*x
	print(xsample(8))
	print(ysample(xsample(50),f))

main()
