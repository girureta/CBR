import cbr
import chess
from math import floor, ceil
from random import shuffle
from copy import deepcopy


print "--CBR Simulation--\n"


# --- DATA PROCESSING ---

lib = chess.PlayCaseLib()

lib.readSymDBFromTextFile('data/symetricDB')

# Split data into training/testing sets
testSplit = 0.7;
sizeDataSet = len(lib.cases)

a = int(floor(sizeDataSet * testSplit))
b = int(ceil(sizeDataSet * testSplit))

print "Training set size:", a
print "Test set size:", sizeDataSet - b
print "\n"


#caseSet = deepcopy(lib.cases)
caseSet = lib.cases

#lib is no longer needed
lib.cases = None
del(lib)

shuffle(caseSet)
trainLib = chess.PlayCaseLib(caseSet[:a])
testLib = chess.PlayCaseLib(caseSet[b:])    


# --- TESTING CBR ---
print "Some Examples: "

for c in testLib.cases[:1]:
    print "\n"

    print "CurrentPlay:", c.currentPlay.data, "with depth", c.currentPlay.depth
    print "Solution:", c.solution.data, "with depth", c.solution.depth

    W=[1,       # Distance to Nearest Border X
       1,       # Distance to Nearest Border Y
       1,       # Distance BK-WK X
       1,       # Distance BK-WK Y
       1,       # Distance BK-WR X
       1,       # Distance BK-WR Y
       1,       # Distance WK-WR X
       1,       # Distance WK-WR Y
       0,       # Penalization: Rock displaced in diagonal
       0]       # Penalization: King moved more than one space

    sol = trainLib.solveCase(c)
 
    print 'Proposed solution:', sol.data, "with depth", sol.depth
    
print '\n--Simulation Finished--\n'
