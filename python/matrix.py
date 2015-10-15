
m = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]


class Matrix:

    def __init__(self, list):
        self.matrix = list
        self.seq = []

    def print_out(self):
        print "[", ', '.join(map(str, self.seq)), "]"

    def print_matrix(self):
        matrix = self.matrix
        length = len(matrix[0])
        width = len(matrix)

        c = 0
        j = 0
        i = 0
        count = length * width

        while c < count:
            for a in xrange(i, length - i):
                self.seq.append(matrix[j][a])
                c += 1

            for b in xrange(j + 1, width - j):
                self.seq.append(matrix[b][a])
                c += 1

            i += 1
            j += 1

            for a1 in reversed(xrange(j - 1, a)):
                self.seq.append(matrix[b][a1])
                c += 1

            for b1 in reversed(xrange(i, b)):
                self.seq.append(matrix[b1][i - 1])
                c += 1

        self.print_out()

cl = Matrix(m)
cl.print_matrix()
