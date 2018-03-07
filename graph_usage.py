"""
Usage of Graph
"""

from graph import Graph
from collections import deque


# ===========================================================================
# Case 1
# Breadth first search
# ===========================================================================

def build_graph(word_file):
    """
    Function to build words graph.

    TODO: REFACTOR!
    """
    words = dict()  # defauldict
    words_graph = Graph()

    # create buckets of words that differ by one letter
    with open(word_file, 'r') as w_file:
        for line in w_file.readlines():
            word = line.strip()
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in words:
                    words[bucket].append(word)
                else:
                    words[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in words.keys():
        for word1 in words[bucket]:
            for word2 in words[bucket]:
                if word1 != word2:
                    words_graph.add_edge(word1, word2)

    return words_graph


def bfs(start_vertex):
    """
    Breadth first search.

    :param start_vertex: vertex to start search.
    """
    start_vertex.distance = 0
    start_vertex.previous = None

    vertices_q = deque()
    vertices_q.append(start_vertex)

    while len(vertices_q) > 0:
        current_vertex = vertices_q.pop()

        for nbr in current_vertex.get_connections():
            if nbr.color == 'white':
                nbr.color = 'gray'
                nbr.distance = current_vertex.distance + 1
                nbr.previous = current_vertex
                vertices_q.append(nbr)

        current_vertex.color = 'black'


def traverse(y):
    x = y
    while x.previous:
        print(x.id)
        x = x.previous
    print(x.id)


if __name__ == '__main__':
    wg = build_graph('words.txt')

    start = wg.get_vertex('FOOL')

    bfs(start)

    traverse(wg.get_vertex('POLE'))

