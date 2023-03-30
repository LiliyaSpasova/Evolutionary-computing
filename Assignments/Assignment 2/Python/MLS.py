from FM import FM
import helpers

class MLS:
    def __init__(self,graph,timesToRestart) -> None:
        self.timesToRestart=timesToRestart
        self.graph=graph
        self.FMPassesAllowed=int(10000/timesToRestart)
        self.solutions=[]
    def pickBestSolution(self):
        minCut=1000
        bestSolution=-1
        for (f,s) in self.solutions:
            if f<minCut:
                bestSolution=(f,s)
                minCut=f
        return bestSolution
    def MLS_run (self):
        for i in range(0,self.timesToRestart):
            partition=helpers.createPartition()
            fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=partition)
            (fitness,solution)=fm.FM_run()
            print (i, (fitness,solution))
            self.solutions.append((fitness,solution))
            print(self.solutions)
        bestSolution=self.pickBestSolution()
        return bestSolution
