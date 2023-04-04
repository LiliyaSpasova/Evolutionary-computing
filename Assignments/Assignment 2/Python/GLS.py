from FM_2 import FM
import helpers
import numpy as np
import random

def crossover(m1,m2):
    dist=getHammingDistance(m1,m2)
    l1 = len(m1)
    res=[-1 for _ in range(0,l1)]
    if dist>l1/2:
        m1=invertBits(m1)
    counter=0
    zerosLeft=l1/2
    onesLeft=l1/2
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
    def __init__(self,graph,populationsSize,fmPassesPerChild,isModified) -> None:
        self.graph=graph
        self.populationSize=populationsSize
        self.population=[]
        self.fmPassesPerChild=fmPassesPerChild
        self.isModified=isModified
    def removeDuplicates(self,lst):
           return [[a, b] for i, [a, b] in enumerate(lst)  if not any(c == b for _, c in lst[:i])]
    def GLSPass(self):
        random.shuffle(self.population)
        if (self.isModified):
            for i in range (0,int(self.populationSize/2)):
                parents=random.sample(self.population,2)
                while(parents[0]==parents[1]):
                    parents=random.sample(self.population,2)
                child=crossover(parents[0],parents[1])
                fm=FM(graph=self.graph,allowedPasses=self.fmPassesPerChild,partition=child)
                (_,solution)=fm.FM_run()
                self.population.append(solution)
        else:
            random.shuffle(self.population)
            for i in range (0,self.populationSize-1,2):
                child=crossover(self.population[i],self.population[i+1])
                fm=FM(graph=self.graph,allowedPasses=self.fmPassesPerChild,partition=child)
                (_,solution)=fm.FM_run()
                self.population.append(solution)
        competition=[]
        for p in self.population:
            fm=FM(graph=self.graph,allowedPasses=self.fmPassesPerChild,partition=p)
            competition.append((fm.calculateFitness(p),p))
            sortedCompetition = sorted(competition)
        if (self.isModified):
            noduplicates = self.removeDuplicates(sortedCompetition)
            best = noduplicates[0:int(self.populationSize/2)]
            duplicated =  [val for val in best for _ in (0, 1)]
            return duplicated
        else:
            return sortedCompetition[0:int(self.populationSize)]
    
    def runGLS(self):
        for _ in range(0,self.populationSize):
            partition=helpers.createPartition()
            self.population.append(partition)
        #25 children per generation, with 80 FM passes each = 2000, so we do it 5 times 
        for _ in range (0,int(10000/(self.populationSize/2)/self.fmPassesPerChild)):
            sorted=self.GLSPass()
            self.population=[]
            for (f,p) in sorted:
               # print((f,p))
                self.population.append(p)
        return sorted[0]
        

        

