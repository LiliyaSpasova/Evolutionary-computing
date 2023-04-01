from Graph import Graph
import matplotlib.pyplot as plt


def plotGraph(graph, partition):
    x_values = []
    y_values = []
    for v in graph.vertices:
        coordinates = v.coordinates
        l=len(coordinates)
        wihtoutBrackets=coordinates[1:l-2]
        s=wihtoutBrackets.split(",")
        x_values.append(s[0])
        y_values.append(s[1])
    plt.plot(x_values, y_values, 'bo', linestyle="--")
    plt.show()