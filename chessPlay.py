
import os
import chess


def clear():
    os.system('clear')

def getRow():
    
    input = raw_input('Please enter a row (1 to 8): ')
    
    val=-1
    try:
        val = int(input)
        
        if val < 1 or val > 8:
            print 'The value is out of range'
            val=-1
        
    except ValueError:
        print("The entered value is not an integer")
    
    return val
        
def getColumn():

    input = raw_input('Please enter a column (1 to 8): ')
    
    val=-1
    try:
        val = int(input)
        
        if val < 1 or val > 8:
            print 'The value is out of range'
            val=-1
        
    except ValueError:
        print("The entered value is not an integer")
    
    return val
    

def getPosition(message):
    a=0
    b=0
    
    print 'Enter the position of the ',message
    
    res=-1
    
    while res==-1:
        res=getRow()
        print res
        
    a=res
    
    res=-1
    while res==-1:
        res=getColumn()
        
    b=res
    
    return a,b
    
def getPlay(p):
    
    p[0],p[1] = getPosition('Black king')
    p[2],p[3] = getPosition('White king')
    p[4],p[5] = getPosition('White rock')
    
def getkNN(yoda):
    cons = raw_input("First of all, you might like to tune some parameters \n is it so? \n (Default: No) \n")
    if cons == '' or  cons == 'n' or cons == 'no' or cons == 'nop':
        print "Then, let's continue. \n"
    elif cons == 'y' or cons == 'yes' or cons == 'yap':
        key=raw_input("Define the parameter K for a K-Nearest Neighbours selection \n (Enter for Default) \n")
        try:
            key = int(float(key))
        except:
            if key == '':
                print "K set as default\n"
                key=yoda.k
            else:
                print "Invalid input, K should be an integer"
                print "K set as default\n"
                key=yoda.k
        if key<1:
            print "Invalid input, K should be greater than 0"
            print "K set as default\n"
            key=yoda.k
        print yoda.k
        yoda.setK(key)


        key=raw_input("Define the vector W of k-Nearest Neigbours' weights\n Please, enter 10 positive values separated by comas. \n(Enter for Default) \n")
        try:
            key = [int(float(key[i])) for i in range(10)]
        except:
            if key == '':
                print "W set as default\n"
                key=yoda.W
            else:
                print "Invalid input, W is a list of ten positive values separated by comas"
                print "W set as default\n"
                key=yoda.W
        if key>0:
            yoda.setK(key)
        else:
            print "Invalid input, K should be greater than 0"
            print "K set as default"



    else:
        print "Invalid input, ansewer should be a Yes or No\n"
    
    
