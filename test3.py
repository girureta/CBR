import cbr
import chess
from math import floor, ceil
from random import shuffle
from copy import deepcopy


print "--CBR Simulation--\n"
FLibFile = 'data/database'
RLibFile = 'data/symetricDB'

yoda = chess.CBRProcessor(FLibFile, RLibFile)

query = chess.Play([3, 4, 3, 6, 1, 1], 10)

yoda.performNewQuery(query)

print "Problem:", yoda.query, "\n"

# print "Welcome to 'Blabla Bla CBR Processor \n"
 
# cons = raw_input("First of all, you might like to tune some parameters \n is it so? \n (Default: No) \n")
# if cons == '' or  cons == 'n' or cons == 'no' or cons == 'nop':
#     print "Then, let's continue \n"
# elif cons == 'y' or cons == 'yes' or cons == 'yap':
#     yoda.setK(raw_input("Define the parameter K for a K-Nearest Neighbours selection \n (Enter for Default) \n"))
# else:
#     print "Invalid input, ansewer should be a Yes or No\n"

yoda.performRetrieval()

# print yoda.retrievedCases[1].currentPlay

# nretrieved = len(yoda.retrievedCases)
#print "Retrieved ", nretrieved, " cases. Distances:", yoda.retrievedDistances

# yoda.printRetrievedCases()

yoda.setAdaptationMethod(0)
yoda.setConsistencyPolicy(True)

yoda.adaptSolution()

#print "Solution: ", yoda.solution

yoda.finishCurrentQuery()

