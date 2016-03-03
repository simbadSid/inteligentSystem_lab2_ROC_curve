from ProblemInstance import ProblemInstance
from util import *
import matplotlib.pyplot as plt
import math
from cupshelpers.ppds import normalize





def buildROC(pbInstance, discriminant, truePositiveRate, falsePositiveRate):
    count       = 0
    # List of the scalar product W.X for each feature X
    observationPositive = pbInstance.computeObservationList(discriminant, True)
    observationNegative = pbInstance.computeObservationList(discriminant, False)
    for bias in pbInstance.getBiasList():
        nbrPositive         = 0.
        nbrNegative         = 0.
        nbrTruePositive     = 0.
        nbrFalsePositive    = 0.
        for sample in xrange(pbInstance.getNbrPositiveSample()):
            biasedObservation = observationPositive[sample] + bias
            if (biasedObservation <= 0):
                nbrNegative += 1
            else:
                nbrPositive += 1
                nbrTruePositive += 1

        for sample in xrange(pbInstance.getNbrNegativeSample()):
            biasedObservation = observationNegative[sample] + bias
            if (biasedObservation <= 0):
                nbrNegative += 1
            else:
                nbrPositive += 1
                nbrFalsePositive += 1

        print "Nbr positive       = " + str(nbrPositive)
        print "Nbr negative       = " + str(nbrNegative)
        print "Nbr true positive  = " + str(nbrTruePositive)
        print "Nbr false positive = " + str(nbrFalsePositive)
        if ((nbrPositive > 0) and (nbrNegative > 0)):
            truePositiveRate[count]     = nbrTruePositive / nbrPositive
            falsePositiveRate[count]    = nbrFalsePositive / nbrNegative
            print "True positive Rate = " + str(truePositiveRate[count])
            print "False positive Rate= " + str(falsePositiveRate[count])
            count += 1
        else:
            print "Unprinted point"
        print "---------------------------------"
    for i in range(count, len(pbInstance.getBiasList())):
        truePositiveRate[i]     = None
        falsePositiveRate[i]    = None

def printROC(falsePositiveRate, truePositiveRate, discriminant):
    plt.plot(falsePositiveRate, truePositiveRate, 'bo-', label='ROC curve with discriminant =  ' + str(discriminant))
    plt.grid()
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.legend()
    plt.show()

def printBiasList(pbInstance):
    axis = [i for i in xrange(pbInstance.getNbrBias())]

    plt.plot(axis, pbInstance.getBiasList(), 'bo-', label='List of bias used for the simulation')
    plt.grid()
    plt.xlabel('Simulation')
    plt.ylabel('Bias value')
    plt.legend()
    plt.show()


def plotSampleAndDiscriminant(pbInstance, discriminant):
    positiveSample = pbInstance.getPositiveSample()
    negativeSample = pbInstance.getNegativeSample()
    plt.plot(positiveSample[0], positiveSample[1], 'g^', label='Positive samples')
    plt.plot(negativeSample[0], negativeSample[1], 'bo',  label='Negative samples')
    
    ###### TODO print discriminant
    discriminantVector = pickVectorPoint(discriminant, x0=-1, x1=5)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    
    
    pbInstance      = ProblemInstance()
    pbInstance.parseProblemInstance(normalizeData=False, normalizeDiscriminent=True)

    plt.figure()
    printBiasList(pbInstance)

    for discriminant in pbInstance.discriminantFunction:
        plotSampleAndDiscriminant(pbInstance, discriminant)
        truePositiveRate    = [0 for i in xrange(pbInstance.getNbrBias())]
        falsePositiveRate   = [0 for i in xrange(pbInstance.getNbrBias())]
        buildROC(pbInstance, discriminant, truePositiveRate, falsePositiveRate)
        printROC(falsePositiveRate, truePositiveRate, discriminant)
        print "*********************************************"



