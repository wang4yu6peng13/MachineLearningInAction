import adaboost
from numpy import *

datArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
#classifierArray = adaboost.adaBoostTrainDS(datArr, labelArr, 10)
#testArr, testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')
#prediction10 = adaboost.adaClassify(testArr, classifierArray)
#errArr = mat(ones((67, 1)))
#print errArr[prediction10!=mat(testLabelArr).T].sum()

classifierArray, aggClassEst = adaboost.adaBoostTrainDS(datArr, labelArr, 10)
adaboost.plotROC(aggClassEst.T, labelArr)