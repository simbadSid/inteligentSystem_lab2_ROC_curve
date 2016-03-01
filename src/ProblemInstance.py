from array import array
from util import *
import math
from matplotlib.mathtext import DELTA





class ProblemInstance:
    # -----------------------------
    # Attributes
    # -----------------------------
    """
    trainingSample_feature  = [[]]        # Lecture notation: X:
    trainingSample_result   = [[]]        # Lecture notation: Y
    discriminantFunction    = [[]]        # Lecture notation: W
    """

    # -----------------------------
    # Builder
    # -----------------------------
    def parseProblemInstance(self, normalize=True, inputFileName = "../resource/input/parameter.txt"):
        file = open(inputFileName)

        nbrBias = int(nextMeaningLine(file))
        minBias = int(nextMeaningLine(file))
        maxBias = int(nextMeaningLine(file))
        if (maxBias < minBias):
            raise Exception ("Max bias (" + str(self.maxBias) + ")< min bias (" + str(self.minBias) + ")")
        self.biasList = buildLinearList(minBias, maxBias, nbrBias)

        # Init feature samples
        nbrSamples                  = int(nextMeaningLine(file))
        featureDimension            = int(nextMeaningLine(file))
        self.trainingSample_result  = [0.0 for i in xrange(nbrSamples)]
        self.trainingSample_feature = [[0.0 for i in xrange(featureDimension)] for j in xrange(nbrSamples)]
        for sample in xrange(nbrSamples):
            self.trainingSample_result[sample] = int(nextMeaningLine(file))
            norm = 0.
            for feature in xrange(featureDimension):
                self.trainingSample_feature[sample][feature] = int(nextMeaningLine(file))
                norm += self.trainingSample_feature[sample][feature] ** 2
            if (normalize == True):
                vectorTimeScallar(self.trainingSample_feature[sample], (1/math.sqrt(norm)))

        # Init discriminante
        nbrDiscriminant             = int(nextMeaningLine(file))
        discriminantDimension       = int(nextMeaningLine(file))
        if (discriminantDimension != featureDimension+1):
            raise Exception("Feature and discriminant have unadaptable dimensions")
        self.discriminantFunction   = [[0.0 for j in xrange(discriminantDimension)] for i in xrange(nbrDiscriminant)]
        for discriminant in xrange(nbrDiscriminant):
            for dim in xrange(discriminantDimension):
                self.discriminantFunction[discriminant][dim] = int(nextMeaningLine(file))
        

        file.close()

    # -----------------------------
    # Getter
    # -----------------------------
    def getNbrSample(self):
        return len(self.trainingSample_result)

    def getTrainingSampleValue(self, sample):
        return self.trainingSample_result[sample]

    def getNbrDiscriminant(self):
        return len(self.discriminantFunction)

    def getFeatureDimension(self):
        return len(self.trainingSample_feature[0])

    def getNbrBias(self):
        return len(self.biasList)

    def getMinBias(self):
        return self.biasList[0]

    def getMaxBias(self):
        return self.biasList[len(self.biasList)-1]

    def getBiasList(self):
        return self.biasList


    # -----------------------------
    # Local methods
    # -----------------------------

    # Return the list of the scalar product W.X for each feature X
    def computeObservationList(self, discriminant):
        res = [0. for i in xrange(self.getNbrSample())]
        for sample in xrange(self.getNbrSample()):
            X = self.trainingSample_feature[sample]
            res[sample] = discriminant[0]
            for dim in xrange(len(X)):
                res[sample] += X[dim] * discriminant[dim+1]
        return res

    def printProblemInstance(self):
        print "Problem instance:\n"
        msg = ""
        print "\t- Number of bias         : " + str(self.getNbrBias())
        print "\t- Bias min               : " + str(self.getMinBias())
        print "\t- Bias max               : " + str(self.getMaxBias())
        print "\t- Number of samples      : " + str(self.getNbrSample())
        print "\t- Feature dimension      : " + str(self.getFeatureDimension())
        print "\t- training samples       : "
        for sample in xrange(self.getNbrSample()):
            print "\t\t y[" + str(sample) + "]\t = " + str(self.trainingSample_result[sample])
            print "\t\t X[" + str(sample) + "]\t = " + str(self.trainingSample_feature[sample])
            print "\t\t ------------------------------"
        print "\t- Number of discriminant : " + str(self.getNbrDiscriminant())
        print "\t- Discriminant           : "
        for discriminant in xrange(self.getNbrDiscriminant()):
            print "\t\t y[" + str(discriminant) + "]\t = " + str(self.discriminantFunction[discriminant])
            print "\t\t ------------------------------"
