import cbr
from copy import deepcopy
from random import choice
import numpy


# Global constants
COLNUMBERS = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

COLNAMES = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'} 

DEPTH2NUM = {'draw': -1, 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 
             'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 
             'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 
             'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16}

DEPTH2CAT = {-1: 'draw', 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 
              4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 
              9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 
              13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 15: 'sixteen'}
 

def letterToCol(letter):
    return COLNUMBERS[letter]
   
def catToInt(cat):
    return DEPTH2NUM[cat]

class Play():
    """ Class for plays in the King VS King + Rook context.
        Input for initialise: a list with the positions of the peaces in order
                              [WKingX, WKingY, WRookX, WRookY, BKingX, BKingY]
    """

    def __init__(self, positions, depth):
        self.data = positions
        self.depth = depth

    def strForStoring(self):
        L =  str(self.data[0]) + ',' + str(self.data[1]) + ','
        L += str(self.data[2]) + ',' + str(self.data[3]) +','
        L += str(self.data[4]) + ',' + str(self.data[5]) +','   
        L += str(self.data[6]) + ',' + str(self.data[7]) +','     
        L += str(self.depth)
        return L


class PlayLib():

    def __init__(self):
        self.plays = []

    def addPlay(self, play):
        self.plays.append(play)

    def __str__(self):
        L = ''
        for play in plays:
            L += str(play) + '\n'

        return L


class PlayCase():

    def __init__(self, play, solution):
        self.currentPlay = play
        self.solution = solution

    def getQuality(self):
        return self.solution.depth()

    def addToFile(self, filename):
        f = open(filename, 'a')
        f.write(self.data.strForStoring())
        f.write('\n')
        f.write(self.solution.strForStoring())
        f.write('\n\n')
        f.close()

    def convertCase(self):
        #Converts the case in the symmetric form
        dat=[]
        dat.append(min(abs(9-self.data.data[0]),self.data.data[0])) #Distance to nearest side (X)
        dat.append(min(abs(9-self.data.data[1]),self.data.data[1])) #Distance to nearest side (Y)
        dat.append(self.data.data[0]-self.data.data[2]) #Distance KB-KW (X)
        dat.append(self.data.data[1]-self.data.data[3]) #Distance KB-KW (Y)
        dat.append(self.data.data[0]-self.data.data[4]) #Distance KB-RW (X)
        dat.append(self.data.data[1]-self.data.data[5]) #Distance KB-RW (Y)
        dat.append(self.data.data[2]-self.data.data[4]) #Distance KW-RW (X)
        dat.append(self.data.data[3]-self.data.data[5]) #Distance KW-RW (Y)
        self.data.data=dat

        sol=[]
        sol.append(min(abs(9-self.solution.data[0]),self.solution.data[0])) #Distance to nearest side (X)
        sol.append(min(abs(9-self.solution.data[1]),self.solution.data[1])) #Distance to nearest side (Y)
        sol.append(self.solution.data[0]-self.solution.data[2]) #Distance KB-KW (X)
        sol.append(self.solution.data[1]-self.solution.data[3]) #Distance KB-KW (Y)
        sol.append(self.solution.data[0]-self.solution.data[4]) #Distance KB-RW (X)
        sol.append(self.solution.data[1]-self.solution.data[5]) #Distance KB-RW (Y)
        sol.append(self.solution.data[2]-self.solution.data[4]) #Distance KW-RW (X)
        sol.append(self.solution.data[3]-self.solution.data[5]) #Distance KW-RW (Y)
        self.solution.data=sol

    def NumericBoard(self):
        a=self.data
        self.data[0]=letterToCol(a[0])
        self.data[2]=letterToCol(self.data[2])
        self.data[4]=letterToCol(self.data[4])
        self.data[6]=catToInt(self.data[6])

        self.solution[0]=letterToCol(self.solution[0])
        self.solution[2]=letterToCol(self.solution[2])
        self.solution[4]=letterToCol(self.solution[4])
        self.solution[6]=catToInt(self.solution[6])

    def setNearest(self,index,distance):
        self.kNN=index
        self.distances=distance



class PlayCaseLib(cbr.CaseLibrary):
    
    def __init__(self, cases=[]):
        self.cases = cases
        
    def addCase(self, case):
        self.cases.append(case)

    def readDatabaseFromTextFile(self, filename):  

        f = open(filename, 'r')
        lastLineReaded = line = f.readline() 

        print 'Reading data....'

        while line != '':
            #Converts data in Numeric format
            fields = line.split(",", 7)
            v = [letterToCol(fields[0]), int(fields[1]),
                 letterToCol(fields[2]), int(fields[3]),
                 letterToCol(fields[4]), int(fields[5])]
            fields[6] = (fields[6])[0:-1]               # Ignore '\n'
            d = catToInt(fields[6])

            currentProblemPlay = Play(v,d)

            line = f.readline()
            fields = line.split(",", 7)
            v = [letterToCol(fields[0]), int(fields[1]),
                 letterToCol(fields[2]), int(fields[3]),
                 letterToCol(fields[4]), int(fields[5])]
            fields[6] = (fields[6])[0:-1]
            d = catToInt(fields[6])

            currentSolutionPlay = Play(v,d)

            currentCase = PlayCase(currentProblemPlay, currentSolutionPlay)
            self.addCase(currentCase)

            f.readline()
            line = f.readline()

        print '...done!\n'
    def readSymDBFromTextFile(self, filename): 
        v=[]
        f = open(filename, 'r')
        lastLineReaded = line = f.readline() 

        print 'Reading data....'

        while line != '':
            #Converts data in Numeric format
            fields = line.split(",")
            for i in fields:
                v.append(int(i))
            d=v.pop()
            currentProblemPlay = Play(v,d)
            v=[]

            line = f.readline()
            fields = line.split(",")
            for i in fields:
                v.append(int(i))
            d=v.pop()
            currentSolutionPlay = Play(v,d)
            v=[]

            currentCase = PlayCase(currentProblemPlay, currentSolutionPlay)
            self.addCase(currentCase)

            f.readline()
            line = f.readline()
        print '...done!\n'
    def solveCase(self, newCase):
        retrievedCases = self.performRetrieval(newCase)
        adaptedCaseSolution = getAdaptedSolution(retrievedCases)
 
        return adaptedCaseSolution

    def KNN(self,K,newCase,W):
        dist=[]

        for case in self.cases:
            dist.append(distance(case.currentPlay,newCase.currentPlay,W))
        ind=numpy.argsort(dist)
        #print ind
        data=[]
        for k in range(K):
            data.append(dist[ind[k]])
        newCase.setNearest(ind[0:K],data)
        
    def performRetrieval(self, newCase, k=1):
        W=[1,1,1,1,1,1,1,1,0,0]
        self.KNN(k,newCase,W)
        indices=newCase.kNN
        retrievedCases= [self.cases[x] for x in indices]

        return retrievedCases

def distance(case, newCase, W):
        D=[]
        DD=[]
        for Dim in range(len(case.data)):
            dim=Dim-1
            DD.append(abs(case.data[dim]-newCase.data[dim]))
            D.append(W[dim]*(abs(case.data[dim]-newCase.data[dim])))
        sim=sum(D)+W[8]*(DD[5]-DD[1])*(DD[4]-DD[0])+W[9]*(DD[2])*(DD[2]-1)+W[9]*(DD[3])*(DD[3]-1) #similarity measure: sum of weighted distances + penalization for moving the rock in diagonal + penalization for moving the king more than 2 spaces

        return sim






def getAdaptedSolution(retrievedCases):
    return retrievedCases[0].solution



