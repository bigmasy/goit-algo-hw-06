import networkx as nx
import matplotlib.pyplot as plt


transport_network = nx.Graph()

stops = ['Зупинка 1', 'Зупинка 2','Зупинка 3', 'Зупинка 4',
         'Зупинка 5', 'Зупинка 6', 'Зупинка 7', 'Зупинка 8',
         'Зупинка 9', 'Зупинка 10', 'Зупинка 11', 'Зупинка 12']

transport_network.add_nodes_from(stops)

routes_1 = [
    ('Зупинка 2', 'Зупинка 1', {'route':'1'}),
    ('Зупинка 1', 'Зупинка 11', {'route':'1'}),
    ('Зупинка 11', 'Зупинка 4', {'route':'1'}),
    ('Зупинка 4', 'Зупинка 10', {'route':'1'}),
    ('Зупинка 10', 'Зупинка 12', {'route':'1'}),
]

routes_2 = [
    ('Зупинка 1', 'Зупинка 6', {'route':'2'}),
    ('Зупинка 6', 'Зупинка 11', {'route':'2'}),
    ('Зупинка 11', 'Зупинка 2', {'route':'2'}),
    ('Зупинка 2', 'Зупинка 3', {'route':'2'}),
    ('Зупинка 3', 'Зупинка 9', {'route':'2'}),
    ('Зупинка 9', 'Зупинка 4', {'route':'2'}),
    ('Зупинка 4', 'Зупинка 12', {'route':'2'}),
]

routes_3 = [
    ('Зупинка 1', 'Зупинка 7', {'route':'3'}),
    ('Зупинка 7', 'Зупинка 8', {'route':'3'}),
    ('Зупинка 8', 'Зупинка 9', {'route':'3'}),
    ('Зупинка 9', 'Зупинка 11', {'route':'3'}),
    ('Зупинка 11', 'Зупинка 3', {'route':'3'}),
]

routes_4 = [
    ('Зупинка 5', 'Зупинка 6', {'route':'4'}),
    ('Зупинка 6', 'Зупинка 7', {'route':'4'}),
    ('Зупинка 7', 'Зупинка 11', {'route':'4'}),
    ('Зупинка 11', 'Зупинка 10', {'route':'4'}),
    ('Зупинка 10', 'Зупинка 3', {'route':'4'}),
]
transport_network.add_edges_from(routes_1)

transport_network.add_edges_from(routes_2)

transport_network.add_edges_from(routes_3)

transport_network.add_edges_from(routes_4)

pos = nx.spring_layout(transport_network)

# Візуалізація графа
nx.draw(transport_network, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=8)
labels = nx.get_edge_attributes(transport_network, 'route')
nx.draw_networkx_edge_labels(transport_network, pos, edge_labels=labels)
plt.title("Transport Network")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", transport_network.number_of_nodes())
print("Кількість ребер:", transport_network.number_of_edges())
print("Ступінь вершин:")
for node in transport_network.nodes():
    print(f"{node}: {transport_network.degree[node]}")
