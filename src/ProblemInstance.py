from array import array
from util import *
import math
from matplotlib.mathtext import DELTA





class ProblemInstance:
    # -----------------------------
    # Attributes
    # -----------------------------
    """
    trainingSample_featureNegative  = [[]]        # Lecture notation: X (partial set):
    trainingSample_featurePositive  = [[]]        # Lecture notation: X (partial set):
    trainingSample_feature          = [[]]        # Lecture notation: X (total set):
    discriminantFunction            = [[]]        # Lecture notation: W
    """

    # -----------------------------
    # Builder
    # -----------------------------
    def parseProblemInstance(self, normalizeData=False, normalizeDiscriminent=False, inputFileName = "../resource/input/parameter.txt"):
        file = open(inputFileName)

        nbrBias = int(nextMeaningLine(file))
        minBias = int(nextMeaningLine(file))
        maxBias = int(nextMeaningLine(file))
        if (maxBias < minBias):
            raise Exception ("Max bias (" + str(self.maxBias) + ")< min bias (" + str(self.minBias) + ")")
        self.biasList = buildLinearList(minBias, maxBias, nbrBias)

        # Init feature samples
        self.nbrSamples                     = int(nextMeaningLine(file))
        self.featureDimension               = int(nextMeaningLine(file))
        self.trainingSample_featurePositive = [[] for i in xrange(self.featureDimension)]
        self.trainingSample_featureNegative = [[] for i in xrange(self.featureDimension)]
        vect = []
        for sample in xrange(self.nbrSamples):
            y       = int(nextMeaningLine(file))
            norm    = 0.
            if (y > 0):
                vect = self.trainingSample_featurePositive
            else:
                vect = self.trainingSample_featureNegative
            for dim in xrange(self.featureDimension):
                xi      = int(nextMeaningLine(file))
                norm    += xi ** 2
                (vect[dim]).append(xi)
            if (normalizeData == True):
                index = len(vect[0])-1
                norm = math.sqrt(norm)
                for dim in xrange(self.featureDimension):
                    vect[dim][index] /= norm

        # Init discriminante
        nbrDiscriminant             = int(nextMeaningLine(file))
        discriminantDimension       = int(nextMeaningLine(file))
        if (discriminantDimension != self.featureDimension+1):
            raise Exception("Feature and discriminant have unadaptable dimensions")
        self.discriminantFunction   = [[0.0 for j in xrange(discriminantDimension)] for i in xrange(nbrDiscriminant)]
        for discriminant in xrange(nbrDiscriminant):
            norm = 0
            for dim in xrange(discriminantDimension):
                self.discriminantFunction[discriminant][dim] = int(nextMeaningLine(file))
                norm += self.discriminantFunction[discriminant][dim] ** 2
            if (normalizeDiscriminent == True):
                vectorTimeScallar(self.discriminantFunction[discriminant], 1./math.sqrt(norm))

        file.close()

    # -----------------------------
    # Getter
    # -----------------------------
    def getNbrSample(self):
        return self.nbrSamples

    def getNbrPositiveSample(self):
        return len(self.trainingSample_featurePositive[0])

    def getNbrNegativeSample(self):
        return len(self.trainingSample_featureNegative[0])

    def getPositiveSample(self):
        return self.trainingSample_featurePositive

    def getNegativeSample(self):
        return self.trainingSample_featureNegative

    def getNbrDiscriminant(self):
        return len(self.discriminantFunction)

    def getFeatureDimension(self):
        return self.featureDimension

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

    # Return the list of the scalar product W.X for each feature X such as Y is positive
    def computeObservationList(self, discriminant, positiveSample):
        res = [0. for i in xrange(self.getNbrPositiveSample())]
        if (positiveSample == True):
            X           = self.getPositiveSample()
            nbrSample   = self.getNbrPositiveSample()
        else:
            X           = self.getNegativeSample()
            nbrSample   = self.getNbrNegativeSample()
        for sample in xrange(nbrSample):
            res[sample] = discriminant[0]
            for dim in xrange(self.getFeatureDimension()):
                res[sample] += X[dim][sample] * discriminant[dim+1]
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
