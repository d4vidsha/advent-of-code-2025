def main():
    res = 0
    line = fp.readline()
    ranges = line[:-1].split(",")
    for section in ranges:
        start, end = section.split("-")
        start = int(start)
        end = int(end)
        print(start, end)
        for i in range(start, end+1):
            i_str = str(i)
            length = len(i_str)
            for j in range(1, length // 2 + 1):
                k = 0
                not_possible = False
                for k in range(j, length, j):
                    if i_str[:j] != i_str[k:j+k]:
                        not_possible = True
                        break
                    # print(j, k, length, i_str[:j], i_str[k:j+k])
                if not not_possible:
                    print(i)
                    res += i
                    break
    return res


if __name__ == "__main__":
    fp = open("input.txt", "r")
    print(main())
    fp.close()
