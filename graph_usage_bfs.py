"""
Usage of Graph
"""

from graph import Graph
from collections import deque, defaultdict


class Queue(deque):
    def put(self, item):
        self.append(item)

    def get(self):
        return self.popleft()

    def is_empty(self):
        return len(self) == 0


# ===========================================================================
# Case 1
# Breadth first search
# ===========================================================================

def build_graph(word_file):
    """
    Function to build words graph.
    """
    words = defaultdict(list)
    words_graph = Graph()

    # create buckets of words that differ by one letter
    with open(word_file, 'r') as w_file:
        for word in w_file.readlines():
            word = word.strip()

            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                words[bucket].append(word)

    # add vertices and edges for words in the same bucket
    # TODO: REFACTOR!
    for bucket in words:
        for word1 in words[bucket]:
            for word2 in words[bucket]:
                if word1 != word2:
                    words_graph.add_edge(word1, word2)

    return words_graph


def bfs(start_vertex):
    """
    Breadth First Search.

    :param start_vertex: vertex to start search.
    """
    start_vertex.distance = 0

    vertices_q = Queue()
    vertices_q.put(start_vertex)

    while not vertices_q.is_empty():
        current_vertex = vertices_q.get()

        for nbr in current_vertex.get_connections():
            if nbr.color == 'WHITE':
                nbr.color = 'GRAY'
                nbr.distance = current_vertex.distance + 1
                nbr.previous = current_vertex
                vertices_q.put(nbr)

        current_vertex.color = 'BLACK'


def traverse(target_node):
    """
    Function to build path from start node to target node.
    """
    path = list()

    while target_node.previous:
        path.append(target_node.id)
        target_node = target_node.previous
    path.append(target_node.id)

    return list(reversed(path))


if __name__ == '__main__':

    wg = build_graph('words.txt')

    start = wg.get_vertex('FOOL')

    bfs(start)

    print(' -> '.join(traverse(wg.get_vertex('SAGE'))))
    print(' -> '.join(traverse(wg.get_vertex('PALL'))))
    print(' -> '.join(traverse(wg.get_vertex('RACE'))))
    print(' -> '.join(traverse(wg.get_vertex('RAGE'))))
