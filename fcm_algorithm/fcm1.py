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
#������������ȣ�Լ�������ǣ�ÿ�е������Ⱥ�Ϊ1
def initWithFuzzyMat(n,k):
    fuzzyMat=np.mat(np.zeros((k,n)))#����k*n�������
    for colIndex in range(n):
        memDegreeSum=0
        randoms=np.random.rand(k-1,1)#����k-1�У�1�е�0-1֮��������
        for rowIndex in range(k-1):
            fuzzyMat[rowIndex,colIndex]=randoms[rowIndex,0]*(1-memDegreeSum)
            memDegreeSum+=fuzzyMat[rowIndex,colIndex]
        fuzzyMat[-1,colIndex]=1-memDegreeSum
    return fuzzyMat

def eculidDistance(vectA,vectB):
    return np.sqrt(np.sum(np.power(vectA-vectB,2)))
#���ݸ����������ȼ���������ģ���ĸΪ�����Ⱥͣ�����Ϊÿ�������������õ�ĳ˻�
def calCentWithFuzzyMat(dataSet,fuzzyMat,p):
    n,m=dataSet.shape
    k=fuzzyMat.shape[0]
    centroids=np.mat(np.zeros((k,m)))
    for rowIndex in range(k):
        degExpArray=np.power(fuzzyMat[rowIndex,:],p)#����uij��p�η�����������
        denominator=np.sum(degExpArray)#������������ĳ������������Ⱥ�
        numerator=np.array(np.zeros((1,m)))
        for colIndex in range(n):
            numerator+=dataSet[colIndex]*degExpArray[0,colIndex]#������ֵ*�õ�����ĳ�������������
        centroids[rowIndex,:]=numerator/denominator#�õ�������
    return centroids
#���ݼ�������ľ������ģ��ٴε�������������
def calFuzzyMatWithCent(dataSet,centroids,p):
    n,m=dataSet.shape
    c=centroids.shape[0]
    fuzzyMat=np.mat(np.zeros((c,n)))
    for rowIndex in range(c):
        for colIndex in range(n):
            d_ij=eculidDistance(centroids[rowIndex,:],dataSet[colIndex,:])
            fuzzyMat[rowIndex,colIndex]=1/np.sum([np.power(d_ij/eculidDistance(centroid,dataSet[colIndex,:]),2/(p-1)) for centroid in centroids])
    return fuzzyMat
#���ݹ�ʽ���������µ������ĺ������ȵ�������Ŀ�꺯��ֵ��ֱ�������ȶ�
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
    fuzzyMat=initWithFuzzyMat(n,k)#���ó�ʼ�������Ⱦ�����
    centroids=calCentWithFuzzyMat(dataSet,fuzzyMat,p)#���������ȼ���������
    targetFunc=0
    while targetFunc*0.99>calTargetFunc(dataSet,fuzzyMat,centroids,k,p):
        fuzzyMat=calFuzzyMatWithCent(dataSet,centroids,p)
        centroids=calCentWithFuzzyMat(dataSet,fuzzyMat,p)
    return fuzzyMat,centroids


if __name__=='__main__':
    dataSet=loadDataFromCSV('d:\Python\src\serum.csv')
    dataSet=normalization(dataSet)
    fuzzyMat,centroids=fuzzyCMean(dataSet,9,3)#ָ��������Ŀ��ָ��m��ֵ
    np.savetxt('serum_9.csv', fuzzyMat.T, delimiter = ',') 
    np.savetxt('centroids_9.csv',centroids.T, delimiter = ',')
    #print 'fuzzyMat=\n',fuzzyMat
    #print np.sum(fuzzyMat,axis=0)
    #print 'centroids=\n',centroids