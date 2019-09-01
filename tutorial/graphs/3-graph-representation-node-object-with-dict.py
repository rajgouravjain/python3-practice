class Node(object):
    def __init__(self,id):
        self.connected_to = {}
        self.id = id
    def add_neighbour(self,nbr, weight):
        self.connected_to[nbr] = weight

###Considering graph as dicitionary

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.number_of_nodes = 0

    def add_node(self,key):
        self.number_of_nodes += 1
        node = Node(key)
        self.vertices[key] = node
        return node

    def get_node(self,key):
        if  key in self.vertices :
            return self.vertices[key]
        raise ValueError


    def __contains__(self, item):
        return item  in self.vertices

    def add_edge(self,src,dst,cost):
        if src not in self.vertices :
            node  =  self.add_node(src)
        if dst not  in  self.vertices:
            node = self.add_node(dst)
        self.vertices[src].add_neighbour(self.vertices[dst],cost)
        self.vertices[dst].add_neighbour(self.vertices[src],cost)
    def get_nodes(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_node(str(i))

    g.add_edge("1","2",10)




