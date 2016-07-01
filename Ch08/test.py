#coding:utf-8
import regression
from numpy import *

abX, abY = regression.loadDataSet('abalone.txt')
yHat01 = regression.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
yHat1 = regression.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 1)
yHat10 = regression.lwlrTest(abX[0:99], abX[0:99], abY[0:99], 10)
print regression.rssError(abY[0:99], yHat01.T)
print regression.rssError(abY[0:99], yHat1.T)
print regression.rssError(abY[0:99], yHat10.T)

yHat01 = regression.lwlrTest(abX[100:199], abX[0:99], abY[0:99], 0.1)
yHat1 = regression.lwlrTest(abX[100:199], abX[0:99], abY[0:99], 1)
yHat10 = regression.lwlrTest(abX[100:199], abX[0:99], abY[0:99], 10)
print regression.rssError(abY[100:199], yHat01.T)
print regression.rssError(abY[100:199], yHat1.T)
print regression.rssError(abY[100:199], yHat10.T)

ws = regression.standRegres(abX[0:99], abY[0:99])
yHat = mat(abX[100:199])*ws
print regression.rssError(abY[100:199], yHat.T.A)

ridgeWeights = regression.ridgeTest(abX, abY)
#print ridgeWeights
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ridgeWeights)
plt.show()

xArr, yArr = regression.loadDataSet('abalone.txt')
#regression.stageWise(xArr, yArr, 0.01, 200)
#regression.stageWise(xArr, yArr, 0.001, 5000)

xMat, yMat = mat(xArr), mat(yArr).T
xMat = regression.regularize(xMat)
yM = mean(yMat, 0)
yMat = yMat - yM
weights = regression.standRegres(xMat, yMat.T)
print weights.T

weights = regression.stageWise(xArr, yArr, 0.005, 1000)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(weights)
plt.show()

'''
lgX, lgY = [], []
regression.setDataCollect(lgX, lgY)
print shape(lgX)
lgX1 = mat(ones((58, 5)))
lgX1[:, 1:5] = mat(lgX)
print lgX1[0]
ws = regression.standRegres(lgX1, lgY)
print ws
print lgX1[0] * ws
print lgX1[-1] * ws
print lgX1[43] * ws
regression.crossValidation(lgX, lgY, 10)
print regression.ridgeTest(lgX, lgY)
'''