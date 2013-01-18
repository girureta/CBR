import cbr
<<<<<<< HEAD
from math import floor, ceil
import chess


print "CBR Simulation \n"


# --- DATA PROCESSING ---

data = []

# Read the dataset
chess.readChessData('data/krkopt.data', data)

lib = cbr.CaseLibrary()

# Transform the dataset into CBR cases
cases = []

for da in data:
    c = chess.ChessCase()
    c.setData(da)
    cases.append(c)

# Split data into training/testing sets
testSplit = 0.7;
sizeDataSet = len(cases)

a = int(floor(sizeDataSet * testSplit))
b = int(ceil(sizeDataSet * testSplit))

print "train set size:", a
print "test set size:", sizeDataSet - b
print "\n"

train_set = cases[:a]
test_set = cases[b:]    


# --- TRAINING CBR ---

train_set = [c for c in train_set if c.solution > -1]    # Filter draw games

lib = chess.ChessCaseLibrary()
=======
import math
import chess





data=[]

#lee el dataset
chess.readChessData('data/krkopt.data',data)

lib = cbr.CaseLibrary()

#convierte el dataset a casos
cases=[]
for da in data:
    c=chess.ChessCase()
    c.setData(da)
    cases.append(c)
    
       

#split data
testSplit=0.7;
    
sizeDataSet=len(cases)

#split data
testSplit=0.7;
    
sizeDataSet=len(cases)

a=int(math.floor(sizeDataSet*testSplit))
b=int(math.ceil(sizeDataSet*testSplit))

print "train set ",a
print "test set ",sizeDataSet-b


train_set = cases[:a]
test_set = cases[b:]    
#################
    
    
    
    
#agregando casos de entrenamiento

#filter draw games
train_set = [c for c in train_set if c.solution > -1]

lib=chess.ChessCaseLibrary()
>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
    
for c in train_set[:1000]:
    lib.addCase(c)
    

<<<<<<< HEAD
# --- TESTING CBR ---
print "Some Examples: "
    
for c in test_set[:10]:
    print "\n"

    print "Original:", c.data, c.solution
    best = c.solution
    c.solution = -666
    
    lib.solveCase(c)
    print "New:", c.data, c.solution
    print "Difference: ", best - c.solution
    
print '\nSimulation Finished\n'
=======


  
#Probando
    
for c in test_set[:10]:
        
    
    print "------"
    
    print "original", c.data,c.solution
    best=c.solution
    c.solution=-666
    
    lib.solveCase(c)
    print "new", c.data,c.solution
    print "diferencia: ",best-c.solution
    
    
    
print 'fin3'
>>>>>>> e3fde2adb51347911bac896f0e2f69891eacd1e4
