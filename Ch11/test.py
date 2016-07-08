import apriori

dataSet = apriori.loadDataSet()
print dataSet
C1 = apriori.createC1(dataSet)
print C1
D = map(set, dataSet)
print D
L1, suppData0 = apriori.scanD(D, C1, 0.5)
print L1

L, suppData = apriori.apriori(dataSet, minSupport=0.5)
print L
#L, suppData = apriori.apriori(dataSet, minSupport=0.7)
#print L
rules = apriori.generateRules(L, suppData, minConf=0.7)
print rules
rules = apriori.generateRules(L, suppData, minConf=0.5)
print rules

'''
actionIdList, billTitles = apriori.getActionIds()
transDict, itemMeaning = apriori.getTransList(actionIdList[:2], billTitles[:2])
for key in transDict.keys():
    print transDict[key]
print transDict.keys()[6]
for item in transDict[' Doyle, Michael 'Mike'']:
    print itemMeaning[item]
transDict, itemMeaning = apriori.getTransList(actionIdList, billTitles)
dataSet = [transDict[key] for key in transDict.keys()]
L, suppData = apriori.apriori(dataSet, minSupport=0.5)
print L
L, suppData = apriori.apriori(dataSet, minSupport=0.3)
print len(L)
print L[6]
rules = apriori.generateRules(L, suppData)
rules = apriori.generateRules(L, suppData, minConf=0.95)
rules = apriori.generateRules(L, suppData, minConf=0.99)
print itemMeaning[26]
print itemMeaning[3]
print itemMeaning[9]
'''

mushDatSet = [line.split() for line in open('mushroom.dat').readlines()]
L, suppData = apriori.apriori(mushDatSet, minSupport=0.3)
for item in L[1]:
    if item.intersection('2'):
        print item
for item in L[3]:
    if item.intersection('2'):
        print item