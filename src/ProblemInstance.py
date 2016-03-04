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
    biasList                        = [[]]        # Contains 1 list of bias for each discriminent
    """

    # -----------------------------
    # Builder
    # -----------------------------
    def parseProblemInstance(self, normalizeData=False, normalizeDiscriminent=False, inputFileName = "../resource/input/parameter.txt"):
        file = open(inputFileName)

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

        # init Bia list
        self.biasList = []
        for discriminant in self.discriminantFunction:
            self.biasList.append(self.computeBiasList(discriminant))

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

    def getDiscriminant(self, discriminantIndex):
        return self.discriminantFunction[discriminantIndex]

    def getFeatureDimension(self):
        return self.featureDimension

    def getBiasList(self, discriminantIndex):
        return self.biasList[discriminantIndex]

    # Return two points of the discriminent: ([x0, x1], [y0, y1])
    def getDiscriminentExtremPoint(self, discriminant):
        # Use the training samples to compute the extreme x and y
        if (discriminant[2] == 0):
            x0 = -1. * discriminant[0] / discriminant[1]
            x1 = x0
            y0 = -1
            y1 = 5
        else:
            x0 = -1.
            x1 = 5.
            y0 = -1. * (x0 * discriminant[1] - discriminant[0]) / discriminant[2]
            y1 = -1. * (x1 * discriminant[1] - discriminant[0]) / discriminant[2]
        
        return ([x0, x1], [y0, y1])

    def getDistanceToDiscriminant(self, discriminant, pointX, pointY):
        a = discriminant[1]
        b = discriminant[2]
        c = discriminant[0]
        numerator   = a * pointX + b * pointY + c
        denominator = math.sqrt((a **2) + (b **2))
        return 1. * numerator / denominator

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
    
    def computeBiasList(self, discriminant):
        res = []
        sampleX = self.trainingSample_featurePositive[0] + self.trainingSample_featureNegative[0]
        sampleY = self.trainingSample_featurePositive[1] + self.trainingSample_featureNegative[1]
        size = 0
        for i in xrange(len(sampleX)):
            x = sampleX[i]
            y = sampleY[i]
            d = self.getDistanceToDiscriminant(discriminant, x, y)
            # insert d in the list by keeping the list sorted and with no doubles
            if ((i == 0) or (d > res[size-1])):
                res.append(d)
                size += 1
                continue
            for j in xrange(size):
                if (res[j] == d):
                    break
                if (res[j] > d):
                    res.insert(j, d)
                    size += 1
                    break
        return res


