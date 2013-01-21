import chess

lib = chess.PlayCaseLib()
lib.readDatabaseFromTextFile('data/database')

print "Converting cases... \n"

i = 0

for case in lib.cases:
	case.convertCase()
	case.addToFile('data/symetricDB')
	i = i + 1
	if i > 400:
		print "."

print "\n ... conversion complete!"

