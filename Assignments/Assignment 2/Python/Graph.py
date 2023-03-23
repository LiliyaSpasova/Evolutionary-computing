class Vertex:
     def __init__(self):
        self.id=-1
        self.coordinates=(None,None)
        self.neighbours=[]
def remove_spaces(splitLines):
    res = [i for i in splitLines if i != '']
    return res
class Graph:
    def __init__(self):
        self.vertices=[]
    def serealize(self):
        file1 = open("Assignment 2\Python\graphData.txt", 'r')
        Lines = file1.readlines()
        # Strips the newline character
        for line in Lines:
            v=Vertex()
            splitLine=line.split(' ')
            splitLine=remove_spaces(splitLine)
            id=splitLine[0]
            coordinates=splitLine[1]
            neighbours=[]
            for i in range(3,len(splitLine)):
               if (i==len(splitLine)-1):
                   splitLine[i]=splitLine[i].replace("\n","")
               neighbours.append(splitLine[i])
            v.id=id
            v.neighbours=neighbours
            v.coordinates=coordinates
            self.vertices.append(v)

               


