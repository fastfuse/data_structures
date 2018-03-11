from queue import PriorityQueue
from graph import Graph, Vertex


def dijkstra_path(input_graph: Graph, start_vertex: Vertex):
    """
    Dijkstra's path.

    Build path from start_vertex to all other vertices in input_graph

    TODO: refactor
    """

    start_vertex.distance = 0
    vertices_q = PriorityQueue()

    for i in [(vertex.distance, vertex) for vertex in input_graph]:
        vertices_q.put(i)

    while not vertices_q.empty():
        current = vertices_q.get()[1]
        current.color = 'BLACK'

        for nbr in current.get_connections():
            if nbr.color == 'WHITE':
                new_dist = current.distance + current.get_weight(nbr)

                if new_dist < nbr.distance:
                    nbr.distance = new_dist
                    nbr.previous = current

                print(f'{current.id} -> {nbr.id} : {new_dist}')

        while not vertices_q.empty():
            vertices_q.get()

        unvisited = [(vertex.distance, vertex) for vertex in input_graph if
                     vertex.color == 'WHITE']

        for i in unvisited:
            vertices_q.put(i)


def traverse_shortest(target_node):
    """
    Function to build shortest path from start to target node.
    """
    path = list()

    while target_node.previous:
        path.append(target_node.id)
        target_node = target_node.previous
    path.append(target_node.id)

    return list(reversed(path))


if __name__ == '__main__':
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    dijkstra_path(g, g.get_vertex('a'))

    print(f'Shortest path:')
    print(' -> '.join(traverse_shortest(g.get_vertex('e'))))
