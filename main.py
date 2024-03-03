from greedy import greedy
from display import *
import networkx as nx
from random import random

if __name__ == "__main__":
    
    nbNodes = 10
    edgeList = []
    G = nx.erdos_renyi_graph(nbNodes, 0.5)
#       for edge in G.edges():
#           edgeList.append((edge[0], edge[1], round(random(), 2)))

#       G.clear() 
#       G.add_weighted_edges_from(edgeList)
#       pos = nx.spring_layout(G, seed=7)
#       path, costs = greedy(G, pos, 0, edgeList) 
    
    # stopAnimation()

