"""
Ash Frazer, Axel Pinard, and Jonathan Wynn

CSCI 3330 Project 3: Graph Algorithms
"""

import collections

import networkx as nx
import matplotlib.pyplot as plt

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

    def __init__(self):  # Constructor
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
                self.dfsUtil(i, visited)

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

    def __init__(self):  # Constructor
        # Initialize graph
        self.G = nx.DiGraph()

        # Create nodes
        nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.G.add_nodes_from(nodes)

        # Add edges
        edges = [
            ('1', '3'), ('3', '2'), ('2', '1'), ('3', '5'), ('4', '1'),
            ('4', '2'), ('4', '12'), ('5', '6'), ('5', '8'), ('6', '7'),
            ('6', '8'), ('6', '10'), ('7', '10'), ('8', '9'), ('8', '10'),
            ('9', '5'), ('9', '11'), ('10', '9'), ('10', '11'), ('11', '12')
        ]

        self.G.add_edges_from(edges)

    def displayGraph(self):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.G)

        # Draw graph
        nx.draw_networkx_nodes(self.G, pos)
        nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edges(self.G, pos, edge_color='r', arrows=True)

        plt.show()

    """
    https://www.geeksforgeeks.org/strongly-connected-components/
    """

    # dfs Function to reach destination
    def dfs(self, curr, des, adj, vis):
        # If current node is the destination, return True
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False

    # To tell whether there is a path from source to destination
    def isPath(self, src, des, adj):
        vis = [0] * (len(adj) + 1)
        return self.dfs(src, des, adj, vis)

    # Function to return all the strongly connected components of a graph.
    def findSCC(self, n, a):
        # Stores all the strongly connected components.
        ans = []

        # Stores whether a vertex is a part of any Strongly Connected Component
        is_scc = [0] * (n + 1)

        adj = [[] for _ in range(n + 1)]

        for i in range(len(a)):
            adj[a[i][int(0)]].append(a[i][int(1)])

        # Traversing all the vertices
        for i in range(1, n + 1):
            if not is_scc[i]:
                # If a vertex i is not a part of any SCC, insert it into a new SCC list
                # and check for other vertices whether they can be part of this list.
                scc = [i]
                for j in range(i + 1, n + 1):
                    # If there is a path from vertex i to vertex j and vice versa,
                    # put vertex j into the current SCC list.
                    if not is_scc[j] and self.isPath(i, j, adj) and self.isPath(j, i, adj):
                        is_scc[j] = 1
                        scc.append(j)
                # Insert the SCC containing vertex i into the final list.
                ans.append(scc)
        return ans

    def sccTest(self):
        obj = Graph2()
        v = int(12)
        sccEdge = [
            [1, 3], [3, 2], [2, 1], [3, 5], [5, 6],
            [4, 2], [4, 1], [4, 12], [5, 8], [9, 5],
            [6, 7], [6, 8], [6, 10], [7, 10], [8, 9],
            [8, 10], [9, 11], [10, 9], [10, 11], [11, 12]
        ]
        ans = obj.findSCC(v, sccEdge)
        print("Strongly Connected Components are:")
        for x in ans:
            for y in x:
                print(y, end=" ")
            print()


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
    def __init__(self): # Constructor
        # Initialize graph
        self.G = nx.Graph()

        # Create nodes
        nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.G.add_nodes_from(nodes)

        # Add edges
        
        edges = [
            ('A', 'B', weight := 22.0), ('A', 'C', weight := 9.0), ('A', 'D', weight := 12.0),
            ('B', 'C', weight := 35.0), ('B', 'F', weight := 36.0), ('B', 'H', weight := 34.0),
            ('C', 'D', weight := 4.0), ('C', 'E', weight := 65.0), ('C', 'F', weight := 42.0),
            ('D', 'E', weight := 33.0), ('D', 'I', weight := 30.0),
            ('E', 'F', weight := 18.0), ('E', 'G', weight := 23.0),
            ('F', 'G', weight := 39.0), ('F', 'H', weight := 24.0),
            ('G', 'H', weight := 25.0), ('G', 'I', weight := 21.0),
            ('H', 'I', weight := 19.0)
        ]

        self.G.add_weighted_edges_from(edges)

    def displayGraph(self):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.G)
        # Draw graph
        nx.draw(
        self.G, pos, with_labels=True, node_color='lightblue', edge_color='red',
        node_size=1000, font_size=10, font_weight='bold', width=1.5)
        plt.show()

    def Dijkstra(self):
        start = input("What is the starting node for our Dijkstra's Alg: ")
        for pathways in self.G:
           if pathways == start:
               continue   
           print(f"The fastest path to {pathways} is")
           print(nx.dijkstra_path(self.G, start, pathways))
        print("")

    def MST(self):
        mst_G = nx.minimum_spanning_tree(self.G)
        
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(mst_G)
        # Draw graph
        nx.draw(
        mst_G, pos, with_labels=True, node_color='lightblue', edge_color='red',
        node_size=1000, font_size=10, font_weight='bold', width=1.5)
        plt.show()


def main():
    menu = {
        1: 'Graph 1',
        2: 'Graph 2',
        3: 'Graph 3',
        4: 'Exit program'}

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
            graph2.displayGraph()
            graph2.sccTest()
            continue
        elif selection == '3':
            graph3.displayGraph()
            graph3.Dijkstra()
            graph3.MST()
            continue
        elif selection == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid option!')


main()
