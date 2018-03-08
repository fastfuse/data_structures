"""
Usage of Graph
"""

from graph import Graph

# ===========================================================================
# Case 2
# Knights Tour problem
# ===========================================================================


def build_knight_moves_graph(board_size):
    """
    Function to build graph w/ legal knight moves.

    :param board_size: size of the board.
    :return: graph
    """
    knight_moves_graph = Graph()

    # helper to convert (x, y) coordinates to number
    to_node_id = lambda row, col, board_size: (row * board_size) + col

    for row in range(board_size):
        for col in range(board_size):
            node_id = to_node_id(row, col, board_size)

            moves = get_legal_moves(row, col, board_size)

            for m in moves:
                move = to_node_id(m[0], m[1], board_size)
                knight_moves_graph.add_edge(node_id, move)

    return knight_moves_graph


# def to_node_id(row, column, board_size):
#     return (row * board_size) + column


# def is_legal(coord, board_size):
#     return 0 <= coord < board_size


def get_legal_moves(x, y, board_size):
    """
    Function to generate list of legal moves of the Knight.
    """
    moves = []
    move_offsets = [
        (-1, -2), (-1, 2), (-2, -1), (-2, 1),
        (1, -2), (1, 2), (2, -1), (2, 1)]

    # helper to check whether coordinate is legal
    is_legal = lambda coord, board_size: 0 <= coord < board_size

    for item in move_offsets:
        new_x = x + item[0]
        new_y = y + item[1]

        if is_legal(new_x, board_size) and is_legal(new_y, board_size):
            moves.append((new_x, new_y))

    return moves


def order_by_available(vertex):
    """
    Function to sort available nodes in desc order
    """
    result = []

    for v in vertex.get_connections():
        if v.color == 'WHITE':
            c = 0

            for w in v.get_connections():
                if w.color == 'WHITE':
                    c += 1
            result.append((c, v))

    result.sort(key=lambda x: x[0])

    return [y[1] for y in result]


def knight_tour(depth, path, target, limit):
    """
    Function to build knight's tour.

    :param depth: current depth in graph.
    :param path: list of visited vertices.
    :param target: vertex to explore.
    :param limit: required number of nodes in the path
    """
    target.color = 'GRAY'
    path.append(target)

    if depth < limit-1:
        nbr_list = target.get_connections()
        i = 0
        done = False

        while i < len(nbr_list) and not done:
            if nbr_list[i].color == 'WHITE':
                done = knight_tour(depth + 1, path, nbr_list[i], limit)
            i += 1

        if not done:  # prepare to backtrack
            path.pop()
            target.color = 'WHITE'
    else:
        done = True
    return done


def knight_tour_optimized(depth, path, target, limit):
    """
    Function to build knight's tour.

    :param depth: current depth in graph.
    :param path: list of visited vertices.
    :param target: vertex to explore.
    :param limit: required number of nodes in the path
    """
    target.color = 'GRAY'
    path.append(target)

    if depth < limit-1:
        nbr_list = order_by_available(target)
        i = 0
        done = False

        while i < len(nbr_list) and not done:
            if nbr_list[i].color == 'WHITE':
                done = knight_tour(depth + 1, path, nbr_list[i], limit)
            i += 1

        if not done:  # prepare to backtrack
            path.pop()
            target.color = 'WHITE'
    else:
        done = True
    return done

if __name__ == '__main__':

    # knight_moves = build_knight_moves_graph(8)

    # g = Graph()
    # g.add_vertex('A')
    # g.add_vertex('B')
    # g.add_vertex('C')
    # g.add_vertex('D')
    # g.add_vertex('E')
    # g.add_vertex('F')
    #
    # g.add_edge('A', 'B')
    # g.add_edge('A', 'D')
    # g.add_edge('B', 'D')
    # g.add_edge('B', 'C')
    # g.add_edge('D', 'E')
    # g.add_edge('E', 'B')
    # g.add_edge('E', 'F')
    # g.add_edge('F', 'C')

    kg = build_knight_moves_graph(8)

    path = list()
    start = kg.get_vertex(0)

    t = knight_tour_optimized(0, path, start, 64)

    print()
