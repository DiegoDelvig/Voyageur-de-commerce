import networkx as nx
import matplotlib.pyplot as plt

def drawPath(G, pos, path):
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=G.edges(),
        node_size=200,
        width=1,
    )

def animation(G, pos, timeStep, currentNode=None, visitedNodes=None, path=None):
    """
    Create animation, changing the state of the graph every step:
    """
     
    plt.clf()
    plt.ion()
    nx.draw(G,pos, node_color='#00b4d9')
    drawPath(G, pos, G.edges())
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))
    
    if (visitedNodes != None) :
        nx.draw_networkx_nodes(G, pos, nodelist=visitedNodes, node_color='green',node_size=200)
    if (currentNode != None) :
        nx.draw_networkx_nodes(G, pos, nodelist=[currentNode], node_color='yellow',node_size=200)
    if (path != None) :
        nx.draw_networkx_edges(G,pos,edgelist=path,edge_color="red",node_size=200,width=2)

    plt.pause(timeStep)


def stopAnimation():
    plt.ioff()
    plt.show()
