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
            if length % 2 == 1:
                continue
            if i_str[:length // 2] == i_str[length // 2:]:
                res += i
    return res

if __name__ == "__main__":
    fp = open("input.txt", "r")
    print(main())
    fp.close()
