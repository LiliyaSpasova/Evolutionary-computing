from FM import FM
import helpers

class ILS:
    def __init__(self,graph,timesToRestart) -> None:
        self.timesToRestart=timesToRestart
        self.graph=graph
        self.FMPassesAllowed=int(10000/timesToRestart)*2
        self.solutions=[]
    def ILS_pass (self):
        return -1
    def pickBestSolution(self):
        minCut=1000
        bestSolution=-1
        for (f,s) in self.solutions:
            if f<minCut:
                bestSolution=(f,s)
                minCut=f
        return bestSolution
    def ILS_run (self):
        for i in range(0,self.timesToRestart):
            partition=helpers.createPartition()
            fm=FM(graph=self.graph,allowedPasses=self.FMPassesAllowed,partition=partition)
            (fitness,solution)=fm.FM_run()
            self.solutions.append((fitness,solution))
        bestSolution=self.pickBestSolution()
        return bestSolution
