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
            biasedObservation = observation[sample] + bias
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
        print "------------------------------------------"
        if (nbrPositive == 0):
            truePositiveRate[count]     = None
        else :
            truePositiveRate[count]     = nbrTruePositive / nbrPositive
        if (nbrNegative == 0):
            falsePositiveRate[count]    = None
        else:
            falsePositiveRate[count]    = nbrFalsePositive / nbrNegative
        count += 1


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


if __name__ == "__main__":
    pbInstance      = ProblemInstance()
    pbInstance.parseProblemInstance()

    plt.figure()
    printBiasList(pbInstance)

    for discriminant in pbInstance.discriminantFunction:
        truePositiveRate    = [i for i in xrange(pbInstance.getNbrBias())]
        falsePositiveRate   = [i for i in xrange(pbInstance.getNbrBias())]
        buildROC(pbInstance, discriminant, truePositiveRate, falsePositiveRate)
        printROC(falsePositiveRate, truePositiveRate, discriminant)



