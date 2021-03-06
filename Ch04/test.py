import bayes
import feedparser

listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print myVocabList
print bayes.setOfWords2Vec(myVocabList, listOPosts[0])
print bayes.setOfWords2Vec(myVocabList, listOPosts[3])

trainMat = []
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
print pAb
print p0V
print p1V

bayes.testingNB()

print '==email classify=='
bayes.spamTest()
print '==email classify=='
bayes.spamTest()
print '==email classify=='
bayes.spamTest()

print '==feedparser classify=='
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
vocabList, pSF, pNY = bayes.localWords(ny, sf)
vocabList, pSF, pNY = bayes.localWords(ny, sf)

bayes.getTopWords(ny, sf)