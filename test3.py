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