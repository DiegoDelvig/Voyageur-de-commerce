import networkx
from itertools import permutations
import sys

from display import *


def bruteforce(G, pos, startNode, edges):
    """
    Brute Force Algorithm:
    Tries every path on the graph, return the shortest one
    """

    perm = list(permutations(G.nodes()))
    minCost = sys.maxsize

    for nodes in perm:
        path = []
        for i in range(len(nodes)):
            try:
                path.append((nodes[i], nodes[i+1]))
            except:
                pass
        animation(G, pos, 0.5, "red", path=path)
        print(path)
