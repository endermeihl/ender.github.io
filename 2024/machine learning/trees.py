from math import log

def calcShannonEnt(dataSet: list) -> float:
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: # the the number of unique elements and their occurance
        currentLabel = featVec[-1] # the last column is used as label
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts: # calculate the Shannon entropy
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) # log base 2
    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    #change to discrete values
    return dataSet, labels

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    # 使用第一行判断包含多少特征属性
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    # 遍历所有的特征属性
    for i in range(numFeatures):  #iterate over all the features
        featList = [example[i] for example in dataSet]  #create a list of all the examples of this feature
        uniqueVals = set(featList)  #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):  #compare this to the best gain so far
            bestInfoGain = infoGain  #if better than current best, set to best
            bestFeature = i
    return bestFeature