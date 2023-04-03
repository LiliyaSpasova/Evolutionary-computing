class Vertex:
     def __init__(self):
        self.id=-1
        self.coordinates=(None,None)
        self.neighbours=[]
        self.numNeighbours=-1
        self.gain=0
        self.cut=0
        self.partition=None
def remove_spaces(splitLines):
    res = [i for i in splitLines if i != '']
    res = [i for i in res if i != '\n']
    return res
class Graph:
    def __init__(self):
        self.vertices=[]
        self.maxGain=-1
    def serealize(self):
        file1 = open("graphData.txt", 'r')
        Lines = file1.readlines()
        # Strips the newline character
        for line in Lines:
            v=Vertex()
            splitLine=line.split(' ')
            splitLine=remove_spaces(splitLine)
            id=int(splitLine[0])
            coordinates=splitLine[1]
            v.numNeighbours=int(splitLine[2])
            neighbours=[]
            for i in range(3,len(splitLine)):
               neighbours.append(int(splitLine[i]))
            v.id=id
            v.neighbours=neighbours
            v.coordinates=coordinates
            if (self.maxGain<len(neighbours)):
                self.maxGain=len(neighbours)
            self.vertices.append(v)

               


