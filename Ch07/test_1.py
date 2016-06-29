import adaboost
from numpy import *

datMat, classLabels = adaboost.loadSimpData()
D = mat(ones((5, 1))/5)
print adaboost.buildStump(datMat, classLabels, D)
classifierArray = adaboost.adaBoostTrainDS(datMat, classLabels, 9)
print classifierArray

datArr, labelArr = adaboost.loadSimpData()
classifierArr = adaboost.adaBoostTrainDS(datArr, labelArr, 30)
print adaboost.adaClassify([0, 0], classifierArr)
print adaboost.adaClassify([[5, 5], [0, 0]], classifierArr)