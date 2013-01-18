import cbr
import chess
from math import floor, ceil
from random import shuffle
from copy import deepcopy


print "--CBR Simulation--\n"


# --- DATA PROCESSING ---

lib = chess.PlayCaseLib()
lib.readDatabaseFromTextFile('data/database')

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
    
for c in testLib.cases[:10]:
    print "\n"

    print "Problem:", c.data.data, "with depth", c.data.depth
    print "Or.Move:", c.solution.data, "with depth", c.solution.depth

    solutionFound = c.solveCase(trainLib)
    print "--> Sol:", solutionFound.data, "with depth", solutionFound.depth
    
print '\n--Simulation Finished--\n'
