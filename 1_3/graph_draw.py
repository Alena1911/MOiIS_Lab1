import networkx as nx
import matplotlib.pyplot as plt
import random
import networkx.algorithms.community.label_propagation as lp


graph = nx.read_gml("sample_graph.gml")

comple_g = lp.label_propagation_communities(graph)
colors = [0 for i in range(len(graph.nodes))]

for color in comple_g.mapping:
    _color = comple_g.mapping[color]
    for node in _color:
        colors[list(graph.nodes).index(node)] = color

# В файл уже записаны позиции для отрисовки (граф был сгенерирован networkx)
pos = nx.get_node_attributes(graph, "pos")

# отрисуем граф
plt.figure(figsize=(8, 8))
nx.draw_networkx_edges(graph, pos, alpha=0.4)
nx.draw_networkx_nodes(
    graph,
    pos,
    nodelist=graph.nodes,
    node_size=80,
    node_color=colors,
    cmap=plt.cm.tab20,
)
plt.show()