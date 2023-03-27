from Graph import Vertex
from Graph import Graph
import helpers
# 0 is left bucket
#1 is right bucket
class FM:
    def __init__(self,allowedPasses,graph,partition) -> None:
        self.g=graph
        self.leftBucket={}
        self.rightBucket={}
        self.partition=partition
        self.lockedVertices=[]
        self.solutions=[]
        self.allowedPasses=allowedPasses

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
            cost = v.numNeighbours
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
        for (_,values) in self.leftBucket.items():
            if len(values)>0:
                return False
        for (_,values) in self.rightBucket.items():
             if len(values)>0:
                return False
        return True
    
    def pickVertex(self,bucket):
        for (key,values) in bucket.items():
            if len(values)!=0:
                vertices=list(bucket[key])
                value = vertices[0]
                self.lockedVertices.append(value)
                bucket[key].remove(vertices[0])
                return value
    def moveVertex(self,src):
        prevPartition=self.partition.copy()
        prevGains=[]
        newGains=[]
        if (src==0):
            vertexId=self.pickVertex(self.leftBucket)
            self.partition[vertexId-1]=1
            vertex=self.getVertex(vertexId)
            for n in vertex.neighbours:
                if n not in self.lockedVertices:
                    prevGain = self.calculateGain(self.getVertex(n),prevPartition)
                    newGain = self.calculateGain(self.getVertex(n),self.partition)
                    prevGains.append((n,prevGain))
                    newGains.append((n,newGain))
        else:
            vertexId=self.pickVertex(self.rightBucket)
            self.partition[vertexId-1]=0
            vertex=self.getVertex(vertexId)
            for n in vertex.neighbours:
                if n not in self.lockedVertices:
                    prevGain = self.calculateGain(self.getVertex(n),prevPartition)
                    newGain = self.calculateGain(self.getVertex(n),self.partition)
                    prevGains.append((n,prevGain))
                    newGains.append((n,newGain))
        self.alterBuckets(prevGains,newGains)
    def getVertex(self,id):
        return self.g.vertices[id-1]
    def alterBuckets(self,prevGains,newGains):
        for ((v,prevGain),(v,newGain)) in zip(prevGains,newGains):
            part=self.getPart(v,self.partition)
            if (part==0):
                self.leftBucket[prevGain].remove(v)
                self.leftBucket[newGain].add(v)
            else:
                self.rightBucket[prevGain].remove(v)
                self.rightBucket[newGain].add(v)
    def calculateFitness(self,partition):
        res=0
        for v in self.g.vertices:
            res+=self.calculateCost(v,partition)
        return res
    def pickBestSolution(self):
        minCut=1000000
        bestSolution=None
        for (cut,solution) in self.solutions:
            if minCut>cut:
                minCut=cut
                bestSolution=solution
        return (minCut,bestSolution)
    
    def FM_pass(self):
        src=0
        counter=0
        for _ in range(0,self.allowedPasses):
            self.moveVertex(src)
            if src==0:
                src=1
            else:
                src=0
            counter+=1
            if counter==2:
                partCopy=self.partition.copy()
                fitness = self.calculateFitness(partCopy)
                self.solutions.append((fitness,partCopy))
                counter=0
            if len(self.lockedVertices)==500:
                break
        bestSoltution=self.pickBestSolution() 
        fitness = self.calculateFitness(bestSoltution[1])
        return ((fitness,bestSoltution[1]))
    
    def FM_run(self):
        maxCost=self.getMaxCost()
        self.initializaBuckets(maxCost)
        self.fillBuckets()
        return self.FM_pass()


