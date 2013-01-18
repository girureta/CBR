import cbr
import chess
from math import floor, ceil
from random import shuffle
from copy import deepcopy


print "--CBR Simulation--\n"


# --- DATA PROCESSING ---

lib = chess.PlayCaseLib()
#lib.readDatabaseFromTextFile('data/database')
lib.readSymDBFromTextFile('data/symetricDB')

# Split data into training/testing sets
testSplit = 0.7;
sizeDataSet = len(lib.cases)

a = int(floor(sizeDataSet * testSplit))
b = int(ceil(sizeDataSet * testSplit))

print "Training set size:", a
print "Test set size:", sizeDataSet - b
print "\n"

caseSet = deepcopy(lib.cases)
shuffle(caseSet)

trainLib = chess.PlayCaseLib(caseSet[:a])
testLib =  chess.PlayCaseLib(caseSet[b:])    

# --- TESTING CBR ---
print "Some Examples: "
K=5
for c in testLib.cases[:1]:
    print "\n"

    print "Problem:", c.data.data, "with depth", c.data.depth
    print "Or.Move:", c.solution.data, "with depth", c.solution.depth

    # solutionFound = c.solveCase(trainLib)
    # print "--> Sol:", solutionFound.data, "with depth", solutionFound.depth
    W=[1, #Distance to Nearest Border X
    	1, #Distance to Nearest Border Y
    	1, #Distance BK-WK X
    	1, #Distance BK-WK Y
    	1, #Distance BK-WR X
    	1, #Distance BK-WR Y
    	1, #Distance WK-WR X
    	1, #Distance WK-WR Y
    	0, #Penalization: Rock displaced in diagonal
    	0] #Penalization: King moved more than one space
    trainLib.KNN(K,c,W)
    print "asd", c.kNN
    
print '\n--Simulation Finished--\n'
