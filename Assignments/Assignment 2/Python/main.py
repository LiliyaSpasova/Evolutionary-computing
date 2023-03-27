from List import Node
from List import DoubleLinkedList
from Graph import Graph
from MLS import MLS
from GLS import GLS
from ILS import ILS

timesToRestartMLS=300

def main():
    g=Graph()
    g.serealize()
    mls=MLS(g,timesToRestartMLS)
    bestSolutionn=mls.MLS_run()
main()
    