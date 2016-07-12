import fpGrowth

lotsOtweets = fpGrowth.getLotsOfTweets('RIMM')

print lotsOtweets[0][4].text

listOfTerms = fpGrowth.mineTweets(lotsOtweets, 20)
print len(listOfTerms)

for t in listOfTerms:
    print t