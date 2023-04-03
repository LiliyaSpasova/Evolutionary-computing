from FM_3 import FM
import helpers
import random
class ILS:
    def __init__(self,graph,timesToRestart,mutationRate) -> None:
        self.timesToRestart=timesToRestart
        self.graph=graph
        self.FMPassesAllowed=int(10000/timesToRestart)
        self.solutions=[]
        self.mutationRate=mutationRate
        self.bestMinCut=10000
        self.bestPartition=None

    def ILS_pass (self,partition):
        for i in range(0,len(partition)):
            x=random.uniform(0,1)
            if (x<self.mutationRate):
                index=random.randint(0, len(partition)-1)
                while partition[i]==partition[index]:
                    index=random.randint(0, len(partition)-1)
                temp = partition[i]
                partition[i]=partition[index]
                partition[index]=temp
        return partition

    
    def ILS_run (self):
        partition=helpers.createPartition()
        for i in range(0,self.timesToRestart):
            partition=self.ILS_pass(partition)
            fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=partition.copy())
            minCutPrev=fm.calculateFitness(partition)
            (minCutNew,newPartition)=fm.FM_run()
            if(minCutNew<self.bestMinCut):
               self.bestMinCut=minCutNew
               self.bestPartition=newPartition
               partition=newPartition
            self.solutions.append((self.bestMinCut,self.bestPartition))
        print (self.bestMinCut)
        return (self.bestMinCut)
