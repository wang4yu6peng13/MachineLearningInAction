import logRegres
from numpy import *

dataArr, labelMat = logRegres.loadDataSet()
weights = logRegres.gradAscent(dataArr, labelMat)
logRegres.plotBestFit(weights.getA())

weights = logRegres.stocGradAscent0(array(dataArr), labelMat)
logRegres.plotBestFit(weights)

weights = logRegres.stocGradAscent1(array(dataArr), labelMat, 500)
logRegres.plotBestFit(weights)

logRegres.multiTest()