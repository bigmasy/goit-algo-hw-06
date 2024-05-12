from task_1 import transport_network

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get('weight', 1)  # Вага ребра
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Додаємо ваги до ребер графа
for u, v in transport_network.edges():
    transport_network[u][v]['weight'] = 1

shortest_paths = {}
for start_node in transport_network.nodes():
    shortest_paths[start_node] = dijkstra(transport_network, start_node)

# Виведення найкоротших шляхів між всіма парами вершин
for start_node in shortest_paths:
    print(f"\nНайкоротші шляхи від {start_node}:\n")
    for end_node, distance in shortest_paths[start_node].items():
        print(f"    До {end_node}: відстань = {distance}")