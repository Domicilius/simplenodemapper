import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
with open('testdata', 'r') as f:
  for line in f.readlines():
    (source, dest, weight) = line.split(', ') 
    G.add_edge(source, dest, weight=int(weight))

pos = nx.shell_layout(G)


edge_labels = dict([((u,v), d['weight']) for u,v,d in G.edges(data=True)])

nx.draw_networkx_nodes(G, pos, node_size=2000, node_shape='s')
nx.draw_networkx_edges(G, pos)

nx.draw_networkx_labels(G, pos, font_size=20, front_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

print(pos)

plt.axis('off')
plt.show()
