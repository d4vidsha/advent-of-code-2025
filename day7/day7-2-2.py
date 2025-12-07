def main():
    # initialise
    line = fp.readline()[:-1]
    beams = [1 if line[i] == "S" else 0 for i in range(len(line))]
    splitters = fp.read().split("\n")[:-1]

    # constant O(1) dp
    curr = beams
    n = len(splitters[0])
    while len(splitters) != 1:
        next = curr.copy()
        for i in range(n):
            if splitters[1][i] == "^" and curr[i] > 0:
                next[i] = 0
                next[i-1] += curr[i]
                next[i+1] += curr[i]
        splitters = splitters[2:]
        curr = next
    return sum(curr)

if __name__ == "__main__":
    fp = open("input7.txt", "r")
    print(main())
    fp.close()
