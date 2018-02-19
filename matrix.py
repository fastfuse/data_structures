class Matrix2D:
    """
    Class represents a two-dimensional array.
    """

    def __init__(self, rows, cols):
        self._matrix = [[(x, y) for y in range(cols)] for x in range(rows)]

        # self._matrix = tuple(
        #     [tuple([(x, y) for y in range(cols)]) for x in range(rows)])

    def row(self, start, finish=None):
        try:
            if not finish:
                return [self._matrix[start]]

            return [self._matrix[r] for r in range(start, finish + 1)]

        except IndexError:
            return "No such row"

    def col(self, start, finish=None):
        try:
            if not finish:
                return [row[start] for row in self._matrix]

            return [[row[i] for i in range(start, finish + 1)] for row in
                    self._matrix]

        except IndexError:
            return "No such column"

    def dump(self):
        return self._matrix

    def __repr__(self):
        return '\n'.join(map(str, self._matrix))
