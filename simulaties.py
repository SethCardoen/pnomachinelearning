from procedures import *
import sympy as sp

def sim1():
	# functie simulatie 1
	x = sp.symbols('x')
	def f(x): return 10 ** x

	# genereer 20 punten aan de hand van xsample en ysample
	xs = xsample(20)
	ys = ysample(xs, f)

	# plot grafieken
	olsPlot(ys, xs)
	knnPlot(ys, xs, 1) # K 1
	knnPlot(ys, xs, 5) # K 5
	knnPlot(ys, xs, 20) # K 20

sim1()
