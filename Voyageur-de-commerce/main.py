from greedy import greedy
from complete.greedy import completeGreedy
from display import *
import networkx as nx
from random import random

if __name__ == "__main__":
    
    nbNodes = 8
    edgeList = []
    # G = nx.erdos_renyi_graph(nbNodes, 0.3)
    G = nx.complete_graph(nbNodes) 
    for edge in G.edges():
        edgeList.append((edge[0], edge[1], round(random(), 2)))

    G.clear() 
    G.add_weighted_edges_from(edgeList)
    pos = nx.spring_layout(G, seed=7)
    
    
    # bruteforce(G, pos, 0, edgeList)
    path, costs = greedy(G, pos, 0, edgeList) 

    stopAnimation()
