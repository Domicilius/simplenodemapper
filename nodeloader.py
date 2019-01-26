import yaml
import networkx as nx
import matplotlib.pyplot as plt


class Node(yaml.YAMLObject):
    yaml_tag = u'!Node'

    def __init__(self, name, position, edges):
        self.name = name
        self.position = position
        self.edges = edges

    def __repr__(self):
        return "%s(name=%r, position=%r, edges=%r)" % (
            self.__class__.__name__, self.name, self.position, self.edges)


G = nx.Graph()


edgelist = []
pos = {}
with open("nodedata.yaml", 'r') as stream:
    for data in yaml.load_all(stream):
        if data.edges:
            for i in data.edges:
                edgelist.append((data.name, i))
        newpos = list(data.position)
        newpos[0] = newpos[0] * 1
        newpos[1] = newpos[1] * 1
        pos[data.name] = newpos

G.add_edges_from(edgelist)

# pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=200, node_shape='s')
nx.draw_networkx_edges(G, pos)
# nx.draw_networkx_labels(G, pos, font_size=5, font_family='sans-serif')

# plt.axis([0, 10, 0, 10])
plt.show()
