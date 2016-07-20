#coding:utf-8
# 分布式均值方差计算的mrjob实现
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRmean(MRJob):
    def __init__(self, *args, **kwargs):
        super(MRmean, self).__init__(*args, **kwargs)
        self.inCount = 0
        self.inSum = 0
        self.inSqSum = 0

    def map(self, key, val): # 接收输入数据流
        if False: yield
        inVal = float(val)
        self.inCount += 1
        self.inSum += inVal
        self.inSqSum += inVal * inVal

    def map_final(self): # 所有输入到达后开始处理
        mn = self.inSum / self.inCount
        mnSq = self.inSqSum / self.inCount
        yield (1, [self.inCount, mn, mnSq])

    def reduce(self, key, packedValues):
        cumVal, cumSumSq, cumN = 0.0, 0.0, 0.0
        for valArr in packedValues:
            nj = float(valArr[0])
            cumN += nj
            cumVal += nj * float(valArr[1])
            cumSumSq += nj * float(valArr[2])
        mean = cumVal/cumN
        var = (cumSumSq - 2*mean*cumVal + cumN*mean*mean)/cumN
        yield (mean, var)

    def steps(self):
        #return ([self.mr(mapper=self.map, reducer=self.reduce, mapper_final=self.map_final)])
        return ([MRStep(mapper=self.map, mapper_final=self.map_final, reducer=self.reduce)])
# mr() is deprecated and will be removed in v0.6.0. Use mrjob.step.MRStep directly instead.

if __name__ == '__main__':
    MRmean.run()

#Windows: python mrMean.py --mapper < inputFile.txt
#Windows: python mrMean.py < inputFile.txt
#Windows: python mrMean.py < inputFile.txt > outFile.txt