from sys import maxsize
from display import *


def IsGraphCompletelyVisited(dataNodes):
    for node in dataNodes:
        if (dataNodes[node] == 0):
            return False
    return True


def getNeighbors(currentNode, edges):
    neighbors = []
    for edge in edges:
        if (currentNode == edge[0]):
            neighbors.append((edge[1], edge[2]))

        if (currentNode == edge[1]):
            neighbors.append((edge[0], edge[2]))
    return neighbors


def getNextNode(neighbors, dataNodes, path):
    
    nextNode = None

    minWeight = maxsize
    sameVisitedScoreNodes = []    
   
    # if there is more than 1 neighbor, remove last node use
    if (len(path) != 0 and len(neighbors) > 1):

        for node in neighbors:
            if (path[-1][0] == node[0]):
                neighbors.remove(node)

    # get the neighbors that has been visited the same times 
    minVisited = maxsize 
    if not dataNodes[neighbors[0][0]] == 0:
        minVisited = dataNodes[neighbors[0][0]] 

    for node in neighbors:
        if (dataNodes[node[0]] < minVisited):
            minVisited = dataNodes[node[0]]
            sameVisitedScoreNodes.append(node)
    
    if (len(sameVisitedScoreNodes) == 0):
        sameVisitedScoreNodes.append(neighbors[0])

    
    # get the less far neighbor 
    for node in sameVisitedScoreNodes:
        if (node[1] < minWeight):
            minWeight = node[1]
            nextNode = node[0]
    
    return nextNode, minWeight




def greedy(G, pos, startNode, edges):
    currentNode = startNode
    path = [] 
    visitedNodes = []
    costs = []
    dataNodes = {} 
    for i in range(len(G.nodes())):
        dataNodes[i] = 0

    dataNodes[startNode] = dataNodes[startNode] + 1

    while not (IsGraphCompletelyVisited(dataNodes)):
        neighbors = getNeighbors(currentNode, edges)
        nextNode, cost = getNextNode(neighbors, dataNodes, path)
        costs.append(cost) 
        dataNodes[nextNode] = dataNodes[nextNode] + 1
        path.append((currentNode, nextNode)) 
        visitedNodes.append(currentNode)
        currentNode = nextNode
        animation(G, pos, 0.5, currentNode, visitedNodes, path)
    
    costs = round(sum(costs), 2)
    print(costs) 
    return path, costs




