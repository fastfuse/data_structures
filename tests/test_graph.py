from graph import Graph


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
        assert self.graph.vertices['V5'].id == 'V5'

    def test_get_vertex(self):
        v = self.graph.get_vertex('V2')
        assert v.id == 'V2'

        assert not self.graph.get_vertex('V7')




