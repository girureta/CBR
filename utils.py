def dumpCases(fileName, cases):
    f = open(fileName, 'w')
    
    for i in cases:
        f.write(str(i.data[0]) + ' ' + str(i.data[1]) + ' ' + 
                str(i.solution) + '\n')
    f.close()


def dumpCases2(fileName, cases, numSamples):
    f = open(fileName, 'w')
    
    num = 1
    for i in cases:
        f.write(str(i.data[0]) + ' ' + str(i.data[1]) + ' ' + 
                str(i.solution) + '\n') 
        if num == numSamples:
            num = 1
            f.write('\n')
        else:
            num = num + 1

    f.close()