import svmMLiA
from numpy import *

dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')

b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)

ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
print ws

datMat = mat(dataArr)
print datMat[0]*mat(ws)+b
print labelArr[0]
print datMat[1]*mat(ws)+b
print labelArr[1]
print datMat[2]*mat(ws)+b
print labelArr[2]