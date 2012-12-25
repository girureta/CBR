'''
Created on 25/12/2012

@author: memo
'''

import cbr
import math
import random
import copy

def testfunc(x,y):
    return math.cos(x)+math.sin(y)

def testfunc2(x,y):
    return (x*x)+(y*y)

def demo(numSamples):
    print 'Generating '+str(numSamples)+' random cases'
    newCases = []
    for i in range(numSamples):
        tCase=cbr.Case()
        tCase.name='Case '+str(i)
        tCase.data=[random.uniform(-5,5),random.uniform(-5,5)]
        tCase.solution= testfunc(tCase.data[0],tCase.data[1])
        newCases.append(tCase)
    return newCases


def demoTest(numSamples):
    newCases = []
    a=-5
    b=10
    
    val=1.0/numSamples
    
    for i in range(numSamples):
        for j in range(numSamples):
            tCase=cbr.Case()
            tCase.name='Case '+str(i)
            tCase.data=[a+((i*val)*b),a+((j*val)*b)]
            tCase.solution= testfunc(tCase.data[0],tCase.data[1])
            newCases.append(tCase)
        
    return newCases

def dumpCases(fileName,cases):
    f=open(fileName,'w')
    
    for i in cases:
        f.write(str(i.data[0])+' '+str(i.data[1])+' '+str(i.solution)+'\n')
    f.close()

def dumpCases2(fileName,cases, numSamples):
    f=open(fileName,'w')
    
    num=1
    for i in cases:
        f.write(str(i.data[0])+' '+str(i.data[1])+' '+str(i.solution)+'\n')
        if num==numSamples:
            num=1
            f.write('\n')
        else:
            num=num+1
    f.close()
def numericalDemo():
    lLib=cbr.Library()
    lLib.cases=demo(1)
    
    testTarget=demoTest(20)
    test = []

    for i in testTarget:
        cC=copy.deepcopy(i)
        lLib.solveCase(cC)
        test.append(cC)
    
    print 'Lib contains '+str(len(lLib.cases))+' cases'
    
    dumpCases2('test',test,20)
    
    dumpCases2('testTarget',demoTest(20),20)
    