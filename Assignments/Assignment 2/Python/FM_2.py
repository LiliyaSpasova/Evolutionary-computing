from Graph import Vertex
from Graph import Graph
import helpers
import random
import time
# 0 is left bucket
#1 is right bucket
class FM:
    def __init__(self,allowedPasses,graph,partition,timer=None) -> None:
        self.g=graph
        self.leftBucket={}
        self.rightBucket={}
        self.partition=partition
        self.lockedVertices=[]
        self.allowedPasses=allowedPasses
        self.cut=None
        self.minCut=100000
        self.bestSolution=None
        self.timer=timer

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

    def updateBuckets(self, vertex):
        vertex.partition = 1 - vertex.partition
        for nId in vertex.neighbours:
            nVertex = self.getVertex(nId)
            nPartition = nVertex.partition
            neighbor_gain = nVertex.gain
            if nPartition == 0:
                if nId in self.leftBucket[neighbor_gain]:
                    self.leftBucket[neighbor_gain].remove(nId)
                    if nVertex.partition == vertex.partition:
                        nVertex.gain -= 2
                    else:
                        nVertex.gain += 2
                    self.leftBucket[nVertex.gain].add(nId)
            else:
                if nId in self.rightBucket[neighbor_gain]:
                    self.rightBucket[neighbor_gain].remove(nId)
                    if nVertex.partition == vertex.partition:
                        nVertex.gain -= 2
                    else:
                        nVertex.gain += 2
                    self.rightBucket[nVertex.gain].add(nId)


    
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
            self.updateBuckets(vertex)
        else:
            vertexId=self.pickVertex(self.rightBucket)
            vertex=self.getVertex(vertexId)
            self.updateBuckets(vertex)
        self.cut-=vertex.gain
        
    def getVertex(self,id):
        return self.g.vertices[id-1]

    def getSolution(self):
        solution=[]
        for v in self.g.vertices:
            solution.append(v.partition)
        return solution
    
    def calculateFitness(self,partition):
        res=0
        for v in self.g.vertices:
            res+=self.calculateCost(v,partition)
        return res/2
    
    def calculateCost(self,vertex,partition):
        cost=0
        for nId in vertex.neighbours:
            if partition[vertex.id-1]!=partition[nId-1]:
                cost+=1
        return cost


    def FM_pass(self):
        cuts=[]
        self.lockedVertices=[]
        src=0
        counter=0
        while len(self.lockedVertices)!=500:
            self.moveVertex(src)
            if src==0:
                src=1
            else:
                src=0
            counter+=1
            if counter==2:
                counter=0
                if (self.minCut>self.cut):
                    self.bestSolution=(self.getSolution()).copy()
                    self.minCut=self.cut
            cuts.append(self.cut)
        return ((self.minCut,self.bestSolution))
    
    def setBuckets(self):
       for v in self.g.vertices:
            if v.partition == 0:
                self.leftBucket[v.gain].add(v.id)
            else:
                self.rightBucket[v.gain].add(v.id)

    def setPartitions (self):
        for i, v in enumerate(self.g.vertices):
               v.partition = self.partition[i]
    def setGains (self):
        for v in self.g.vertices:
            for neighbour in v.neighbours:
                n=self.getVertex(neighbour)
                if n.partition == v.partition:
                    v.gain -= 1
                else:
                    v.gain += 1
                    v.cut += 1

    def getTotalCut(self):
        res = 0
        for (key,values) in self.rightBucket.items():
            vertices=list(self.rightBucket[key])
            for vId in vertices:
                v=self.getVertex(vId)
                res+=v.cut
        return res

    def reset (self):
        for v in self.g.vertices:
            v.gain = 0
            v.cut = 0
    def FM_run(self):
        solutions=[]
        solutions.append((100000,self.partition))
        if self.timer is None:
            for _ in range (0,self.allowedPasses):
                self.reset()
                self.setPartitions()
                self.setGains()
                self.initializaBuckets(self.g.maxGain)
                self.setBuckets()
                self.cut=self.getTotalCut()
                (cut,solution)=self.FM_pass()
                self.partition=solution.copy()
                solutions.append((cut,solution.copy()))
        else:
            start=time.time()
            while True:
                self.reset()
                self.setPartitions()
                self.setGains()
                self.initializaBuckets(self.g.maxGain)
                self.setBuckets()
                self.cut=self.getTotalCut()
                (cut,solution)=self.FM_pass()
                self.partition=solution.copy()
                solutions.append((cut,solution.copy()))
                if time.time()>start+self.timer:
                    break
        return ((cut,solution.copy()))



