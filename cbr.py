
import math
	
class Case:
	
	def __init__(self):
		self.data=[]
		self.name=''
		self.solution=[]
	
	def f(self,x):
		print x

	def sim(self,cB):
		#if len(cB.data)!=len(self.data):
		#	raise AssertionError('Data of different size')
		add=0
		diff=0
		for i in range(len(self.data)):
			diff=self.data[i]-cB.data[i]
			add=add+(diff*diff)
		
		return 1/(1+math.sqrt(add))
		
	def __str__(self):
		
		return self.name
		

class Library:
	
	def __init__(self):
		self.cases = []
		
	def retrieveCase(self,newCase):
		sim=-1
		cCase= None
		for case in self.cases:
			nSim=newCase.sim(case)
			#print str(case),nSim
			if nSim>sim:
				sim=nSim
				cCase=case
		return cCase
	
	def transformSolution(self,newCase,oldCase):
		newCase.solution=oldCase.solution
	
	def solveCase(self,newCase):
		oldCase=self.retrieveCase(newCase)
		self.transformSolution(newCase,oldCase)
