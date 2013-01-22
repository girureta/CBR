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
             'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
             'unknown': None}

DEPTH2CAT = {-1: 'draw', 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 
              4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 
              9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 
              13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 15: 'sixteen'}

BASE_W = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]



# Classes 
class Play():

    def __init__(self, positions, depth=None):
        """ Input for initialise: a list with the positions of the peaces 
              with ordering [WKingX, WKingY, WRookX, WRookY, BKingX, BKingY]
        """
        for p in positions:
            if p < 1 or p > 9:
                print "Warning: illegal position entered"

        self.data = positions
        self.depth = depth
        self.gauge = self.getGauge()

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
        L =  COLNAMES[self.data[0]] + ',' + str(self.data[1]) + ','
        L += COLNAMES[self.data[2]] + ',' + str(self.data[3]) + ','
        L += COLNAMES[self.data[4]] + ',' + str(self.data[5]) + ',' 
        if self.depth is None:
            L += "unknown"
        else:
            L += DEPTH2CAT[self.depth]
        return L

    def getReducedRepresentation(self):
        """ Returns an invariant-under-simmertries representation of the play
            as an ReducedPlay object
        """
        distToX = min(abs(9 - self.BKingX()), self.BKingX())
        distToY = min(abs(9 - self.BKingY()), self.BKingY())
        BKingWKingX = self.BKingX() - self.WKingX()
        BKingWKingY = self.BKingY() - self.WKingY()
        BKingWRookX = self.BKingX() - self.WRookX()
        BKingWRookY = self.BKingY() - self.WRookY()
        WKingWRookX = self.WKingX() - self.WRookX()
        WKingWRookY = self.WKingY() - self.WRookY()

        newData = [distToX, distToY, BKingWKingX, BKingWKingY, BKingWRookX, 
                BKingWRookY, WKingWRookX, WKingWRookY]

        return ReducedPlay(newData,self.depth)  

    def getGauge(self):
        """ Returns the gauge of the play, i.e. the necessearily information
            to revert a reducedRepresentation projection. The format is a
            tuple (x-corner, y-corner)
        """

        if self.BKingX() <= 4:
            gaugeX = 0
        else:
            gaugeX = 1

        if self.BKingY() <= 4:
            gaugeY = 0
        else:
            gaugeY = 1

        return (gaugeX, gaugeY)          

    def checkForConsistenty(self, checkedPlay):
        """ Checks if new checkedPlay is a possible configuration after
            a white players move starting from the current play
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



class ReducedPlay():

    def __init__(self, positions, depth=None):
        self.data = positions
        self.depth = depth

    def strForStoring(self):
        L =  str(self.data[0]) + ',' + str(self.data[1]) + ','
        L += str(self.data[2]) + ',' + str(self.data[3]) + ','
        L += str(self.data[4]) + ',' + str(self.data[5]) + ','   
        L += str(self.data[6]) + ',' + str(self.data[7]) + ','     
        L += str(self.depth)
        return L

    def distToX(self):
        return self.data[0]

    def distToY(self):
        return self.data[1]

    def BKingWKingX(self):
        return self.data[2]

    def BKingWKingY(self):
        return self.data[3]
    
    def BKingWRookX(self):
        return self.data[4]
    
    def BKingWRookY(self):
        return self.data[5]

    def WKingWRookX(self):
        return self.data[6]
    
    def WKingWRookY(self):
        return self.data[7]

    def strForStoring(self):
        L =  str(self.data[0]) + ',' + str(self.data[1]) + ','
        L += str(self.data[2]) + ',' + str(self.data[3]) + ','
        L += str(self.data[4]) + ',' + str(self.data[5]) + ',' 
        L += str(self.data[6]) + ',' + str(self.data[7]) + ',' 
        if self.depth is None:
            L += "unknown"
        else:
            L += DEPTH2CAT[self.depth]
        return L

    def projectOriginalRepresentation(self, gauge):
        """ Returns the plau in the original representation (Play object)"""
        if gauge[0] == 0:
            BKingX = self.distToX()
            BKingY = self.distToY()
        else:
            BKingX = 9 - self.distToX()
            BKingY = 9 - self.distToY()            

        WKingX = BKingX - self.BKingWKingX()
        WKingY = BKingY - self.BKingWKingY()
        WRookX = BKingX - self.BKingWRookX()
        WRookY = BKingY - self.BKingWRookY()

        convertedData = [BKingX, BKingY, WKingX, WKingY, WRookX, WRookY]

        return Play(convertedData,self.depth) 


class PlayCase():

    def __init__(self, play, solution):
        self.currentPlay = play
        self.solution = solution

    def __str__():
        pLit = "Problem: " + str(self.currentPlay)
        sLit = "Solution: " + str(self.solution)
        return pLit + "\n" + sLit

    def addToFile(self, filename):
        f = open(filename, 'a')
        f.write(self.currentPlay.strForStoring())
        f.write('\n')
        f.write(self.solution.strForStoring())
        f.write('\n\n')
        f.close()

    def getReducedRepresentation(self):
        rp = self.currentPlay.getReducedRepresentation()
        rc = self.solution.getReducedRepresentation()
        return ReducedPlayCase(rp, rc)



class ReducedPlayCase():

    def __init__(self, play, solution):
        self.currentPlay = play
        self.solution = solution

    def addToFile(self, filename):
        f = open(filename, 'a')
        f.write(self.currentPlay.strForStoring())
        f.write('\n')
        f.write(self.solution.strForStoring())
        f.write('\n\n')
        f.close()

    def projectOriginalRepresentation(self, gauge):
        """ Projects the case to the original representation (Case object)"""
        fPlay = self.currentPlay.projectOriginalRepresentation(gauge)
        fSol = self.solution.projectOriginalRepresentation(gauge) 
        return PlayCase(fPlay, fSol) 



class PlayCaseLib(cbr.CaseLibrary):
    
    def __init__(self, cases=[]):
        self.cases = cases

    def addCase(self, case):
        """ Adds the case to the lib. This function do not store the case in 
            a file. For that, storeCase() can be used.
        """
        self.cases.append(case)

    def readDatabaseFromTextFile(self, filename):  

        f = open(filename, 'r')
        line = f.readline() 

        print 'Reading data....'

        while line != '':

            fields = line.split(",", 7)

            v = [COLNUMBERS[fields[0]], int(fields[1]),
                 COLNUMBERS[fields[2]], int(fields[3]),
                 COLNUMBERS[fields[4]], int(fields[5])]

            fields[6] = (fields[6])[0:-1]               # Ignore '\n'

            d = DEPTH2NUM[fields[6]]

            currentProblemPlay = Play(v,d)

            line = f.readline()

            fields = line.split(",", 7)

            v = [COLNUMBERS[fields[0]], int(fields[1]),
                 COLNUMBERS[fields[2]], int(fields[3]),
                 COLNUMBERS[fields[4]], int(fields[5])]

            fields[6] = (fields[6])[0:-1]

            d = DEPTH2NUM[fields[6]]

            currentSolutionPlay = Play(v,d)

            c = PlayCase(currentProblemPlay, currentSolutionPlay)
            self.addCase(c)

            f.readline()
            line = f.readline()

        print '...done!\n'

        self.filename = filename

    def storeCase(self, caseToStore):
        """ Adds a case to the database and the database file"""
        self.addCase(caseToStore)
        caseToStore.addToFile(self.filename)



class ReducedPlayCaseLib(cbr.CaseLibrary):

    def __init__(self, cases=[]):
        self.cases = cases  

    def addCase(self, case):
        """ Adds the case to the lib. This function do not store the case in 
            a file. For that, storeCase() can be used.
        """
        self.cases.append(case)

    def readDatabaseFromTextFile(self, filename): 

        f = open(filename, 'r')
        line = f.readline() 

        print 'Reading data....'

        v = []

        while line != '':
            #Converts data in Numeric format
            fields = line.split(",")
            fields[8] = DEPTH2NUM[(fields[8])[0:-1]] 
            for i in fields:
                v.append(int(i))
            d = v.pop()
            currentProblemPlay = ReducedPlay(v, d)
            v = []

            line = f.readline()
            fields = line.split(",")
            fields[8] = DEPTH2NUM[(fields[8])[0:-1]] 
            for i in fields:
                v.append(int(i))
            d = v.pop()
            currentSolutionPlay = ReducedPlay(v,d)
            v = []

            c = ReducedPlayCase(currentProblemPlay, currentSolutionPlay)
            self.addCase(c)

            f.readline()
            line = f.readline()

        self.filename = filename

        print '...done!\n'

    def storeCase(self, caseToStore):
        """ Adds a case to the database and the database file"""
        self.addCase(caseToStore)
        caseToStore.addToFile(self.filename)



class CBRProcessor():

    def __init__(self, FullLibrary, ReducedLibrary):
        """ CBR Processor holds the main functions and heart of the CBR.
            Inputs are the databases of string with the paths of their files
        """

        if isinstance(FullLibrary,str):
            self.readFDatabaseFromFiles(FullLibrary)
        elif isinstance(FullLibrary,PlayCaseLib):
            self.FLib = FullLibrary
        else:
            print "Error: Full Library must be a PlayCaseLib object"

        if isinstance(ReducedLibrary,str):
            self.readRDatabaseFromFiles(ReducedLibrary)
        elif isinstance(ReducedLibrary,ReducedPlayCaseLib):
            self.RLib = ReducedLibrary
        else:
            print "Error: Reduced Library must be a PlayCaseLib object"

        self.solvedCasesCache = []
        self.heart = "Unicorns and other happy tender things"
        self.intialiseQueryVariables()
        self.setDefaultParameters()

    def __str__(self):
        print "CBR Processor:"
        print "    Main database filename: ", self.FLib.filename
        print "    Reduced database filename: ", self.RLib.filename
        print "    Actual Parameters: "
        print "                        k:", self.k 
        print "                  weights:", self.W 
        print "        adaptation method:", self.method
        print "       preserve coherence:", self.coherence
        print "    Solved cases in cache:", self.solvedCasesCache, "\n"

    def intialiseQueryVariables(self):
        """ Cleans the query-specific parameters """
        self.query = None
        self.retrievedCases = []
        self.retrievedDistances = []
        self.solution = None
        self.evaluation = None

    def setDefaultParameters(self):
        """ Set the CBR parameters to default """
        self.k = 3
        self.W = BASE_W
        self.method = 2
        self.coherence = True

    def readFDatabaseFromFiles(self, FullLibraryFile):
        self.FLib = PlayCaseLib()
        self.FLib.readDatabaseFromTextFile(FullLibraryFile)

    def readRDatabaseFromFiles(self, ReducedLibraryFile):
        self.RLib = ReducedPlayCaseLib()
        self.RLib.readDatabaseFromTextFile(ReducedLibraryFile)  

    def getHeart(self):
        """ Returns the heart of the CBR"""
        return self.heart

    def performNewQuery(self, query):
        """ Adds a new current problem to the CBR Processor. If there is 
            already a defined current problem it will be overwritten.
                Input: a Play object describing the problem. Depth is optional
        """
        if isinstance(query, Play):
            self.query = query
            self.retrievedCases = []
            self.retrievedDistances = []
        else:
            print "Error: Query must be an object of class Play"

    def setK(self, k):
        """ Sets the k parameter of the kNN for the retrieval"""

        if self.retrievedCases != [] and len(self.retrievedCases) != k:
            print "Warning: changing the k once retrieval is performed"
            print "Unexpected results may occur. Please, repeat retrieval"
            print "with the new parameters before starting adaptation phase"

        self.k = k

    def setWeights(self, W):
        """ Sets the weight vector for the weighted kNN during retrieval"""
        if len(W) != len(BASE_W):
            print "Error: lenth of weights vector should be", len(BASE_W)
        else:
            self.W = W

    def setAdaptationMethod(self, method):
        """ Sets the adaptatio method used by the system. Options are:
                0: lazy adaptation - returns the most similar case solution
                1: less depth solution - returns the less deep of the closest
                        solutions (does not admit force consistency)
                2: adapt by averaging - provides an average solution of the
                        most similar cases
                3-9: use an user defined function (user defined functions can
                        be added to the extraAdaptationFunctions.py file
        """

        if isinstance(method, int):
            if method >= 0 and method < 10:
                self.method = method
            else:
                print "Invalid input, method should be an int between 0 and 9"
        else:
            print "Invalid input, method should be an integer"

    def setConsistencyPolicy(self, consistency):
        """ Sets the consistency policy of the CBR. When True, only consistent
            solutions can be obtained from the adaptation system. This
            restriction is highly domain dependent, so it can be deactivated
        """
        if isinstance(consistency, bool):
            self.consistency = consistency
        else:
            print "Invalid input, consistency should be a True/False constant"

    def askForConsistency(self):
        """ Ask the user for consistency keeping durign adaptation"""

        print "\n"
        print "Do you want to restrict the adaptation only to coherent cases?"
        print "Free adaptation is more general: can be used in other domains"
        print "\n"

        cons = raw_input("Preserve consistency? (y/n): ")
        if cons == '':
            return [True, 2]
        elif cons == 'y' or cons == 'yes' or cons == 'yap':
            return True
        elif cons == 'n' or cons == 'no' or cons == 'nop':
            return False
        else:
            print "Invalid input, consistency should be a True/False constant"

        if cons is None:
            self.consistency = askForMethod()

    def askForMethod(self):
        """ Ask the user for an adaptation method """

        print "\nPlease, choose an adaptation method (enter for default: 2):"
        print "   0: lazy adaptation - returns the most similar case solution"
        print "   1: less depth solution - returns the less deep of the"
        print "             closest solutions (does not admit consistency)"
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
                self.method = method
            else:
                print "Invalid input, method shold be a number between 0 and 9"

        if method is None:
            method = askForMethod()
            self.method = method

    def solveQuery(self, query, saveResultsIntoDabase=False):
        """ Solves a new query performing the whole CBR cycle"""
        self.performNewQuery(query)
        self.performRetrieval()
        self.adaptSolution()
        self.evaluateSolution()

        results = [self.solution, self.evaluation]

        self.finishCurrentQuery()

        if saveResultsIntoDabase:
            self.saveCache()

        return results

    def performRetrieval(self):
        """ Performs the retrieval using the parameters of the CBR. Retrieved 
            cases and their distances to the query are stored in the object.
        """ 
        print "Retrieving similar cases..."

        kNNIndices, self.retrievedDistances = self.kNN()

        gauge = self.query.gauge

        rC = [self.RLib.cases[x].projectOriginalRepresentation(gauge)
                 for x in kNNIndices]

        self.retrievedCases = rC

    def kNN(self):
        """ Finds the k Nearest Neighbors of the query Case in the library 
            using the weight vector W to compute the distance.
            Returns a list of the k indices of the cases and their distances.
        """
        qdata = self.query.getReducedRepresentation()   # data from query

        dist = [self.distance(case.currentPlay.data, qdata.data) 
                     for case in self.RLib.cases]

        kNNIndices = argsort(dist)[0:self.k]

        distances = [dist[kNNIndices[k]] for k in range(self.k)]

        return [kNNIndices, distances]

    def distance(self, c1, c2):
        """ Finds weighted distance between cases c1 and c2 (reduced rep.)"""
    
        if len(c1) == len(c2):
            dimension = len(c1)
        else:
            print "Wrong input, cases need to have the same dimension!"
            return None

        # Component wise Manhattan distance
        dist = [abs(c1[i] - c2[i]) for i in range(dimension)]
        # Component wise weighted Manhattan distance
        wDist = [self.W[i] * dist[i] for i in range(dimension)]
        
        totalWManhattan = sum(wDist)
        # Penalization for moving the rock in diagonal
        diagRookMoving = (dist[5] - dist[1]) * (dist[4] - dist[0])
        # Penalization for moving the king more than 2 spaces
        kingMoreThan2 = dist[2] * (dist[2] - 1) + dist[3] * (dist[3] - 1)

        distance = (totalWManhattan + 
                    self.W[8] * diagRookMoving + 
                    self.W[9] * kingMoreThan2)

        return distance

    def printRetrievedCases(self):
        """ Prints the retrievedCases in full-representation """
        i = 1
        for case in self.retrievedCases:
            print "Retrieved case #" + str(i)
            print "    Problem:", case.currentPlay
            print "    Solution;", case.solution, '\n'
            i += 1

    def adaptSolution(self):
        """ Uses retrieved cases to construct a solution for the query """
        print "Adapting solution space..."
        if self.method == 0:
            print "    Adaptation method: Lazy Adaptation"
            self.lazyAdaptation()

        elif self.method == 1:
            print "    Adaptation method: Less-depth Solution"
            self.adaptByLessDepth()

        elif self.method == 2:
            print "    Adaptation method: Adapt by Averaging"
            self.adaptByAveraging()

        elif self.method >= 3:
            try:
                import extraAdaptationFunctions as extra
            except:
                print "There is some problems with the adaptation functions"
                print "extra library. Please, check the file."

            print "Adaptation method: User defined"
            solution = extra.adapt(self.query, self.retrievedCases,
                                             self.method, self.consistency)

            if self.solution is None:
                print "Method not defined. Please, check definitions in"
                print "the adaptation functions file!" 
                print "In the meanwhile, you can select another method."
                method = self.askForMethod()
                consistency = self.askForConsistency()
            else:
                self.solution = solution

        print "   ...done!\n"

    def lazyAdaptation(self):
        """ Do not perform adaptation (i.e. sets as solution the solution of 
            the first retrieved case). Very lazy indeed. 
        """
        self.solution = self.retrievedCases[0].solution
        if self.coherence:
            self.moveSolutionToClosestConsistent()

    def adaptByLessDepth(self):
        """ Sets the solution stored in retrieved cases with less depth
            (i.e. the most optimal from the point of view of the problem) 
            as the problem solution.
        """

        best = float("inf")
        bestIndex = 0    
        
        i = 0
        for c in self.retrievedCases:
            if c.solution.depth is not None and c.solution.depth < best:
                bestIndex = i
                best = c.solution.depth
            i += 1

        if best == float("inf"):
            print "No listed solution with defined depth!"
            print "Please, choose another method and try again"
        else:
            self.solution = self.retrievedCases[bestIndex].solution
            if self.coherence:
               self.moveSolutionToClosestConsistent()

    def adaptByAveraging(self):
        """ Adapts the solution using averaging weighted by distance
            over the retrieved cases """

        if self.k < 2:
            print "Warning! Averaging method is being used with k = 1!"

        rc = self.retrievedCases

        # Initialising averagedFields:
        averagedFields = [0 for field in rc[0].solution.data]
        dimension = len(averagedFields)

        # Computing weights:
        maxDistance = max(self.retrievedDistances)
        similarities = [maxDistance - d + 1 for d in self.retrievedDistances]
        w = [s/sum(similarities) for s in similarities]

        for i in range(dimension):
            for j in range(len(rc)):
                averagedFields[i] += w[j] * rc[j].solution.data[i]

        if not self.coherence:
            self.solution = Play([int(round(field)) for field in fields])
        else:
            self.solution = self.findClosestConsSolution(averagedFields)

    def moveSolutionToClosestConsistent(self):
        """ Sets the (manhattan) closest solution to the one in the system """
        """ If solution is already consistent, depth is preserved"""

        if self.solution is None:
            print "Error: no solution have been computed yet!"
        elif not self.query.checkForConsistenty(self.solution):
            self.solution = self.findClosestConsSolution(self.solution.data)

    def findClosestConsSolution(self,fields):
        """ Returns the (manhattan) closest solution to a non necessearily
            integer fields list being consistent with the given query.
            Fiels format: [WKingX, WKingY, WRookX, WRookY, BKingX, BKingY]
        """

        intFields = Play([int(round(field)) for field in fields])
        qF = self.query.data                           # query Fields

        if self.query.checkForConsistenty(intFields):
            return Play(intFields)

        print "        Forcing consistency over the found solution..."

        # Generating candidates
        #         WKingX   WKingY   WRook(x,y)    BKing(x,y)
        cands = [[qF[0] + 1, qF[1], qF[2], qF[3], qF[4], qF[5]],
                 [qF[0] - 1, qF[1], qF[2], qF[3], qF[4], qF[5]],
                 [qF[0], qF[1] + 1, qF[2], qF[3], qF[4], qF[5]],
                 [qF[0], qF[1] - 1, qF[2], qF[3], qF[4], qF[5]],
                 [[qF[0], qF[1], i, qF[3], qF[4], qF[5]] for i in range(1,9)],
                 [[qF[0], qF[1], qF[2], i, qF[4], qF[5]] for i in range(1,9)]]

        # Filtering positions out of the domain
        cands = [c for c in cands if (c[0] < 9 and c[0] > 0)]
        cands = [c for c in cands if (c[1] < 9 and c[1] > 0)]
    
        # Filtering current position (white must move)
        cands = [c for c in cands if c != qF]

        # Initialising minimum distance
        minDist = float("inf")

        for c in cands:
            cDist = sum([abs(x - y) for x in intFields.data for y in c])
            if cDist < minDist:
                closerField = c
                minDist = cDist    

        return Play(closerField) 

    def askForDepthEvaluation(self):
        """ Ask the user to evalue the depth (i.e. number of movement until 
            checkmate) of a proposed solution """
        print "\nPlease, evalue the following play (blacks to move):\n"
        print self.solution
        
        depth = raw_input("--> Estimated depth (press enter for skip): ")
        print ""

        if depth != '':
            try:
                depth = int(float(depth))
            except:
                print "Invalid input, depth should be an integer"
                self.askForDepthEvaluation()
            if depth >= 0 and depth <= 20:
                self.solution.depth = depth
            else:
                print"Invalid input, depth shold be a number between 0 and 20"
                self.askForDepthEvaluation()

    def askForEvaluation(self):
        """ Ask the user to evaluate the solution of the system and returns
            its choice
        """

        if self.solution is None:
            print "No solution found to be evaluated"
            return None

        print "The introduced problem was:"
        print self.query
        print "Please, evalue the following solution proposed by the system:"
        print self.solution
        print "\n"
        print "Evaluation should be a number between 0 and 1. The system will"
        print "add the case to the database if the evaluation is over 0.7"

        if self.evaluation != None:
            print "Current evaluation of the solution:", self.evaluation
        
        evaluation = raw_input("--> Evaluation result (press enter to skip):")

        if evaluation != '':
            try:
                evaluation = float(depth)
            except:
                print "Invalid input, evaluation should be a number!"
                self.askForEvaluation()
            if evaluation >= 0 and evaluation <= 1:
                return evaluation
            else:
                print"Invalid input, evaluation shold be between 0 and 1"
                self.askForDepthEvaluation()

    def evaluateSolution(self, askEvaluation=False, askDepth=True):
        """ Performs evaluation of the solution stored in the system"""

        print "Evaluating Solution..."

        if self.solution is None:
            print "No solution found to be evaluated"
            return None

        if askEvaluation:
            evaluationResult = self.askForEvaluation()
            if evaluationResult is not None:
                self.evaluation = evaluationResult
                return None

        if self.query.depth is None:
            depthConsistency = None
        else:
            if self.solution.depth is None and askDepth:
                self.askForDepthEvaluation() 
            if self.solution.depth is None:
                depthConsistency = None
            else:
                if self.query.depth > self.solution.depth:
                    depthConsistency = 1
                else:
                    depthConsistency = 0

        if self.query.checkForConsistenty(self.solution):
            playConsistency = 1
        else:
            playConsistency = 0

        if depthConsistency is None:
            print "\n Warning: Depth-consistency cannot be evalued \n"
            depthConsistency = 0

        evaluationResult = 0.5 * (depthConsistency + playConsistency)

        self.evaluation = evaluationResult

    def finishCurrentQuery(self, askEvaluation=False, askDepth=True):
        """ Terminates the current query. If a solution is defined, it is 
            evaluated and returned. If evaluation perform is over 0.5, the 
            solution is, in addition, added to the cache database.
        """
        if self.solution != None and self.evaluation == None:
            e = self.evaluateSolution(askEvaluation, askDepth)
            self.evaluation = e

        print "Query terminated ------"
        print "    Introduced Query:", self.query

        if self.solution != None:
            self.evaluateSolution(askEvaluation, askDepth)

            print "    Proposed Solution:", self.solution
            print "    Quality of solution:", str(self.evaluation)+"/1.0"

            if self.evaluation != None:
                print "    Evaluation of the result:",round(self.evaluation,2)            
                if self.evaluation >= 0.7:
                    finalCase = PlayCase(self.query, self.solution)
                    self.solvedCasesCache.append(finalCase)
                    print ""
                    print "Case was stored in cache. Please, remember to save" 
                    print "the changes before close the system to permanently"
                    print "add the stored cases to the database."

        print "------------------------"
        print " \n\nPlease, add a new query to start again."

        self.intialiseQueryVariables()

    def saveCache(self):
        """ Adds cases in cache to the permanent database files """
        while self.solvedCasesCache != []:
            case = self.solvedCasesCache.pop()
            rcase = case.getReducedRepresentation()
            self.FLib.storeCase(case)
            self.RLib.storeCase(rcase)