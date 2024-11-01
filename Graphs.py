import collections

import networkx as nx
import matplotlib.pyplot as plt

# sample code to create and display graph via matplotlib
# G = nx.Graph()
#
# # add nodes to the graph
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_node("D")

# # connect nodes with edges
# G.add_edge("A", "B")
# G.add_edge("A", "C")
# G.add_edge("B", "D")
# G.add_edge("C", "D")

# # draw the graph
# nx.draw(G, with_labels=True, node_color='lightblue', edge_color='red', node_size=1000, font_size=15)
# plt.show()

class Graph1:
    """
    You are asked to represent the undirected graph below in a computer. Then, apply it
    as a sample to answer the following questions computationally:
    a) Starting from any vertex, can DFS and BFS find all connected components of an
    undirected graph?
    b) Can both BFS and DFS determine if there is a path between two given nodes?
    c) Provided that there is a path between two vertices u and v in the graph. If started
    from u, do DFS and BFS always find exactly the same path to v?
    """
    def __init__(self): # Constructor
        # Initialize graph
        self.G = nx.Graph()

        # Create nodes
        nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        self.G.add_nodes_from(nodes)

        # Add edges
        edges = [
            ('A', 'B'), ('A', 'E'), ('A', 'F'), ('B', 'C'), ('B', 'F'),
            ('C', 'D'), ('C', 'G'), ('D', 'G'), ('E', 'F'), ('E', 'I'),
            ('F', 'I'), ('I', 'J'), ('I', 'M'), ('J', 'G'), ('M', 'N'),
            ('H', 'K'), ('H', 'L'), ('K', 'L'), ('K', 'O'), ('L', 'P')
        ]

        self.G.add_edges_from(edges)

    def displayGraph(self):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.G)

        # Draw graph
        nx.draw(
            self.G, pos, with_labels=True, node_color='lightblue', edge_color='red',
            node_size=1000, font_size=10, font_weight='bold', width=1.5
        )

        plt.show()

    def dfsUtil(self, v, visited):
        """
        https://www.geeksforgeeks.org/python-program-for-depth-first-search-or-dfs-for-a-graph/
        """
        visited.add(v)
        print(v, end=' ')
        for i in self.G[v]:
            if i not in visited:
                self.dfsUtil(i,visited)

    def dfs(self, v):
        visited = set()
        self.dfsUtil(v, visited)

    def dfsTest(self):
        while True:
            print('DFS Test')
            start_node = input('Enter starting node: ').upper()
            if start_node not in self.G.nodes:
                print('Invalid input')
                continue
            self.dfs(start_node)
            print('')
            selection = input('Run DFS again? (y/n): ').lower()
            if selection == 'y':
                continue
            else:
                break

    def bfs(self, start):
        """
        https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/?ref=header_outind
        """
        visited = {node: False for node in self.G}
        queue = collections.deque([start])
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for i in self.G[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def bfsTest(self):
        while True:
            print('BFS Test')
            start_node = input('Enter starting node: ').upper()
            if start_node not in self.G.nodes:
                print('Invalid input')
                continue
            self.bfs(start_node)
            selection = input('Run BFS again? (y/n): ').lower()
            if selection == 'y':
                continue
            else:
                break

class Graph2:
    """
    A connected digraph can be decomposed to its strongly connected components as a
    ‘meta graph’. Implement the digraph below as a graph object, and then answer the
    following questions computationally.
    a) Use an application to find the strongly connected components of the digraph;
    b) Draw the digraph as a ‘meta graph’ of its strongly connected components in your
    project report (Note: you don’t have to draw it with a program. Draw it manually
    in your report is acceptable); and then
    c) Represent the ‘meta graph’ as a DAG and linearize it in its topological order.
    """

    pass # Delete and replace with implementation

class Graph3:
    """
    Provided is a weighted undirected graph. Implement it as a graph object and then
    computationally answer the following questions:
    a) Write an application that applies Dijkstra’s algorithm to produce the shortest path
    tree for a weighted graph with a given starting node. Test and verify your program
    with the given graph starting with node A;
    b) Write a program that produces a minimum spanning tree for a connected weighted
    graph. Test your program with the given graph above;
    c) Are a shortest path tree and a minimum spanning tree usually the same?
    d) If the graph has an edge with a negative weight, can you apply Dijkstra’s
    algorithm to find a shortest path tree?
    """

    pass # Delete and replace with implementation

def main():
    menu = {
            1 : 'Graph 1',
            2 : 'Graph 2',
            3 : 'Graph 3',
            4 : 'Exit program'}

    # Initialize graph objects
    graph1 = Graph1()
    graph2 = Graph2()
    graph3 = Graph3()

    print('Welcome to our Graph Project!')
    print(f'Which graph would you like to see?')

    # Prompt user for selection
    while True:
        # Print menu options
        for key, value in menu.items():
            print(f'{key}: {value}')

        selection = input('Enter your option (1-4): ')
        if selection == '1':
            graph1.displayGraph()
            graph1.dfsTest()
            graph1.bfsTest()
            continue
        elif selection == '2':
            # graph2.displayGraph()
            continue
        elif selection == '3':
            # graph3.displayGraph()
            continue
        elif selection == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid option!')

main()