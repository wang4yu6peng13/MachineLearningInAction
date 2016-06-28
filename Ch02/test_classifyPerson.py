#coding:utf-8
import kNN

group, labels = kNN.createDataSet()
print kNN.classify0([0,0],group,labels,3)

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
print datingDataMat
print datingLabels[0:20]

'''
import matplotlib
import matplotlib.pyplot as plt
from numpy import array
fig = plt.figure()
ax = fig.add_subplot(121)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-2, 25, -0.2, 2.0])
plt.xlabel(u'玩视频游戏所耗时间百分比')
plt.ylabel(u'每周消费的冰淇淋公升数')

ax = fig.add_subplot(122)
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-5000, 100000, -1, 25])
plt.xlabel(u'每年获取的飞行常客里程数')
plt.ylabel(u'玩视频游戏所耗时间百分比')
plt.show()
'''

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print normMat
print ranges
print minVals

kNN.datingClassTest()

kNN.classifyPerson()