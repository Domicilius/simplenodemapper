import yaml
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

class Node(yaml.YAMLObject):
  yaml_tag = u'!Node'
  def __init__(self, name, position, edges):
    self.name = name
    self.position = position
    self.edges = edges

  def __repr__(self):
    return "%s(name=%r, position=%r, edges=%r)" % (self.__class__.__name__, self.name, self.position, self.edges)

edgelist=[]
pos = []
with open("nodedata.yaml", 'r') as stream:
  for data in yaml.load_all(stream):
    if data.edges:
      for i in data.edges:
        edgelist.append((data.name, i))
    newpos = list(data.position)
    pos[data] = newpos

G.add_edges_from(edgelist)

#pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=2000, node_shape='s')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=20, front_family='sans-serif')

print(pos)

plt.axis('off')
plt.show()