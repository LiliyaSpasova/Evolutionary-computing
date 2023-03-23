from Graph import Vertex
from Graph import Graph
import random
# 0 is left bucket
#1 is right bucket
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
        self.solutions=[]

    def getPart(self,id,partition):
        return partition[id-1]

    def calculateCost(self,vertex,partition):
        cost=0
        part=self.getPart(vertex.id,partition)
        for neigbour in vertex.neighbours:
            neigbourPart=self.getPart(neigbour,partition)
            if neigbourPart!=part:
                cost+=1
        return cost

    def calculateGain(self,vertex,partition):
        cost=self.calculateCost(vertex,partition)
        return cost-(vertex.numNeighbours-cost)
    
    def getMaxCost(self):
        maxcost=-1
        for v in self.g.vertices:
            cost=self.calculateCost(v,self.partition)
            if maxcost<cost:
                maxcost=cost
        return maxcost

    def initializaBuckets(self,maxCost):
        self.rightBucket = {i: set() for i in range(maxCost, -maxCost - 1, -1)}
        self.leftBucket = {i: set() for i in range(maxCost, -maxCost - 1, -1)}

    def fillBuckets(self):
        for v in self.g.vertices:
            part=self.getPart(v.id,self.partition)
            gain=self.calculateGain(v,self.partition)
            if (part==0):
                self.leftBucket[gain].add(v.id)
            else:
                self.rightBucket[gain].add(v.id)
    def areBucketsEmpty(self):
        return False
    def pickVertex(self,bucket):
        for (key,values) in bucket.items():
            if len(values)!=0:
                vertices=list(bucket[key])
                value = vertices[0]
                self.lockedVertices.append(value)
                bucket[key].remove(vertices[0])
                return value
    def moveVertex(self,src):
        if (src==0):
            vertexId=self.pickVertex(self.leftBucket)
            vertex=self.getVertex(vertexId)
            prevGains=[]
            newGains=[]
            for n in vertex.neighbours:
                gain = self.calculateGain(self.getVertex(n),self.partition)
                prevGains.append((n,gain))
            self.partition[vertexId-1]=1
            for n in vertex.neighbours:
                gain = self.calculateGain(self.getVertex(n),self.partition)
                newGains.append((n,gain))
            
        else:
            vertexId=self.pickVertex(self.rightBucket)
            vertex=self.getVertex(vertexId)
            prevGains=[]
            newGains=self.calculateGain(vertex,self.partition)
            for n in vertex.neighbours:
                gain = self.calculateGain(self.getVertex(n),self.partition)
                prevGains.append((n,gain))
            self.partition[vertexId-1]=0
            for n in vertex.neighbours:
                gain = self.calculateGain(self.getVertex(n),self.partition)
                newGains.append((n,gain))
        self.alterBuckets(prevGains,newGains)
    def getVertex(self,id):
        return self.g.vertices[id]
    def alterBuckets(self,prevGains,newGains):
        for ((v,prevGain),(v,newGain)) in (prevGains,newGains):
            x=5
    def calculateFitness(self,partition):
        res=0
        for v in self.g.vertices:
            res+=self.calculateCost(v,partition)
    def FM_pass(self):
        self.g.serealize()
        self.partition=createPartition()
        maxCost=self.getMaxCost()
        self.initializaBuckets(maxCost)
        self.fillBuckets()
        src=0
        counter=0
        while(not self.areBucketsEmpty()):
            self.moveVertex(src)
            self.recalculateBuckets()
            if src==0:
                src=1
            else:
                src=0
            counter+=1
            if counter==2:
                self.solutions.append((self.calculateFitness(self.partition),self.partition))
                counter=0
            

                

