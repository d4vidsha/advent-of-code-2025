def main():
    ranges = []
    while line := fp.readline()[:-1]:
        ranges.append(tuple([int(i) for i in line.split("-")]))
    
    ids = [int(i) for i in fp.read().split("\n")[:-1]]
    print(ids)
    ranges.sort()
    print(ranges)

    res = 0 

    for id in ids:
        for i in range(len(ranges)):
            if ranges[i][0] <= id and id <= ranges[i][1]:
                print(id)
                res += 1
                break

            # if i+1 < len(ranges) and id >= ranges[i+1][0]:
            #     if id <= ranges[i+1][1]:
            #         print(id)
            #         res += 1
            #     continue
            # if ranges[i][0] <= id and id <= ranges[i][1]:
            #     print(id)
            #     res += 1
        #         break
        #     if l < id and id < r:
        #
        # j = 0
        # while j < len(ranges) and ranges[j][0] <= ids[i]:
        #     j += 1
        # # if ranges[j-1][1] < ids[i] and ids[i] < ranges[j][0]:
        # if j == 0:
        #     continue
        # if ids[i] <= ranges[j-1][1]:
        #     print(ids[i])
        #     res += 1

    return res

if __name__ == "__main__":
    fp = open("input5.txt", "r")
    print(main())
    fp.close()
