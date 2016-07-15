import svdRec
from numpy import *

Data = svdRec.loadExData()
U, Sigma, VT = linalg.svd(Data)
print Sigma

Sig3 = mat([[Sigma[0], 0, 0], [0, Sigma[1], 0], [0, 0, Sigma[2]]])
print U[:,:3] * Sig3 * VT[:3,:]

myMat = mat(svdRec.loadExData())
print svdRec.ecludSim(myMat[:,0], myMat[:,4])
print svdRec.ecludSim(myMat[:,0], myMat[:,1])
print svdRec.pearsSim(myMat[:,0], myMat[:,4])
print svdRec.pearsSim(myMat[:,0], myMat[:,1])
print svdRec.cosSim(myMat[:,0], myMat[:,4])
print svdRec.cosSim(myMat[:,0], myMat[:,1])

myMat = mat(svdRec.loadExData1())
print myMat
print svdRec.recommend(myMat, 2)
print svdRec.recommend(myMat, 2, simMeas=svdRec.ecludSim)
print svdRec.recommend(myMat, 2, simMeas=svdRec.pearsSim)

from numpy import linalg as la
U, Sigma, VT = la.svd(mat(svdRec.loadExData2()))
print Sigma
Sig2 = Sigma**2
print sum(Sig2)
print sum(Sig2)*0.9
print sum(Sig2[:2])
print sum(Sig2[:3])

myMat = mat(svdRec.loadExData2())
print svdRec.recommend(myMat, 1, estMethod=svdRec.svdEst)
print svdRec.recommend(myMat, 1, estMethod=svdRec.svdEst,simMeas=svdRec.pearsSim)

svdRec.imgCompress(2)