import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import numpy.random

def xsample(n, a=0, b=1):
	return np.linspace(a,b,n)

def ysample(x,f,e=1):
	vector = []
	for i in x:
		vector.append(f(i)+(numpy.random.normal(0,1,1)[0]))
	vector = np.asarray(vector)	
	return vector	

def ols(y,x):
	x_mean = np.mean(x)
	y_mean = np.mean(y)
	b = (sum((x-x_mean)*(y-y_mean)))/(sum((x-x_mean)**2))
	a = y_mean - b*x_mean
	def g(x): return a*x + b
	return (a,b)
	

def knn(x0, y, x,k):
    lenghtarray = []
    for i in range(len(x)):
        lenghtarray.append(abs(x[i] - x0))
        shortest = sorted(lenghtarray)[:k]
        value = np.mean(shortest)  #moeten nog werken met de indexen want y
    return value


def main():
    x = sp.symbols('s')
    def f(x): return 2*x
    print(ols(ysample(xsample(5),f),xsample(5)))
    print(knn(0.24534567,ysample(xsample(5),f),xsample(5),2))

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
