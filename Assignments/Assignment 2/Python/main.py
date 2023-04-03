
from Graph import Graph
from MLS import MLS
from GLS import GLS
from ILS import ILS
import time

timesToRestartMLS=120
glsFMPassesPerChild=20
glsPopulationSize=50
isGLSModified=False
glsSolutions=[]
mlsSolutions=[]
ilsSolutions=[]

ilsRestartTimes=100
ilsMutationRate=0.05


def main():
    t0 = time.time()
    g=Graph()
    g.serealize()
    for _ in range (0,5):
      #  mls=MLS(g,timesToRestartMLS)
      #  mlsSolutions.append(mls.MLS_run())
       # gls=GLS(g,glsPopulationSize,glsFMPassesPerChild,isGLSModified)
        #glsSolutions.append(gls.runGLS())
        ils=ILS(g,timesToRestart=ilsRestartTimes,mutationRate=ilsMutationRate)
        ilsSolutions.append(ils.ILS_run())
        print("Current solutions")
        print(ilsSolutions)
    t1 = time.time()
    totalTime = t1-t0  
    print(totalTime)
    print(mlsSolutions)
main()
    