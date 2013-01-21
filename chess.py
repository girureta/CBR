import cbr
from copy import deepcopy
from random import choice
from numpy import argsort


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

    def __init__(self, positions, depth=None):
        self.data = positions
        self.depth = depth


    def __str__(self):
        L = 'White King: ' + self.readWKingPosition() + "; "
        L += 'White Rook: ' + self.readBKingPosition() + "; "
        L += 'Black King: ' + self.readWRookPosition()
        return L


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


    def readWKingPosition(self):
        return '(' + COLNAMES[self.WKingX()] + ',' + str(self.WKingY())+ ')'

    def readWRookPosition(self):
        return '(' + COLNAMES[self.WRookX()] + ',' + str(self.WRookY())+ ')'

    def readBKingPosition(self):
        return '(' + COLNAMES[self.BKingX()] + ',' + str(self.BKingY())+ ')'


    def strForStoring(self):
        L =  str(self.data[0]) + ',' + str(self.data[1]) + ','
        L += str(self.data[2]) + ',' + str(self.data[3]) + ','
        L += str(self.data[4]) + ',' + str(self.data[5]) + ','   
        L += str(self.data[6]) + ',' + str(self.data[7]) + ','     
        L += str(self.depth)
        return L


    def getSymmetricRepresentation(self):
        dat = [min(abs(9 - self.data.data[0]), self.data.data[0]), 
                                                # Distance to nearest side (X)
               min(abs(9 - self.data.data[1]), self.data.data[1]),
                                                # Distance to nearest side (Y)
               self.data.data[0] - self.data.data[2],     # Distance KB-KW (X)
               self.data.data[1] - self.data.data[3],     # Distance KB-KW (Y)
               self.data.data[0] - self.data.data[4],     # Distance KB-RW (X)
               self.data.data[1] - self.data.data[5],     # Distance KB-RW (Y)
               self.data.data[2] - self.data.data[4],     # Distance KW-RW (X)
               self.data.data[3] - self.data.data[5]      # Distance KW-RW (Y)
              ]
        return dat     


    def checkForConsistenty(self, checkedPlay):
        """ Checks if new checkedPlay is a possible configuration after
            a white player move starting from the current play
        """

        legalKingXMove = abs(self.WKingX() - checkedPlay.WKingX()) == 1
        legalKingYMove = abs(self.WKingY() - checkedPlay.WKingY()) == 1
        
        legalKingMove = legalKingYMove ^ legalKingXMove
        illegalKingMove = legalKingXMove and legalKingYMove

        changeRookX = self.WRookX() != checkedPlay.WRookX() 
        changeRookY = self.WRookY() != checkedPlay.WRookY() 

        legalRookMove = changeRookX ^ changeRookY
        illegalRookMove = changeRookY and changeRookY

        legalMove = ((legalRookMove ^ legalKingMove) and not
                        illegalRookMove and not illegalKingMove)

        coherentBlack = (self.BKingX() == checkedPlay.BKingX() and
                         self.BKingY() == checkedPlay.BKingY()) 

        if legalMove and coherentBlack:
            return True
        else:
            return False

    def getDepth(self):
        self.depth = askForDepthEvaluation()
        return self.depth



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
        """Converts the case in the symmetric form"""
        self.currentPlay.data = self.currentPlay.getSymmetricRepresentation()
        self.solution.data = self.solution.getSymmetricRepresentation()


    def NumericBoard(self):
        self.data[0] = letterToCol(self.data[0])
        self.data[2] = letterToCol(self.data[2])
        self.data[4] = letterToCol(self.data[4])
        self.data[6] = catToInt(self.data[6])
 
        self.solution[0] = letterToCol(self.solution[0])
        self.solution[2] = letterToCol(self.solution[2])
        self.solution[4] = letterToCol(self.solution[4])
        self.solution[6] = catToInt(self.solution[6])


    def setNearest(self, index, distance):
        self.kNN = index
        self.distances = distance


    def evaluateSolution(self):
        if self.currentPlay.depth is None or self.solution.depth is None:
            depthConsistency = self.solution.getDepth()
            if depthConsistency == None:
                return None
        else: 
            if self.currentPlay.depth > self.solution.depth:
                depthConsistency = 1
            else:
                depthConsistency = 0

        if self.currentPlay.checkForConsistenty(self.solution):
            playConsistency = 1
        else:
            playConsistency = 0

        return depthConsistency + playConsistency



class PlayCaseLib(cbr.CaseLibrary):
    
    def __init__(self, cases=[]):
        self.cases = cases
        

    def addCase(self, case):
        self.cases.append(case)


    def readDatabaseFromTextFile(self, filename):  

        f = open(filename, 'r')
        line = f.readline() 

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

        self.filename = filename


    def readSymDBFromTextFile(self, filename): 

        v = []
        f = open(filename, 'r')
        line = f.readline() 

        print 'Reading data....'

        while line != '':
            #Converts data in Numeric format
            fields = line.split(",")
            for i in fields:
                v.append(int(i))
            d = v.pop()
            currentProblemPlay = Play(v, d)
            v = []

            line = f.readline()
            fields = line.split(",")
            for i in fields:
                v.append(int(i))
            d = v.pop()
            currentSolutionPlay = Play(v,d)
            v = []

            currentCase = PlayCase(currentProblemPlay, currentSolutionPlay)
            self.addCase(currentCase)

            f.readline()
            line = f.readline()

        print '...done!\n'


    def KNN(self, K, newCase, W):
        dist = []
        for case in self.cases:
            dist.append(distance(case.currentPlay.data, 
                                                newCase.currentPlay.data, W))
        ind = argsort(dist)
        data = []
        for k in range(K):
            data.append(dist[ind[k]])
        newCase.setNearest(ind[0:K], data)


    def performRetrieval(self, newCase, k=1):
        W = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
        self.KNN(k,newCase,W)
        indices = newCase.kNN
        retrievedCases = [self.cases[x] for x in indices]

        return retrievedCases


    def solveCase(self, caseToSolve):
        retrievedCases = self.performRetrieval(caseToSolve, 4)
        problemPlay = caseToSolve.currentPlay
        method = askForMethod()
        adaptedSol = getAdaptedSolution(problemPlay, retrievedCases, method)
        return adaptedSol


    def storeCase(self, caseToStore):
        self.addCase(caseToStore)
        caseToStore.addToFile(self.filename)




def distance(caseData, newCaseData, W=None):
    
    if W is None:
        W = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]

    D = []
    DD = [] 
    
    for Dim in range(len(caseData)):
        dim = Dim - 1
        DD.append(abs(caseData[dim] - newCaseData[dim]))
        # print dim
        D.append(W[dim] * (abs(caseData[dim] - newCaseData[dim])))
    
    # similarity measure: sum of weighted distances + 
    #                    + penalization for moving the rock in diagonal + 
    #                    + penalization for moving the king more than 2 spaces

    sim = sum(D) + (W[8] * (DD[5] - DD[1]) * (DD[4] - DD[0]) + W[9] * 
                    (DD[2]) * (DD[2] - 1) + W[9] * (DD[3]) * (DD[3] - 1)) 

    return sim



def getAdaptedSolution(problemPlay, retrievedCases, method=3, consist=True):
    """ Adapts the retrieved cases to fit the case to solve given a method """

    if method == 0:
        solution = lazyAdaptation(problemPlay, retrievedCases, consist)
    elif method == 1:
        solution = adaptByLessDepth(retrievedCases, consist)
    elif method == 3:
        solution = adaptByAveraging(problemPlay, retrievedCases, consist)
    elif method >= 4:
        import extraAdaptationFunctions as extra
        solution = extra.adapt(problemPlay, retrievedCases, method)
        if solution is None:
            print "Method unknown, check the adaptation functions file!"
            consistency, method = askForMethod()

    return solution



def lazyAdaptation(problemPlay, retrievedCases, preserveConsistency=False):
    """ Do not perform adaptation (i.e. returns the first retrieved solution)
        unless preserveConsistency is True 
    """

    solution = retrievedCases[0].solution

    if preserveConsistency:
        solution = findClosestConsistentSolution(problemPlay, solution.data)
        solution = Play(solution)

    return solution



def adaptByLessDepth(retrievedCases, consistency=False):
    """ Returns the solution in retrievedCases with less depth"""

    if consistency:
        "Warning! This adaptation method no not preserve consistency!"

    best = float("inf")
    bestIndex = 0    
    
    ind = 0
    for sol in retrievedCases:
        if(sol.solution.depth < best):
            bestIndex = ind
            best = sol.solution.depth
        ind += 1

    return retrievedCases[bestIndex].solution



def adaptByAveraging(problemPlay, retrievedCases, preserveConsistency):
    """ Adapts a given problemPlay (of class Play) using averaging over a list
        of retrieved cases (of class PlayCase). Returns a solution Play.
    """

    k = len(retrievedCases)

    if k < 2:
        print "Warning! Averaging adaptation method is being used with k = 1"

    # Perform average:
    averagedFields = [0 for field in retrievedCases[0].currentPlay.data]
    
    d = len(averagedFields)

    for i in range(d):
        for case in retrievedCases:
            averagedFields[i] += (1/k) * case.currentPlay.data[i]

    if not preserveConsistency:
        return Play([int(round(field)) for field in fields])
    else:
        return findClosestConsistentSolution(problemPlay, averagedFields)



def findClosestConsistentSolution(problemPlay, fields):
    """ Finds the closest solution to a no integer fields list
        being consistent with the given problem.
        Fiels format: [WKingX, WKingY, WRookX, WRookY, BKingX, BKingY]
    """

    intFields = Play([int(round(field)) for field in fields])
    oF = problemPlay.data                           # original Fields

    if problemPlay.checkForConsistenty(intFields):
        return intFields

    # Generating candidates
    cands = [[oF[0] + 1, oF[1], oF[2], oF[3], oF[4], oF[5]],
             [oF[0] - 1, oF[1], oF[2], oF[3], oF[4], oF[5]],
             [oF[0], oF[1] + 1, oF[2], oF[3], oF[4], oF[5]],
             [oF[0], oF[1] - 1, oF[2], oF[3], oF[4], oF[5]],
             [[oF[0], oF[1], i, oF[3], oF[4], oF[5]] for i in range(1,9)],
             [[oF[0], oF[1], oF[2], i, oF[4], oF[5]] for i in range(1,9)]]

    # Filtering positions out of the domain
    cands = [c for c in cands if (c[0] < 9 and c[0] > 0)]
    cands = [c for c in cands if (c[1] < 9 and c[1] > 0)]


    minDist = float("inf")

    for c in cands:
        cDist = sum([abs(x - y) for x in intFields.data for y in c])
        if cDist < minDist:
            closerField = c
            minDist = cDist      

    return Play(closerField) 


def askForMethod():
    """ Ask the user for an adaptation method and returns it as an integer """

    print "\nPlease, choose an adaptation method (press enter for default):"
    print "   0: lazy adaptation - returns the most similar case solution"
    print "   1: less depth solution - returns the less deep of the closest"
    print "             solutions (does not admit force consistency)"
    print "   2: adapt by averaging - provides an average solution of the"
    print "             most similar cases"
    print "   3: use an user defined function (user defined functions can"
    print "             be added to the extraAdaptationFunctions.py file "
    print "\n"

    method = raw_input("Adaptation method (0-9): ")
    if method == '':
        return [True, 2]
    else:
        try:
            method = int(float(method))
        except:
            print "Invalid input, method should be an integer"
            method = None
        if method >= 0 and method < 10:
            return method
        else:
            print "Invalid input, method shold be a number between 0 and 9"

    if method == None:
        method = askForMethod()
        return method



def askForMethod():
    """ Ask the user for consistency keeping durign adaptation"""

    print "\nDo you want to restrict the adaptation only to coherent cases?"
    print "  Free adaptation is more general and can be used in other domains"
    print "\n"

    consistency = raw_input("Preserve consistency (y/n): ")
    if consistency == '':
        return [True, 2]
    elif consistency == 'y' or consistency == 'yes' or consistency == 'yap':
        return True
    elif consistency == 'n' or consistency == 'no' or consistency == 'nop':
        return False
    else:
        print "Invalid input, method shold be a number between 0 and 9"
        consistency = None

    if consistency == None:
        consistency = askForMethod()
        return consistency



def askForDepthEvaluation(play):
    """ Ask the user to evalue the depth (i.e. number of movement until 
        checkmate) of a play """
    print "Please, evalue the following play (blacks to move)"
    print play
    print "\n"
    
    depth = raw_input("Estimated depth (press enter for skip): ")

    if depth == '':
        return None
    else:
        try:
            depth = int(float(depth))
        except:
            print "Invalid input, depth should be an integer"
            depth = None
        if depth >= 0 and depth < 20:
            return depth
        else:
            print "Invalid input, depth shold be a number between 0 and 20"
