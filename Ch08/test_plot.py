#coding:utf-8
import regression
from numpy import *

xArr, yArr = regression.loadDataSet('ex0.txt')
print xArr[0:2]

ws = regression.standRegres(xArr, yArr)
print ws

xMat, yMat = mat(xArr), mat(yArr)
yHat = xMat * ws
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy * ws
ax.plot(xCopy[:,1], yHat)
plt.show()

yHat = xMat * ws
print corrcoef(yHat.T, yMat)

xArr, yArr = regression.loadDataSet('ex0.txt')
print yArr[0]
print regression.lwlr(xArr[0], xArr, yArr, 1.0)
print regression.lwlr(xArr[0], xArr, yArr, 0.001)
yHat = regression.lwlrTest(xArr, xArr, yArr, 0.01)
# 1.0 与标准回归一致 欠拟合
# 0.003 过拟合
xMat = mat(xArr)
srtInd = xMat[:,1].argsort(0)
xSort = xMat[srtInd][:,0,:]
#import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xSort[:,1], yHat[srtInd])
ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
plt.show()