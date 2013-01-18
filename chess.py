#<<<<<<< HEAD
import cbr
from copy import deepcopy
from random import choice


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
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # n = 1
    # for l in letters:
    #     if letter == l:
    #         return n
    #     n += 1


def catToInt(cat):
    return DEPTH2NUM[cat]
    # categories = ['draw', 'zero', 'one', 'two', 'three', 'four', 'five', 
    #               'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    #               'thirteen', 'fourteen', 'fifteen', 'sixteen']
    # n = -1
    # for c in categories:
    #     if c == cat:
    #         return n
    #     n+=1 


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

#=======
'''
Created on 26/12/2012

@author: memo
'''


import cbr
import copy

def letterToCol(letter):
    letters=['a','b','c','d','e','f','g','h']
    
    n=1
    for l in letters:
        if letter==l:
            return n
        n=n+1
        
def catToInt(cat):
    categories=['draw','zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen']
    n=-1
    for c in categories:
        if c==cat:
            return n
        n=n+1 


class ChessCase(cbr.Case):

  

    
    #d is a string
    def setData(self,d):
        
        
        fields=d.split(",",7)

        
        #ignore '\n'
        fields[6]=(fields[6])[0:-1]
        
        
        v=[
        letterToCol(fields[0]),
        int(fields[1]),
        letterToCol(fields[2]),
        int(fields[3]),
        letterToCol(fields[4]),
        int(fields[5])
        ]
    
        self.data=v
        self.solution=catToInt(fields[6])
        
#>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
    def WKingX(self):
        return self.data[0]

    def WKingY(self):
        return self.data[1]

    def WRookX(self):
        return self.data[2]

    def WRookY(self):
        return self.data[3]
    
    def BKingX(self):
        return self.data[4]
    
    def BKingY(self):
        return self.data[5]
#<<<<<<< HEAD

    def setWKingX(self, val):
        self.data[0] = val

    def setWKingY(self, val):
        self.data[1] = val

    def setWRookX(self, val):
        self.data[2] = val

    def setWRookY(self, val):
        self.data[3] = val
    
    def setBKingX(self, val):
        self.data[4] = val
    
    def setBKingY(self, val):
        self.data[5] = val

    def readWKingPosition(self):
        return '(' + COLNAMES[self.WKingX()] + ',' + str(self.WKingY())+ ')'

    def readWRookPosition(self):
        return '(' + COLNAMES[self.WRookX()] + ',' + str(self.WRookY())+ ')'

    def readBKingPosition(self):
        return '(' + COLNAMES[self.BKingX()] + ',' + str(self.BKingY())+ ')'

    def __str__(self):
        L = 'White King: ' + self.readWKingPosition() + "; "
        L += 'White Rook: ' + self.readBKingPosition() + "; "
        L += 'Black King: ' + self.readWRookPosition()
        return L

    def strForStoring(self):
        L =  COLNAMES[self.BKingX()] + ',' + str(self.BKingY()) + ','
        L += COLNAMES[self.WRookX()] + ',' + str(self.WRookY()) +','
        L += COLNAMES[self.BKingX()] + ',' + str(self.BKingY()) + ','
        L += DEPTH2CAT[self.depth]
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
        self.data = play
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

    def solveCase(self, caseLib):
        retrievedCases = performRetrieval(self, caseLib)
        adaptedCaseSolution = getAdaptedSolution(self, retrievedCases)
 
        return adaptedCaseSolution
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


# class ChessCase(cbr.Case):

#     # d is a string
#     def setData(self, d):
        
#         fields = d.split(",", 7)
#         fields[6] = (fields[6])[0:-1]          # Ignore '\n'
        
#         v = [letterToCol(fields[0]),
#              int(fields[1]),
#              letterToCol(fields[2]),
#              int(fields[3]),
#              letterToCol(fields[4]),
#              int(fields[5])]
    
#         self.data = v
#         self.solution = catToInt(fields[6])

#     def WKingX(self):
#         return self.data[0]

#     def WKingY(self):
#         return self.data[1]

#     def WRookX(self):
#         return self.data[2]

#     def WRookY(self):
#         return self.data[3]
    
#     def BKingX(self):
#         return self.data[4]
    
#     def BKingY(self):
#         return self.data[5]
  
#     #Setters  
#     def SetWKingX(self, val):
#         self.data[0] = val

#     def SetWKingY(self, val):
#         self.data[1] = val

#     def SetWRookX(self, val):
#         self.data[2] = val

#     def SetWRookY(self, val):
#         self.data[3] = val
    
#     def SetBKingX(self, val):
#         self.data[4] = val
    
#     def SetBKingY(self, val):
#         self.data[5] = val


# class ChessCaseProcessor(cbr.CaseProcessor):
    
#     def transformSolution(self, newCase, plays):
#         bestPlay = ChessCase
#         best =- 99999
        
#         for p in plays:
#             if p.solution > best:
#                 bestPlay = p
#                 best = p.solution

#         newCase.solution = bestPlay.solution
#         newCase.data = bestPlay.data


# class ChessCaseLibrary(cbr.CaseLibrary):
    
#     def __init__(self):
#         self.cases = []
#         self.processor = ChessCaseProcessor()
        
#     def addCase(self, case):
#         self.cases.append(case)
        
#     def solveCase(self, newCase):
#         if self.processor is not None:
            
#             # Get possible plays from this state
#             plays = []
#             getValidPlays(newCase,plays)
#             oldCases = []
            
#             # For each allowed play in plays get the most similar case 
#             for p in plays: 
#                 # retrieveCase from base class
#                 oldCases.append(self.retrieveCase(p))
               
#             # Assigns to each new play the depth of the most similar case
#             for i in range(len(plays)):
#                 plays[i].solution = oldCases[i].solution

#             self.processor.transformSolution(newCase, plays)
    

# def getValidPlays(case, plays):
        
#     tempCase = ChessCase()

#     # White king
#     xHigher1 = case.WKingX() > 1
#     yHigher1 = case.WKingY() > 1
#     xLower8 = case.WKingX() < 8
#     yLower8 = case.WKingY() < 8     
     
#     if xHigher1:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingX(case.WKingX() - 1)
#         plays.append(tempCase)
    
#     if yHigher1:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingY(case.WKingY() - 1)
#         plays.append(tempCase)

#     if xLower8:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingX(case.WKingX() + 1)
#         plays.append(tempCase) 

#     if yLower8:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingY(case.WKingY() + 1)
#         plays.append(tempCase)

# 	# The king also moves to the corners :)
#     if xHigher1 and yHigher1:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingX(case.WKingX() - 1)
#         tempCase.SetWKingY(case.WKingY() - 1)
#         plays.append(tempCase)
        
#     if xLower8 and yHigher1:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingX(case.WKingX() + 1)
#         tempCase.SetWKingY(case.WKingY() - 1)
#         plays.append(tempCase)

#     if xLower8 and yLower8:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingX(case.WKingX() + 1)
#         tempCase.SetWKingY(case.WKingY() + 1)
#         plays.append(tempCase)

#     if xHigher1 and yLower8:
#         tempCase = deepcopy(case)
#         tempCase.SetWKingX(case.WKingX() - 1)
#         tempCase.SetWKingY(case.WKingY() - 8)
#         plays.append(tempCase)
         
#     # RookY
#     for i in range(1, 9):
#         xRook = case.WRookX()
#         yRook = case.WRookY()
                 
#         if ((case.WKingX() != xRook or case.WKingY() != i) and 
#                 (case.WKingX() != xRook or case.WKingY() != i) and 
#                 (i != yRook )):
#             tempCase = deepcopy(case)
#             tempCase.SetWRookY(i)
#             plays.append(tempCase)
            
#         if ((case.WKingX() != i or case.WKingY() != yRook) and 
#                 (case.WKingX() != i or case.WKingY() != xRook) and 
#                 (i != xRook)):
#             tempCase = deepcopy(case)
#             tempCase.SetWRookX(i)
#             plays.append(tempCase)
        
#     #for j in range(1,8):
            

# def readChessData(name, data=None):
#     if data is None:
#         data = []
#         dataNonGiven = True

#     file = open(name, 'r')
    
#     line = file.readline()
    
#     while line != '':
#         #print line
#         data.append(line)
#         line = file.readline()

#     if dataNonGiven:
#         return data


def performRetrieval(self, caseLib, k=1):
    cases = []
    for i in range(k):
        cases.append(choice(caseLib.cases))
    return cases


def getAdaptedSolution(self, retrievedCases):
    return retrievedCases[0].solution





#=======
  
    #Setters  
    def SetWKingX(self,val):
        self.data[0]=val

    def SetWKingY(self,val):
        self.data[1]=val

    def SetWRookX(self,val):
        self.data[2]=val

    def SetWRookY(self,val):
        self.data[3]=val
    
    def SetBKingX(self,val):
        self.data[4]=val
    
    def SetBKingY(self,val):
        self.data[5]=val


class ChessCaseProcessor(cbr.CaseProcessor):
    
    def transformSolution(self,newCase,plays):
        
        
        bestPlay=ChessCase
        best=-99999
        
        for p in plays:
            if p.solution>best:
                bestPlay=p
                best=p.solution
                
                 
        newCase.solution=bestPlay.solution
        newCase.data=bestPlay.data


class ChessCaseLibrary(cbr.CaseLibrary):
    
    def __init__(self):
        self.cases = []
        self.processor = ChessCaseProcessor()
        
        
    def addCase(self,case):
        self.cases.append(case)
        
    def solveCase(self,newCase):
        if self.processor is not None:
            
            #get possible plays from this state
            
            plays=[]
            
            getValidPlays(newCase,plays)
            
            oldCases=[]
            
            
            #por cada jugada posible consiguo el caso mas parecido
            for p in plays: 
                
                #Este retrieveCase es de la clase base
                oldCases.append(self.retrieveCase(p))
                

            # a cada nueva jugada le asigno el depth del mejor caso parecido
            for i in range(0,len(plays)):
                plays[i].solution=oldCases[i].solution

            self.processor.transformSolution(newCase,plays)
    
def getValidPlays(case,plays):
    
    
    tempCase=ChessCase()
    #white king
    
    if case.WKingX()>1:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()-1)
        plays.append(tempCase);
    
    if case.WKingY()>1:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingY(case.WKingY()-1)
        plays.append(tempCase);

    if case.WKingX()<8:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()+1)
        plays.append(tempCase);

    if case.WKingY()<8:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingY(case.WKingY()+1)
        plays.append(tempCase);
        
    #RookY
    for i in range(1,9):
        xRook=case.WRookX()
        yRook=case.WRookY()
        
        
        if (case.WKingX()!=xRook or case.WKingY()!=i) and (case.WKingX()!=xRook or case.WKingY()!=i) and (i!=yRook ):
            tempCase=copy.deepcopy(case)
            tempCase.SetWRookY(i)
            plays.append(tempCase)
            
        if (case.WKingX()!=i or case.WKingY()!=yRook) and (case.WKingX()!=i or case.WKingY()!=xRook) and (i!=xRook):
            tempCase=copy.deepcopy(case)
            tempCase.SetWRookX(i)
            plays.append(tempCase)
        
    #for j in range(1,8):
            
    

def readChessData(name,data):   
    file = open(name, 'r')
    
    line= file.readline()
    
    while line != '':
        #print line
        data.append(line)
        line= file.readline()
#>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
