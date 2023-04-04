
from Graph import Graph
from MLS import MLS
from GLS import GLS
from ILS import ILS
import time

timesToRestartMLS=60
glsFMPassesPerChild=5
glsPopulationSize=50
isGLSModified=True
glsSolutions=[]
mlsSolutions=[]
ilsSolutions=[]

ilsRestartTimes=100
ilsMutationRate=0.05

timer=2

def main():
    t0 = time.time()
    g=Graph()
    g.serealize()
    for _ in range (0,1):
        mls=MLS(g,timesToRestartMLS,timer)
        mlsSolutions.append(mls.MLS_run())
        gls=GLS(g,glsPopulationSize,glsFMPassesPerChild,isGLSModified,timer)
        glsSolutions.append(gls.runGLS()[0])
        ils=ILS(g,timesToRestart=ilsRestartTimes,mutationRate=ilsMutationRate,timer=timer)
        ilsSolutions.append(ils.ILS_run())
    t1 = time.time()
    totalTime = t1-t0  
    print(totalTime)
    print(mlsSolutions)
    print(ilsSolutions)
    print(glsSolutions)
main()
    