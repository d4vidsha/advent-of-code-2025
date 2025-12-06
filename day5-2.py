def main():
    ranges = []
    while line := fp.readline()[:-1]:
        ranges.append(tuple([int(i) for i in line.split("-")]))
    
    ids = [int(i) for i in fp.read().split("\n")[:-1]]
    print(ids)
    ranges.sort()
    print(ranges)

    res = 0 

    # only include ranges that matter
    new_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        if new_ranges[-1][1] >= ranges[i][1]:
            continue
        new_ranges.append(ranges[i])
    print(new_ranges)

    ranges = new_ranges
    for i in range(len(ranges)):
        # #check if previous one covered the whole range
        # if i >= 1 and ranges[i][1] <= ranges[i-1][1]:
        #     continue
        # if last range
        if i == len(ranges) - 1:
            res += ranges[-1][1] - ranges[-1][0] + 1
            continue
        if ranges[i][1] < ranges[i+1][0]:
            res += ranges[i][1] - ranges[i][0] + 1
        elif ranges[i][1] == ranges[i+1][0]:
            res += ranges[i][1] - ranges[i][0]
        elif ranges[i+1][0] < ranges[i][1] and ranges[i][1] < ranges[i+1][1]:
            res += ranges[i+1][0] - ranges[i][0]
        # elif ranges[i+1][1] <= ranges[i][1]:
        #     res += ranges[i][1] - ranges[i][0] + 1
        print(ranges[i], res)
    # res += ranges[-1][1] - ranges[-1][0] + 1

    # if ranges[-1][0] < ranges[-2][1] and ranges[-2][1] <= ranges[-1][1]:
    #     res += ranges[-1][1] - ranges[-2][1]
    # elif ranges[-2][1] <= ranges[-1][0]:
    #     res += ranges[-1][1] - ranges[-1][0] + 1
    print(ranges[-1], res)
    return res

if __name__ == "__main__":
    fp = open("input5.txt", "r")
    print(main())
    fp.close()
