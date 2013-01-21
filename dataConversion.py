import chess

data = chess.readChessData('data/krkopt.data')

cases = []
lib = chess.PlayLib()


for da in data:
    fields = da.split(",", 7)
    fields[6] = (fields[6])[0:-1]

    v = [chess.letterToCol(fields[0]), int(fields[1]),
         chess.letterToCol(fields[2]), int(fields[3]),
         chess.letterToCol(fields[4]), int(fields[5])]

    play = chess.Play(v, chess.catToInt(fields[6]))

    lib.addPlay(play)


N = len([p for p in lib.plays if p.depth > 0])
n = 0

print "Processing "+str(N)+" possible plays..." 


for currentPlay in lib.plays:

    if currentPlay.depth > 0:

        n += 1
        if n%50 == 0:
            print str(100*n/N) + "%..."

        legalPositionsInDB = []

        for checkedPlay in lib.plays:
            if currentPlay.checkForConsistenty(checkedPlay):
                legalPositionsInDB.append(checkedPlay)

        depth = 20
        movePlay = None

        for checkedPlay in legalPositionsInDB:
            if depth > checkedPlay.depth and checkedPlay.depth >= 0:
                depth = checkedPlay.depth
                movePlay = checkedPlay

        if (movePlay is not None) and (movePlay.depth < currentPlay.depth):
            currentCase = chess.PlayCase(currentPlay, movePlay)
            currentCase.addToFile('database')
