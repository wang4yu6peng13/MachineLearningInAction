#coding:utf-8
# 分布式均值和方差计算的reducer
import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.rstrip()

input = read_input(sys.stdin)
mapperOut = [line.split('\t') for line in input]
cumVal = 0.0
cumSumSq = 0.0
cumN = 0.0
for instance in mapperOut:
    nj = float(instance[0])
    cumN += nj
    cumVal += nj * float(instance[1])
    cumSumSq += nj * float(instance[2])
mean = cumVal / cumN
varSum = (cumSumSq - 2 * mean * cumVal + cumN * mean * mean) / cumN
#report: still alive
#100	0.509570	0.084777
#report: still alive

meanSq = cumSumSq/cumN
#report: still alive
#100	0.509570	0.344439
#report: still alive

#print "%d\t%f\t%f" % (cumN, mean, varSum)
print "%d\t%f\t%f" % (cumN, mean, meanSq)
print >> sys.stderr, "report: still alive"

# Linux: cat inputFile.txt | python mrMeanMapper.py | python mrMeanReducer.py
# Windows: python mrMeanMapper.py < inputFile.txt | python mrMeanReducer.py