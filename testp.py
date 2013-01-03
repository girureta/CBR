import cbr
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
    
for c in train_set[:1000]:
    lib.addCase(c)
    



  
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
