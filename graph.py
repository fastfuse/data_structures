"""
Graph Data Structure.
"""


class Vertex:
    """
    Class represents a vertex (aka Node) of the Graph.
    """
    def __init__(self, name):
        self._id = name
        self.connections = {}
        self._color = 'white'
        self._distance = 0
        self._prev = None

    def add_connection(self, vertex, weight=0):
        """
        Add new connection.

        :param vertex: vertex to connect with.
        :param weight: weight of connection.
        """
        self.connections[vertex] = weight

    def get_connections(self):
        return list(self.connections.keys())

    def get_weight(self, vertex):
        """
        Get a weight of connection (edge) w/ a vertex.
        """
        return self.connections.get(vertex)

    @property
    def id(self):
        return self._id

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_distance(self):
        return self._distance

    def set_distance(self, distance):
        self._distance = distance

    def get_prev(self):
        return self._prev

    def set_prev(self, prev):
        self._prev = prev

    color = property(get_color, set_color)
    distance = property(get_distance, set_distance)
    previous = property(get_prev, set_prev)

    def __repr__(self):
        return f"<Vertex object. ID: {self.id}>"


class Graph:
    """
    Class represents Graph data structure.

    TODO: add possibility to add existing vertex.
    """
    def __init__(self):
        self._vertices = {}
        self.vertices_count = 0

    def add_vertex(self, name):
        """
        Add new vertex to graph.

        :param name: vertex name
        """
        new_vertex = Vertex(name)
        self._vertices[name] = new_vertex
        self.vertices_count += 1

        return new_vertex

    def get_vertex(self, name):
        """
        Get vertex of a graph.

        :param name: vertex name.

        :return: vertex or None if no such vertex.
        """
        return self._vertices.get(name, None)

    def add_edge(self, from_v, to_v, weight=0):
        """
        Add new edge (connection) between two vertices.

        :param from_v: "source" vertex.
        :param to_v: "destination" vertex.
        :param weight: weight of the connection.
        """
        if from_v not in self.vertices:
            self.add_vertex(from_v)

        if to_v not in self.vertices:
            self.add_vertex(to_v)

        self._vertices[from_v].add_connection(self._vertices[to_v], weight)

    @property
    def vertices(self):
        return list(self._vertices.keys())

    def __contains__(self, item):
        return item in self.vertices

    def __iter__(self):
        return iter(self._vertices.values())
