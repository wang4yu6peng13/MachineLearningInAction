import trees
import treePlotter

myDat, labels = trees.createDataSet()
print myDat
print trees.calcShannonEnt(myDat)
print trees.splitDataSet(myDat, 0, 1)
print trees.splitDataSet(myDat, 0, 0)
print trees.splitDataSet(myDat, 1, 1)
print trees.chooseBestFeatureToSplit(myDat)
print trees.createTree(myDat, labels)

treePlotter.createPlot()
print 'createPlot over'

print treePlotter.retrieveTree(1)
myTree = treePlotter.retrieveTree(0)
print treePlotter.getNumLeafs(myTree)
print treePlotter.getTreeDepth(myTree)
