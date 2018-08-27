#!/usr/bin/env python    
# _*_ coding:utf-8 _*_  
import numpy as np

def loadDataFromCSV(fileName):
    dataSet= np.loadtxt(open(fileName,"rb"),delimiter=",",skiprows=1)
    return dataSet

def normalization(dataSet):
    colNum=np.shape(dataSet)[1]
    for index in range(colNum):
        colMax=np.max(dataSet[:,index])
        dataSet[:,index]=dataSet[:,index]/colMax
    return dataSet
#任意给定隶属度，约束条件是，每行的隶属度和为1
def initWithFuzzyMat(n,k):
    fuzzyMat=np.mat(np.zeros((k,n)))#生成k*n的零矩阵
    for colIndex in range(n):
        memDegreeSum=0
        randoms=np.random.rand(k-1,1)#生成k-1行，1列的0-1之间的随机数
        for rowIndex in range(k-1):
            fuzzyMat[rowIndex,colIndex]=randoms[rowIndex,0]*(1-memDegreeSum)
            memDegreeSum+=fuzzyMat[rowIndex,colIndex]
        fuzzyMat[-1,colIndex]=1-memDegreeSum
    return fuzzyMat

def eculidDistance(vectA,vectB):
    return np.sqrt(np.sum(np.power(vectA-vectB,2)))
#根据给定的隶属度计算聚类中心：分母为隶属度和，分子为每个点的隶属度与该点的乘积
def calCentWithFuzzyMat(dataSet,fuzzyMat,p):
    n,m=dataSet.shape
    k=fuzzyMat.shape[0]
    centroids=np.mat(np.zeros((k,m)))
    for rowIndex in range(k):
        degExpArray=np.power(fuzzyMat[rowIndex,:],p)#计算uij的p次方，即隶属度
        denominator=np.sum(degExpArray)#所有样本属于某个聚类的隶属度和
        numerator=np.array(np.zeros((1,m)))
        for colIndex in range(n):
            numerator+=dataSet[colIndex]*degExpArray[0,colIndex]#样本点值*该点属于某个聚类的隶属度
        centroids[rowIndex,:]=numerator/denominator#得到类中心
    return centroids
#根据计算出来的聚类中心，再次迭代计算隶属度
def calFuzzyMatWithCent(dataSet,centroids,p):
    n,m=dataSet.shape
    c=centroids.shape[0]
    fuzzyMat=np.mat(np.zeros((c,n)))
    for rowIndex in range(c):
        for colIndex in range(n):
            d_ij=eculidDistance(centroids[rowIndex,:],dataSet[colIndex,:])
            fuzzyMat[rowIndex,colIndex]=1/np.sum([np.power(d_ij/eculidDistance(centroid,dataSet[colIndex,:]),2/(p-1)) for centroid in centroids])
    return fuzzyMat
#根据公式，不断用新的类中心和隶属度迭代计算目标函数值，直到趋于稳定
def calTargetFunc(dataSet,fuzzyMat,centroids,k,p):
    n,m=dataSet.shape
    c=fuzzyMat.shape[0]
    targetFunc=0
    for rowIndex in range(c):
        for colIndex in range(n):
            targetFunc+=eculidDistance(centroids[rowIndex,:],dataSet[colIndex,:])**2*np.power(fuzzyMat[rowIndex,colIndex],p)
    return targetFunc

def fuzzyCMean(dataSet,k,p,initMethod=initWithFuzzyMat):
    n,m=dataSet.shape
    fuzzyMat=initWithFuzzyMat(n,k)#调用初始化隶属度矩阵函数
    centroids=calCentWithFuzzyMat(dataSet,fuzzyMat,p)#根据隶属度计算类中心
    targetFunc=0
    while targetFunc*0.99>calTargetFunc(dataSet,fuzzyMat,centroids,k,p):
        fuzzyMat=calFuzzyMatWithCent(dataSet,centroids,p)
        centroids=calCentWithFuzzyMat(dataSet,fuzzyMat,p)
    return fuzzyMat,centroids


if __name__=='__main__':
    dataSet=loadDataFromCSV('d:\Python\src\serum.csv')
    dataSet=normalization(dataSet)
    fuzzyMat,centroids=fuzzyCMean(dataSet,9,3)#指定聚类数目和指数m的值
    np.savetxt('serum_9.csv', fuzzyMat.T, delimiter = ',') 
    np.savetxt('centroids_9.csv',centroids.T, delimiter = ',')
    #print 'fuzzyMat=\n',fuzzyMat
    #print np.sum(fuzzyMat,axis=0)
    #print 'centroids=\n',centroids