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
caseSet=lib.cases

#lib is no longer needed
lib.cases=None
del(lib)

shuffle(caseSet)
trainLib = chess.PlayCaseLib(caseSet[:a])
testLib =  chess.PlayCaseLib(caseSet[b:])    

# --- TESTING CBR ---
print "Some Examples: "
K=5
total=0
repeated=0
for c in testLib.cases:


    sol=trainLib.solveCase(c)

    #print c.currentPlay.data,' ',sol.data
    total+=c.currentPlay.depth
    total-=sol.depth
    
    if c.currentPlay.data==sol.data:
        repeated+=1 
    #print 'The solution is, ',sol.data,' ',sol.depth
    
print 'total-> ',total
print 'repeated-> ',repeated
print '\n--Simulation Finished--\n'
