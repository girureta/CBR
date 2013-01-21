#<<<<<<< HEAD
from math import sqrt

#=======

import math
#>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
	
class Case:
	
	def __init__(self):
#<<<<<<< HEAD
		self.data = []
		self.name = ''
		self.solution = []

	def setData(self, d):
		self.data = d
	
	def f(self, x):
		print x

	def sim(self, cB):
		#if len(cB.data) != len(self.data):
		#	raise AssertionError('Data of different size')
		add = 0
		diff = 0
		for i in range(len(self.data)):
			diff = self.data[i] - cB.data[i]
			add = add + (diff * diff)
		
		return 1 / (1 + sqrt(add))
		
	def __str__(self):
#=======
		self.data=[]
		self.name=''
		self.solution=[]
	def setData(self,d):
		self.data=d
	
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
		
#>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
		return self.name
	
	def printData(self):
		print self.data
		

class CaseProcessor:
	#def __init__(self):
		
#<<<<<<< HEAD
	def transformSolution(self, newCase, oldCase):
		newCase.solution = oldCase.solution


class CaseLibrary:
	
	def __init__(self):
		self.cases = []
		self.processor = CaseProcessor()

	def retrieveCase(self, newCase):
		sim =- 1
		cCase = None

		for case in self.cases:
			nSim = newCase.sim(case)
			#print str(case),nSim
			if nSim > sim:
				sim = nSim
				cCase = case

		return cCase

	def solveCase(self, newCase):
		if self.processor is not None:
			oldCase = self.retrieveCase(newCase)
			self.processor.transformSolution(newCase, oldCase)
#=======
	def transformSolution(self,newCase,oldCase):
		newCase.solution=oldCase.solution

class CaseLibrary:
	
	
	
	def __init__(self):
		self.cases = []
		self.processor = CaseProcessor()
		
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
	
	def solveCase(self,newCase):
		if self.processor is not None:
			oldCase=self.retrieveCase(newCase)
			self.processor.transformSolution(newCase,oldCase)


	

#>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
