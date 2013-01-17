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
    
    xHigher1= case.WKingX()>1
    yHigher1= case.WKingY()>1
    
    xLower8= case.WKingX()<8
    yLower8= case.WKingY()<8
    
    
     
    if xHigher1:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()-1)
        plays.append(tempCase);
    
    if yHigher1:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingY(case.WKingY()-1)
        plays.append(tempCase);

    if xLower8:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()+1)
        plays.append(tempCase);

    if yLower8:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingY(case.WKingY()+1)
        plays.append(tempCase)

	#The king also moves to the corners :)
    if xHigher1 and yHigher1:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()-1)
        tempCase.SetWKingY(case.WKingY()-1)
        plays.append(tempCase)
        
    if xLower8 and yHigher1:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()+1)
        tempCase.SetWKingY(case.WKingY()-1)
        plays.append(tempCase)

    if xLower8 and yLower8:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()+1)
        tempCase.SetWKingY(case.WKingY()+1)
        plays.append(tempCase)

    if xHigher1 and yLower8:
        tempCase=copy.deepcopy(case)
        tempCase.SetWKingX(case.WKingX()-1)
        tempCase.SetWKingY(case.WKingY()-8)
        plays.append(tempCase)
         
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
