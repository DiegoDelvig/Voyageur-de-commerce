from greedy import greedy
from bruteforce import bruteforce
from display import *
import networkx as nx
from random import random
import matplotlib.pyplot as plt


def transformToComplete(G):

    # nx.dijkstra_path(G, node1, node2)
    edges = []
    for node1 in G.nodes:
        for node2 in G.nodes:
            path = nx.dijkstra_path(G, node1, node2)
            edges.append(path)

    for path in edges:
        if (len(path) == 1):
            edges.remove(path)

    return edges


if __name__ == "__main__":

    nbNodes = 6
    edgeList = []
    bruteforceB = False
    greedyB = True

    if (bruteforceB):
        G = nx.complete_graph(nbNodes)
        for edge in G.edges():
            edgeList.append((edge[0], edge[1], round(random(), 2)))
        G.clear()
        G.add_weighted_edges_from(edgeList)
        pos = nx.spring_layout(G, seed=7)
        plt.pause(2)
        bruteforce(G, pos, 0, edgeList)
        stopAnimation()

    if (greedyB):
        G = nx.erdos_renyi_graph(nbNodes, 0.38)

        for edge in G.edges():
            edgeList.append((edge[0], edge[1], round(random(), 2)))
        G.clear()
        G.add_weighted_edges_from(edgeList)
        pos = nx.spring_layout(G, seed=7)
        plt.pause(2)
        path, costs, returnPath = greedy(G, pos, 0, edgeList)
        stopAnimation()
