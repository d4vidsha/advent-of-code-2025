import math
import heapq

def main():

    coords = [tuple([int(d) for d in i.split(",")]) for i in fp.read().split("\n")[:-1]]
    # print(coords)

    n = len(coords)
    link = [i for i in range(n)]
    size = [1] * n

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


    pq = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2 + (coords[i][2] - coords[j][2]) ** 2)
            heapq.heappush(pq, (dist, i, j))

    # pop n of them
    for i in range(n):
        _, x, y = heapq.heappop(pq)
        # print(size)
        # print(link)
        # print(x, y)
        # print(find(x), find(y))
        if find(x) != find(y):
            union(x, y)
            # print("not same so union")

    # print(size)
    # print(link)
    # print(len(set(link)))
    # print(find(7))

    # find the subgraphs
    print(size)
    subgraph_sizes = []
    for i in range(n):
        # is subgraph
        if i == link[i]:
            subgraph_sizes.append(size[i])

    print(subgraph_sizes)
    # find the top 3
    subgraph_sizes.sort(reverse=True)
    res = 1
    for i in range(3):
        res *= subgraph_sizes[i]
        print(subgraph_sizes[i])


    return res

if __name__ == "__main__":
    fp = open("input8.txt", "r")
    print(main())
    fp.close()
