import random

def getRandomNode(curr,edgeList,i):
   """Return random node from edge list that is not himself, if the edge list is empty, create a node"""
   if (len(edgeList) == 0) :
      return hex(i+ 1)
   node = edgeList[random.randint(0,len(edgeList)-1)][random.randint(0,1)]
   while node == curr:
      node = edgeList[random.randint(0,len(edgeList)-1)][random.randint(0,1)]
   return node


def genEdgeList(nbNode,density,end):
   """Gen a edge list to create a classic graph, each node is a hex value"""

   edgeList = []
   for i in range(nbNode):
      curr = hex(i)
      edgeList.append([curr,getRandomNode(curr,edgeList,i), random.randint(1,9)/10])
      if (random.random() < end) :
         pass
      edgeList.append([curr,getRandomNode(curr,edgeList,i), random.randint(1,9)/10])

      while (random.random() < density) :
         edgeList.append([curr,getRandomNode(curr,edgeList,i), random.randint(1,9)/10])
   return edgeList

   
def createGraph(nbNode: int, density: float, end: float):
    edgeList = genEdgeList(nbNode, density, end)
    dataList = {}
    
    for edge in edgeList:
      dataList[edge[0]] = {"visitCount" : 0, "lastVisit":0, "discovered":False}
      dataList[edge[1]] = {"visitCount" : 0, "lastVisit":0, "discovered":False}

    return edgeList, dataList

