from edge import Edge
from node import Node


class Graph(object):

    def __init__(self,nodes,edges):
        self.nodes = nodes
        self.edges = edges

        self.adjacencyList = {}
        for node in self.nodes:
            self.adjacencyList[node.name] = []

        for edge in self.edges:
            self.adjacencyList[edge.node1.name].append(edge)


    def addNode(self,nodeName):
        node = Node(nodeName)
        self.nodes.append(node)
        self.adjacencyList[node.name] = []

    def addEdge(self,node1,node2,weight):
        edge = Edge(node1,node2,weight)
        self.edges.append(edge)
        self.adjacencyList[edge.node1.name].append(edge.node2)


n1 = Node("A")
n2 = Node("B")
n3 = Node("C")

e1 = Edge(n1,n2,4.0)
e2 = Edge(n1,n3,5.0)
e3 = Edge(n2,n3,5.0)

graph = Graph([n1,n2,n3],[e1,e2,e3])

print(graph.adjacencyList)



