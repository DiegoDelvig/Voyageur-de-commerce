import networkx as nx
import matplotlib.pyplot as plt
import random

def genetic(edgeList,dataList,show,hasWeight):
   nodeArray = list(dataList.keys())

   G  = nx.Graph()
   G.add_weighted_edges_from(edgeList) 
   nx.draw_spring(G,with_labels=True)
   pos = nx.spring_layout(G)

   # ALGO
   currentNode = nodeArray[0]
   path = [currentNode]
   visitedEdge = []
   nbVisitedNode = 0
   round = 0
   totalWeight = 0

   plt.ion()

   while (len(nodeArray) > nbVisitedNode ):
      round +=1 

      possibleNextNodes = []
      for edge in edgeList:
         if (edge[0] == currentNode):
            possibleNextNodes.append([edge[1],edge[2]])
         if (edge[1] == currentNode):
            possibleNextNodes.append([edge[0],edge[2]])

      def calcNodeScore(edge):
         node = edge[0]
         weight = edge[1]
         score = 0
         if (hasWeight):
            score += weight * 5
         score += dataList[node]['visitCount']
         if ( dataList[node]['discovered']):
            score +=  20
         
         score += abs(dataList[node]['lastVisit'] - round) * 0.8
         return score 

      possibleNextNodes.sort(key=calcNodeScore)
      print(possibleNextNodes[0])
      totalWeight += possibleNextNodes[0][1]
      nextNode = possibleNextNodes[0][0]
      if (dataList[nextNode]['discovered'] == False):
         nbVisitedNode += 1

      dataList[nextNode]['discovered'] = True
      dataList[nextNode]['visitCount'] += 1
      path.append(nextNode)
      visitedEdge.append((currentNode,nextNode))
      currentNode = nextNode

      if (show):
         plt.clf()
         nx.draw(G,pos, node_color='#00b4d9')
         nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
         nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))

         nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='green',node_size=200)
         nx.draw_networkx_nodes(G, pos, nodelist=[currentNode], node_color='red',node_size=300)
         nx.draw_networkx_edges(G,pos,edgelist=visitedEdge,edge_color="green",node_size=200,width=3)
         plt.pause(1)

   plt.ioff()
   return round, totalWeight


