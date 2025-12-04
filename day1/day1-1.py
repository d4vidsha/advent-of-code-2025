def main():
    curr = 50
    res = 0
    while line := fp.readline():
        if line == "\n":
            break
        rotation = line[:-1]
        num = int(rotation[1:])
        if rotation[0] == "L":
            curr -= num
        elif rotation[0] == "R":
            curr += num
        curr %= 100
        if curr == 0:
            res += 1
    return res

if __name__ == "__main__":
    fp = open("input.txt", "r")
    print(main())
    fp.close()
