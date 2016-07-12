import fpGrowth

parsedDat = [line.split() for line in open('kosarak.dat').readlines()]
initSet = fpGrowth.createInitSet(parsedDat)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 100000)
myFreqList = []
fpGrowth.mineTree(myFPtree, myHeaderTab, 100000, set([]), myFreqList)
print len(myFreqList)
print myFreqList