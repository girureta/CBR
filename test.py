import cbr
import chess
from math import floor, ceil
from random import shuffle
from copy import deepcopy


print "--CBR Simulation--\n"
FLibFile = 'data/database'
RLibFile = 'data/symetricDB'

yoda = chess.CBRProcessor(FLibFile, RLibFile)

yoda.setAdaptationMethod(0)

query = chess.Play([3, 4, 3, 6, 1, 1], 10)

r = yoda.solveQuery(query, True)
print r[0]

# print "Welcome to 'Blabla Bla CBR Processor \n"
 
# cons = raw_input("First of all, you might like to tune some parameters \n is it so? \n (Default: No) \n")
# if cons == '' or  cons == 'n' or cons == 'no' or cons == 'nop':
#     print "Then, let's continue \n"
# elif cons == 'y' or cons == 'yes' or cons == 'yap':
#     yoda.setK(raw_input("Define the parameter K for a K-Nearest Neighbours selection \n (Enter for Default) \n"))
# else:
#     print "Invalid input, ansewer should be a Yes or No\n"

print yoda.solvedCasesCache
