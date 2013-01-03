

import cbr
#import random
import math
#import copy
import demo


import chess


def mhd2d(p1,p2,q1,q2):
    return math.fabs(p1-q1)-math.fabs(p2-q2)

def getWKing(case):
    return [case.data[0],case.data[1]]

def getWRook(case):
    return [case.data[2],case.data[3]]

def getBKing(case):
    return [case.data[4],case.data[5]]

#demo.numericalDemo()

test=2

if test == 1:
    m= chess.ChessCase()
    
    lib = cbr.CaseLibrary()
    
    data=[]
    chess.readChessData('data/krkopt.data',data)
    
    for da in data:
        c=chess.ChessCase()
        c.setData(da)
    
    
    print 'fin'


if test == 2:
    m= chess.ChessCase()
    
    lib = cbr.CaseLibrary()
    
    data=[]
    chess.readChessData('data/krkopt.data',data)
    
    for da in data:
        c=chess.ChessCase()
        c.setData(da)
        
        lib.cases.append(c)
    
    
    print 'Num casos en la libreria: ',len(lib.cases)
    print 'Generando nuevo dataset'
    
    mejorJugada=cbr.Case()
    bestDepth=-9999
    nuevaJugada=cbr.Case()
    
    newFile=  open("data/newDataSet", 'w')
    for actual in lib.cases[:100]:
        for test in lib.cases[:1000]:
            if actual !=test:
                
                nuevaJugada.solution=None
                if mhd2d(actual.data[0],actual.data[1],test.data[0],test.data[1])==1 and (actual.data[2]!=test.data[2] or actual.data[3]!=actual.data[3]) :
                    nuevaJugada=test
                    
                if mhd2d(actual.data[0],actual.data[1],test.data[0],test.data[1])==0 and actual.data[2]==test.data[2] and actual.data[3]!=actual.data[3] :
                    nuevaJugada=test
                
                if mhd2d(actual.data[0],actual.data[1],test.data[0],test.data[1])==0 and actual.data[2]!=test.data[2] and actual.data[3]==actual.data[3] :
                    nuevaJugada=test
                    
                if nuevaJugada is not None and nuevaJugada.solution<bestDepth :
                    mejorJugada=nuevaJugada
                    bestDepth=nuevaJugada.solution
                
        newFile.write(str(actual.data[0])+","+str(actual.data[1])+","+str(actual.data[2])+","+str(actual.data[3])+","+str(actual.data[4])+","+str(actual.data[5])+","+str(nuevaJugada.data[0])+","+str(nuevaJugada.data[1])+","+str(nuevaJugada.data[2])+","+str(nuevaJugada.data[3])+","+str(nuevaJugada.data[4])+","+str(nuevaJugada.data[5])+'\n')
             
    newFile.close()
    print 'fin2'
    
