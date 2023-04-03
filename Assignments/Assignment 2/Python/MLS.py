#from FM import FM
import helpers
from FM_3 import FM

class MLS:
    def __init__(self,graph,timesToRestart) -> None:
        self.timesToRestart=timesToRestart
        self.graph=graph
        self.FMPassesAllowed=int(10000/timesToRestart)
        self.solutions=[]
    def pickBestSolution(self):
        minCut=1000
        bestSolution=-1
        for (s,f) in self.solutions:
            if f<minCut:
                bestSolution=(s,f)
                minCut=f
        return bestSolution[1]
    def MLS_run (self):
        print("Start MLS")
        for i in range(0,self.timesToRestart):
            partition=helpers.createPartition()
           # print(partition)
            #sol, cuts = runFM(self.FMPassesAllowed, partition)
            fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=partition)
            ( cuts,sol, )=fm.FM_run()
            #fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=partition)
            #res=fm.FM_run()
           # print (i,(  cuts))
            self.solutions.append((sol, cuts))
            #print(self.solutions)
        bestSolution=self.pickBestSolution()
        return bestSolution
