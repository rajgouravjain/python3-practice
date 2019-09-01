class LinkedListNode(object):
    def __init__(self,index, data):
        self.index = index
        self.data = data
        self.next = None

class AdjNode(LinkedListNode):
    pass


# A class to represent a graph. A graph
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V"

##considring graph as dictionary of linked list
class Graph:
    def __init__(self):

        self.vertices = {}

        # Function to add an edge in an undirected graph
    def __contains__(self, item):
        return item in self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.keys())
    def add_edge(self, src, dest, weight):
        # Adding the node to the source node

        node = AdjNode(dest, weight)
        if src not in self.vertices:
            self.vertices[src] = None
        node.next = self.vertices[src]
        self.vertices[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src, weight)
        if dest not in self.vertices:
            self.vertices[dest] = None
        node.next = self.vertices[dest]
        self.vertices[dest] = node

        # Function to print the graph

    def print_graph(self):
        print(self.vertices)
        for v in graph:
            print("Adjacency list of vertex {}\n head".format(v), end="")
            temp = self.vertices[v]
            while temp:
                print(" -> {} ({})".format(temp.index, temp.data), end="")
                temp = temp.next
            print(" \n")


if  __name__ == '__main__':
    V = 5
    graph = Graph()
    graph.add_edge(0, 4,5)
    graph.add_edge(0, 1,3)
    graph.add_edge(1, 2,7)
    graph.add_edge(1, 3,2)
    graph.add_edge(1, 4,8)
    graph.add_edge(2, 3,9)
    graph.add_edge(3, 4,1)

    graph.print_graph()