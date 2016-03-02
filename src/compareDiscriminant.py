from ProblemInstance import ProblemInstance
import matplotlib.pyplot as plt
import math
from cupshelpers.ppds import normalize





def buildROC(pbInstance, discriminant, truePositiveRate, falsePositiveRate):
    count       = 0
    # List of the scalar product W.X for each feature X
    observation = pbInstance.computeObservationList(discriminant)
    for bias in pbInstance.getBiasList():
        nbrPositive         = 0.
        nbrNegative         = 0.
        nbrTruePositive     = 0.
        nbrFalsePositive    = 0.
        for sample in xrange(pbInstance.getNbrSample()):
            biasedObservation   = observation[sample] + bias
            realValue           = pbInstance.getTrainingSampleValue(sample)
            if (biasedObservation <= 0):
                nbrNegative += 1
            else:
                nbrPositive += 1
                if (realValue * biasedObservation > 0):
                    nbrTruePositive += 1
                else:
                    nbrFalsePositive+= 1
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

def printParameters(pbInstance, discriminant):
# TODO
    print "TODO"

def printBiasList(pbInstance):
    axis = [i for i in xrange(pbInstance.getNbrBias())]

    plt.plot(axis, pbInstance.getBiasList(), 'bo-', label='List of bias used for the simulation')
    plt.grid()
    plt.xlabel('Simulation')
    plt.ylabel('Bias value')
    plt.legend()
    plt.show()


def plotSampleAndDiscriminant(pbInstance, discriminant):
    sortedSamples = pbInstance.getSortedSample()
    plt.plot(sortedSamples[0][0], sortedSamples[0][1], 'g^', label='Positive samples')
    plt.plot(sortedSamples[1][0], sortedSamples[1][1], 'bo',  label='Negative samples')
    ###### TODO print discriminant
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    
    
    pbInstance      = ProblemInstance()
    pbInstance.parseProblemInstance()

    plt.figure()
    printBiasList(pbInstance)

    for discriminant in pbInstance.discriminantFunction:
        printParameters(pbInstance, discriminant)
        plotSampleAndDiscriminant(pbInstance, discriminant)
        truePositiveRate    = [0 for i in xrange(pbInstance.getNbrBias())]
        falsePositiveRate   = [0 for i in xrange(pbInstance.getNbrBias())]
        buildROC(pbInstance, discriminant, truePositiveRate, falsePositiveRate)
        printROC(falsePositiveRate, truePositiveRate, discriminant)
        print "*********************************************"



