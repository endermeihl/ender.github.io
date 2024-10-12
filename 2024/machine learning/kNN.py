import matplotlib.pyplot as plt
from numpy import *
import operator
from os import listdir

def createDateSet()-> tuple:
    group = array([[1.0, 1.1],[1.0, 1.0],[0, 0],[0, 0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX: array, dataSet: array, labels: list, k: int) -> str:
    dataSetSize = dataSet.shape[0] # 数据的纬度情况
    diffMat = tile(inX, (dataSetSize,1)) - dataSet # tile(inX, (dataSetSize,1)) 将inX重复dataSetSize次，1代表在行上重复,纬度广播
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1) # axis=1表示按行相加，axis=0表示按列相加
    distances = sqDistances**0.5 # 欧式距离公式
    sortedDistIndicies = distances.argsort() # 返回从小到大的索引值
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] # 返回距离最近的k个点的标签
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # 计算每个标签出现的次数
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) # 对字典按值进行排序，返回一个列表
    return sortedClassCount[0][0]

def file2matrix(filename: str) -> tuple:
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines) # 得到文件行数
    returnMat = zeros((numberOfLines,3)) # 创建一个numberOfLines行，3列的矩阵
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3] # 将每行的前三个元素存储到矩阵中
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet: array) -> tuple:
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.2
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        if(classifierResult!=datingLabels[i]):
            errorCount +=1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([
        ffMiles,
        percentTats,
        iceCream,
    ])
    classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print("You will probably like this person: %s" % resultList[classifierResult - 1])


def img2vector(filename: str) -> array:
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline() # 读取一行
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j]) # 将每行的前32个元素存储到矩阵中
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits') # 获取目录内容
    m = len(trainingFileList)
    trainingMat = zeros((m,1024)) # 创建一个m行，1024列的矩阵
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0] # 获取文件名
        classNumStr = int(fileStr.split('_')[0]) # 获取文件名的第一个数字
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits') # 获取目录内容
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0] # 获取文件名
        classNumStr = int(fileStr.split('_')[0]) # 获取文件名的第一个数字
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult,classNumStr))
        if(classifierResult != classNumStr):
            errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))