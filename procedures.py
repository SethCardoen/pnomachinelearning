import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import numpy.random

def xsample(n, a=0, b=1):
	return np.linspace(a,b,n)

def ysample(x,f,e=1):
	vector = []
	for i in x:
		vector.append(f(i)+(numpy.random.normal(0,1,e)[0]))
	vector = np.asarray(vector)	
	return vector	

def ols(y,x):

    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    b= (sum((x-x_mean)*(y-y_mean))) / (sum((x-x_mean)**2))

    a = y_mean - b*x_mean

    def g(x): return b*x + a
    return (b,a)

def knn(x0, y, x,k):
    lenghtarray = []
    for i in range(len(x)):
        lenghtarray.append(abs(x[i] - x0))
       
    shortest = sorted(lenghtarray)[:k]

    K = []
    for item in shortest:
        K.append(lenghtarray.index(item)) 
        # K = lijst met indexen voor dichtste punten
     
    y = 1/k * sum(y[K])
    
    #value = np.mean(shortest) moeten nog werken met de indexen want y (wordt momenteel niet gebruikt)
    
    return y

def olsPlot(y, x, p=0, q=1):
	(a,b) = ols(y, x)
	def g(x): return a*x + b
	yy = g(x)
    
	plt.figure()
	plt.scatter(x,y, color='r', s = 3)
	plt.title("ols")
	plt.plot(x,yy)
	plt.show()

def knnPlot(y, x,k,a=0, b=1):
	x0waardes = np.linspace(a,b,300)
	yy = []
    
	for x0 in x0waardes:
		yy.append(knn(x0, y, x,k))
        
	plt.figure()
	plt.scatter(x,y, color='r', s = 3)
	plt.title("KNN met K =" + str(k))
	plt.plot(x0waardes,yy)
	plt.show()

def main():
    x = sp.symbols('s')
    def f(x): return 2*x

    xs = xsample(15)
    ys = ysample(xs, f)

    #print(ols(ys,xs))
    olsPlot(ys, xs)
    knnPlot(ys,xs,3)

if __name__ == "__main__":
   	main()
