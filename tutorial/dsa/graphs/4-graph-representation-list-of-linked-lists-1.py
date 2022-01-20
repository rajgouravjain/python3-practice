class LinkedList(object):
    def __init__(self,index, data):
        self.index = index
        self.data = data
        self.next = None

class AdjNode(LinkedList):
    pass


# A class to represent a graph. A graph
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V"

##considring graph as linked list
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.vertices = [None] * self.V

        # Function to add an edge in an undirected graph

    def add_edge(self, src, dest, weight):
        # Adding the node to the source node
        node = AdjNode(dest, weight)
        node.next = self.vertices[src]
        self.vertices[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src, weight)
        node.next = self.vertices[dest]
        self.vertices[dest] = node

        # Function to print the graph

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.vertices[i]
            while temp:
                print(" -> {} ({})".format(temp.index, temp.data), end="")
                temp = temp.next
            print(" \n")


if  __name__ == '__main__':
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 4,5)
    graph.add_edge(0, 1,3)
    graph.add_edge(1, 2,7)
    graph.add_edge(1, 3,2)
    graph.add_edge(1, 4,8)
    graph.add_edge(2, 3,9)
    graph.add_edge(3, 4,1)

    graph.print_graph()