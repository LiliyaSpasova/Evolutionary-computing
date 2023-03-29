from List import Node
from List import DoubleLinkedList
from Graph import Graph
from MLS import MLS
from GLS import GLS
from ILS import ILS
import time

timesToRestartMLS=300
glsFMPassesPerChild=60
glsPopulationSize=50
glsSolutions=[]
mlsSolutions=[]

def main():
    t0 = time.time()
    g=Graph()
    g.serealize()
   
    for _ in range (0,25):
        mls=MLS(g,timesToRestartMLS)
        mlsSolutions.append(mls.MLS_run())
        gls=GLS(g,glsPopulationSize,glsFMPassesPerChild)
        glsSolutions.append(gls.runGLS())
    t1 = time.time()
    totalTime = t1-t0  
    print(totalTime)
main()
    