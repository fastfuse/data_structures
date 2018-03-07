from graph import Graph, Vertex


class SetupTeardownMixin:
    def setup_method(self):
        self.graph = Graph()

        self.graph.add_vertex('V1')
        self.graph.add_vertex('V2')
        self.graph.add_vertex('V3')
        self.graph.add_vertex('V4')


class TestGraph(SetupTeardownMixin):
    def test_add_vertex(self):
        assert self.graph.vertices_count == 4

        self.graph.add_vertex('V5')
        assert self.graph.vertices_count == 5
        assert self.graph.vertices[-1] == 'V5'

    def test_get_vertex(self):
        v = self.graph.get_vertex('V2')
        assert v.id == 'V2'

        assert not self.graph.get_vertex('V7')

    def test_add_edge(self):
        self.graph.add_edge('V6', 'V7', weight=5)

        assert 'V6' in self.graph
        assert 'V7' in self.graph

        v6 = self.graph.get_vertex('V6')
        v7 = self.graph.get_vertex('V7')

        assert v7 in v6.get_connections()

    def test_get_vertices(self):
        assert self.graph.vertices == ['V1', 'V2', 'V3', 'V4']
