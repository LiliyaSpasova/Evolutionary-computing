from FM import FM
import helpers
import numpy as np
import random

def crossover(m1,m2):
    dist=getHammingDistance(m1,m2)
    len = len(m1)
    res=[-1 for _ in range(0,len)]
    if dist>len/2:
        m1=invertBits(m1)
    counter=0
    zerosLeft=len/2
    onesLeft=len/2
    for (i,j) in zip(m1,m2):
        if i==j:
            res[counter]=i
            if (i==0):
                zerosLeft-=1
            else:
                onesLeft-=1
        counter+=1
    counter=0
    for (i,j) in zip(m1,m2):
        if i!=j:
            uniform= np.random.uniform(0,1)
            if (uniform<0.5):
                if  zerosLeft>0:
                    res[counter]=0
                    zerosLeft-=1
                else:
                    res[counter]=1
                    onesLeft-=1
            else:
                if onesLeft>0:
                    res[counter]=1
                    onesLeft-=1
                else:
                    res[counter]=0
                    zerosLeft-=1
        counter+=1
    return res

def getHammingDistance(m1,m2):
    res=0
    for (i,j) in zip(m1,m2):
        if i!=j:
            res+=1
    return res

def invertBits (member):
    a=np.array(member)
    np.invert(a)
    return a

class GLS:
    def __init__(self,graph,populationsSize,FMPassesAllowed) -> None:
        self.graph=graph
        self.populationSize=populationsSize
        self.population=[]
        self.FMPassesAllowed=FMPassesAllowed
    
    def GLSPass(self):
        parents=random.sample(self.population, 2)
        child=crossover(parents[0],parents[1])
        fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=child)
        (_,solution)=fm.FM_run()
        self.population.append(solution)
        competition=[]
        for p in self.population:
            fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=p)
            competition.append((fm.calculateFitness(),p))
        sortedCompetition = sorted(competition)
        return sortedCompetition[0:50]
    
    def runGLS(self):
        for _ in range(0,self.poulationSize):
            partition=helpers.createPartition()
            self.population.append(partition)
        

        

