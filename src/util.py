import os
import math



DEFAULT_COMMENT = "#"



def isEndOfFile(file):
    return (file.tell() == os.fstat(file.fileno()).st_size)

def nextMeaningLine(file, commentString=DEFAULT_COMMENT):
    while (not isEndOfFile(file)):
        res = file.readline().strip()
        if (res.startswith(commentString)):
            continue
        elif (res == "\n" or res == ""):
            continue
        else:
            return res
    raise Exception("No usefull string found in the file " + file.name)

def vectorLength(vector):
    res = 0
    for i in xrange(len(vector)):
        res += math.pow(vector[i], 2)
    return math.sqrt(res)


def lowestValue(a, b):
    if (a < b):
        return a
    else:
        return b

def biggestValue(a, b):
    if (a > b):
        return a
    else:
        return b

# build a list with a linear progression from the min to the max
def buildLinearList(min, max, nbrElem):
    res     = [0.0 for i in xrange(nbrElem)]
    min     = min
    max     = max
    delta   = (float(max) - float(min) + 1.) / float(nbrElem)
    for i in xrange(nbrElem/2):
        res[i]              = min
        res[nbrElem-i-1]    = max
        max                 -= delta
        min                 += delta
    return res

