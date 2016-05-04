import sys
import math
import PathFinder2

def pathfinder(n):

    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    elif n < 0:
        print('invalid entry')
        exit(1)
    else:
        # Initialize all entries to 0
        matrix = [[0 for i in range(n)] for j in range(n)]

        # Only one possible way to get to any vertex on the last row
        for i in range(n):
            matrix[n-1][i] = 1

        # Each vertex x can be reached by moving from a vertex below
        # or moving from a vertex to the left. Total number of ways
        # to reach x is the sum of ways to reach those two parent
        # vertices.

        for r in range(n-2, -1, -1):
            for c in range(n - 1 - r, n):
                matrix[r][c] = matrix[r][c-1] + matrix[r+1][c]

        n_ways = matrix[0][n-1]

        return n_ways

def main():

    if len(sys.argv) != 2:
        print('Usage: {} <n>'.format(sys.argv[0]))
        exit(1)

    try:
        n = int(sys.argv[1])

    except ValueError:
        print('invalid entry')
        exit(1)

    half = pathfinder(n)
    full = PathFinder2.pathfinder2(n)

    print(math.trunc(full/half))



if __name__ == '__main__':
    main()
