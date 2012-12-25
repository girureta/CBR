

import cbr
import random
import math
import copy

import demo


def letterToCol(letter):
    letters=['a','b','c','d','e','f','g','h']
    
    n=0
    for l in letters:
        if letter==l:
            return n
        n=n+1
        
def catToInt(cat):
    categories=['draw','zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen']
    n=0
    for c in categories:
        if c==cat:
            return n
        n=n+1 


class ChessCase(cbr.Case):
    
    t=0
    
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
        int(fields[5]),
        catToInt(fields[6]),    
        ]
    
        self.data=v
        

def readChessData(name,data):   
    file = open(name, 'r')
    
    line= file.readline()
    
    while line != '':
        #print line
        data.append(line)
        line= file.readline()


#demo.numericalDemo()

m= ChessCase()

data=[]
readChessData('data/krkopt.data',data)

for da in data:
    c=ChessCase()
    c.setData(da)


print 'fin'