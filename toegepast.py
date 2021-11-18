from procedures import *

def main():
	x = sp.symbols('x')
	def f(x): return 2*x
	
	xs = xsample(15)
	ys = ysample(xs, f)
	
	olsPlot(ys, xs)
	knnPlot(ys, xs, 3)

main()
