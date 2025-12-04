MOD = 100
def main():
    curr = 50
    res = 0
    while line := fp.readline():
        if line == "\n":
            break
        rotation = line[:-1]
        num = int(rotation[1:])
        if rotation[0] == "L":
            while num != 0:
                curr -= 1
                curr %= MOD
                num -= 1
                if curr == 0:
                    res += 1
        elif rotation[0] == "R":
            while num != 0:
                curr += 1
                curr %= MOD
                num -= 1
                if curr == 0:
                    res += 1
    return res

if __name__ == "__main__":
    fp = open("input-2.txt", "r")
    print(main())
    fp.close()

