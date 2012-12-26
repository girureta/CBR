

#import cbr
#import random
#import math
#import copy
#import demo


import chess


#demo.numericalDemo()

m= chess.ChessCase()

data=[]
chess.readChessData('data/krkopt.data',data)

for da in data:
    c=chess.ChessCase()
    c.setData(da)


print 'fin'