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

    pass # Delete and replace with implementation

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
    graph1 = Graph1()
    graph2 = Graph2()
    graph3 = Graph3()