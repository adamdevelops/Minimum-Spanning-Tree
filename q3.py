'''
Question 3

Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)
'''



class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        print len(self.nodes)
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
            edge_list.append(edge)
        return edge_list

    def get_node_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        node_list = []
        for node in self.nodes:
            node = (node.value)
            node_list.append(node)
        return node_list

    def make_set(self, vertex, parent, rank):
        parent[vertex] = vertex
        rank[vertex] = 0

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, v1, v2):
        v1root = self.find(parent, v1)
        v2root = self.find(parent, v2)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[v1root] < rank[v2root]:
            parent[v1root] = v2root
        elif rank[v1root] > rank[v2root]:
            parent[v2root] = v1root
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[v1root] = v2root
            rank[v2root] += 1


def ques3(graph):
    # Result
    A = {}

    nodes = graph.get_node_list()
    # len_nodes = len(nodes)

    parent = {}
    rank = {}

    for i, node in enumerate(nodes):
        graph.make_set(node, parent, rank)

    edges = sorted(graph.get_edge_list())

    for w, v1, v2 in edges:
        root1 = graph.find(parent, v1)
        root2 = graph.find(parent, v2)
        if root1 != root2:
            if bool(A.has_key(v1)):
                A[v1].append((w,v2))
                graph.union(parent, rank, root1, root2)
            else:
                A[v1] = [(w,v2)]
                graph.union(parent, rank, root1, root2)
    return A



graph = Graph()
graph.insert_edge(10, 'a', 'c')
graph.insert_edge(6, 'a', 'p')
graph.insert_edge(5, 'a', 'y')
graph.insert_edge(15, 'c', 'y')
graph.insert_edge(4, 'p', 'y')

graph1 = Graph()
graph1.insert_edge(2, 'a', 'b')
graph1.insert_edge(3, 'a', 'c')
graph1.insert_edge(3, 'a', 'd')
graph1.insert_edge(4, 'b', 'c')
graph1.insert_edge(3, 'b', 'e')
graph1.insert_edge(5, 'c', 'd')
graph1.insert_edge(1, 'c', 'e')
graph1.insert_edge(7, 'd', 'f')
graph1.insert_edge(8, 'e', 'f')
graph1.insert_edge(9, 'f', 'g')

graph2 = Graph()
graph2.insert_edge(4, 'a', 'b')
graph2.insert_edge(6, 'b', 'c')
graph2.insert_edge(1, 'c', 'f')
graph2.insert_edge(2, 'a', 'f')
graph2.insert_edge(5, 'b', 'f')

print(ques3(graph))
print(ques3(graph1))
print(ques3(graph2))

# O(nlogn)
