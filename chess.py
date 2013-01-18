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


def performRetrieval(self, caseLib, k=1):
    cases = []
    for i in range(k):
        cases.append(choice(caseLib.cases))
    return cases


def getAdaptedSolution(self, retrievedCases):
    return retrievedCases[0].solution
