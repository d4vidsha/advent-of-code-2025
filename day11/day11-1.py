def main():
    lines = [line for line in fp.read().split("\n")[:-1]]
    input = {}
    for line in lines:
        k, v = line.split(":")
        input[k.strip()] = v.strip().split()
    print(input)

    res = 0

    def dfs(curr):
        nonlocal res
        if curr == "out":
            res += 1
            return
        for item in input[curr]:
            dfs(item)
    dfs("you")

    return res

if __name__ == "__main__":
    fp = open("input11.txt", "r")
    print(main())
    fp.close()
