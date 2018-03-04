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

    def __repr__(self):
        return f"<Vertex object. ID: {self.id}>"


class Graph:
    """
    Class represents Graph data structure.
    """
    def __init__(self):
        self.vertices = {}
        self.vertices_count = 0

    def add_vertex(self, name):
        """
        Add new vertex to graph.

        :param name: vertex name
        """
        new_vertex = Vertex(name)
        self.vertices[name] = new_vertex
        self.vertices_count += 1

        return new_vertex

    def get_vertex(self, name):
        """
        Get vertex of a graph.

        :param name: vertex name.

        :return: vertex or None if no such vertex.
        """
        return self.vertices.get(name, None)

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

        self.vertices[from_v].add_connection(self.vertices[to_v], weight=weight)

    def get_vertices(self):
        return list(self.vertices.keys())

    def __contains__(self, item):
        return item in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())
