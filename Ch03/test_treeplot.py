
import treePlotter

myTree = treePlotter.retrieveTree(0)
treePlotter.createPlot(myTree)
myTree['no surfacing'][3]= 'maybe'
print myTree
treePlotter.createPlot(myTree)
