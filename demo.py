'''
Created on 25/12/2012

@author: memo
'''

import cbr
import utils

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
    
    utils.dumpCases2('test',test,20)
    
    utils.dumpCases2('testTarget',demoTest(20),20)
    