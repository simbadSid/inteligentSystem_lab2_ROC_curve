from array import array
from util import *





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
    def parseProblemInstance(self, inputFileName = "../resource/input/parameter.txt"):
        file            = open(inputFileName)

        # Init feature samples
        nbrSamples                  = int(nextMeaningLine(file))
        featureDimension            = int(nextMeaningLine(file))
        self.trainingSample_result  = [0.0 for i in xrange(nbrSamples)]
        self.trainingSample_feature = [[0.0 for i in xrange(featureDimension)] for j in xrange(nbrSamples)]
        for sample in xrange(nbrSamples):
            self.trainingSample_result[sample] = int(nextMeaningLine(file))
            for feature in xrange(featureDimension):
                self.trainingSample_feature[sample][feature] = int(nextMeaningLine(file))

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

    def getNbrDiscriminant(self):
        return len(self.discriminantFunction)

    def getFeatureDimension(self):
        return len(self.trainingSample_feature[0])

    # -----------------------------
    # Local methods
    # -----------------------------
    def printProblemInstance(self):
        print "Problem instance:\n"
        msg = ""
        print "\t- Number of samples      : " + str(self.getNbrSample())
        print "\t- Feature dimension      : " + str(self.getFeatureDimension())
        print "\t- training samples       : "
        for sample in xrange(self.getNbrSample()):
            print "\t\t y[" + str(sample) + "]\t = " + str(self.trainingSample_result[sample])
            print "\t\t X[" + str(sample) + "]\t = " + str(self.trainingSample_feature[sample])
        print "\t- Number of discriminant : " + str(self.getNbrDiscriminant())
        print "\t- Discriminant           : "
        for discriminant in xrange(self.getNbrDiscriminant()):
            print "\t\t y[" + str(discriminant) + "]\t = " + str(self.discriminantFunction[discriminant])
        print "\t\t ------------------------------"
