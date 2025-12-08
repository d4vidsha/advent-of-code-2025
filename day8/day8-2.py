import math
import heapq

def main():

    coords = [tuple([int(d) for d in i.split(",")]) for i in fp.read().split("\n")[:-1]]
    def union(x, y):
        x = find(x)
        y = find(y)
        # assume not the same circuit
        if size[x] < size[y]:
            # swap
            temp = x
            x = y
            y = temp
        # we are saying that x is the smaller subgraph/circuit
        # we want to attach y subgraph to x subgraph
        link[y] = x
        size[x] += size[y]

    def find(x):
        while link[x] != x:
            x = link[x]
        return x

    n = len(coords)
    link = [i for i in range(n)]
    size = [1] * n

    pq = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2 + (coords[i][2] - coords[j][2]) ** 2)
            heapq.heappush(pq, (dist, i, j))

    # pop until there is only one circuit
    x = 0
    y = 0
    while len(set([find(x) for x in link])) != 1:
        _, x, y = heapq.heappop(pq)
        if find(x) != find(y):
            union(x, y)
    return coords[x][0] * coords[y][0]

if __name__ == "__main__":
    fp = open("input8.txt", "r")
    print(main())
    fp.close()

