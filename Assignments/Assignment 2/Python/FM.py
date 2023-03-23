from Graph import Vertex
from Graph import Graph
import random
def createPartition():
    length = 250
    partition = [0] * length + [1] * length
    random.shuffle(partition)
    return partition

class FM:
    def __init__(self) -> None:
        self.g=Graph()
        self.leftBucket={}
        self.rightBucket={}
        self.partition=""
        self.lockedVertices=[]

    def getPart(self,id):
        return self.partition[id-1]

    def calculateCost(self,vertex):
        cost=0
        part=self.getPart(vertex.id)
        for neigbour in vertex.neighbours:
            neigbourPart=self.getPart(neigbour)
            if neigbourPart!=part:
                cost+=1
        return cost

    def calculateGain(self,vertex):
        cost=self.calculateCost(vertex)
<<<<<<< HEAD
        return cost-(vertex.numNeighbours-cost)
=======
        return cost-vertex.numNeighbours

>>>>>>> 8222dcfa5539ea09f5c9aa4781b4ae04f6d14506
    def getMaxCost(self):
        maxcost=-1
        for v in self.g.vertices:
            cost=self.calculateCost(v)
            if maxcost<cost:
                maxcost=cost
        return maxcost

    def initializaBuckets(self,maxCost):
        self.rightBucket = {i: set() for i in range(maxCost, -maxCost - 1, -1)}
        self.leftBucket = {i: set() for i in range(maxCost, -maxCost - 1, -1)}

    def fillBuckets(self):
        for v in self.g.vertices:
            part=self.getPart(v.id)
            gain=self.calculateGain(v)
            if (part==0):
                self.leftBucket[gain].add(v.id)
            else:
                self.rightBucket[gain].add(v.id)
    
    def moveVertex(self):
        return -1

    def recalculateBuckets(self):
        return -1
        
    def FM_pass(self):
        self.g.serealize()
        self.partition=createPartition()
        maxCost=self.getMaxCost()
        self.initializaBuckets(maxCost)
        self.fillBuckets()
        x=5
                

