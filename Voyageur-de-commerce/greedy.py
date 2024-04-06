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

    minVisited = maxsize
    minVisitedNode = None
    for node in neighbors:
        if (dataNodes[node[0]] < minVisited):
            minVisited = dataNodes[node[0]]
            minVisitedNode = node

    sameNbVisitedNodes = [minVisitedNode]
    for node in neighbors:
        if (dataNodes[minVisitedNode[0]] == dataNodes[node[0]]):
            sameNbVisitedNodes.append(node)


    minWeight = maxsize
    nextNode = None
    for node in sameNbVisitedNodes:
        if (node[1] < minWeight):
            nextNode = node[0]
            minWeight = node[1]

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
    animation(G, pos, 0.5, "red")

    while not (IsGraphCompletelyVisited(dataNodes)):
        neighbors = getNeighbors(currentNode, edges)
        nextNode, cost = getNextNode(neighbors, dataNodes, path)
        costs.append(cost)
        dataNodes[nextNode] = dataNodes[nextNode] + 1
        path.append((currentNode, nextNode))
        visitedNodes.append(currentNode)
        currentNode = nextNode
        animation(G, pos, 0.5, "red", currentNode, visitedNodes, path)

    dk = nx.dijkstra_path(G, currentNode, startNode)
    returnPath = []
    for i in range(len(dk)):
        try:
            returnPath.append((dk[i], dk[i+1]))
        except:
            break

    for edge in edges:
        if ((edge[0], edge[1]) in returnPath):
            costs.append(edge[2])
        if ((edge[1], edge[0]) in returnPath):
            costs.append(edge[2])

    animation(G, pos, 2, "red", currentNode, visitedNodes, path)
    drawPath(G, pos, returnPath, 2, "blue")
    costs = round(sum(costs), 2)
    print(costs)
    return path, costs, returnPath
