def main():
    lines = [line for line in fp.read().split("\n")[:-1]]
    input = {}
    for line in lines:
        k, v = line.split(":")
        input[k.strip()] = v.strip().split()
    print(input)

    res = 0

    def dfs(curr, dac, fft):
        nonlocal res
        if curr == "out":
            if dac == 1 and fft == 1:
                res += 1
            return
        for item in input[curr]:
            if item == "dac":
                dac = 1
            elif item == "fft":
                fft = 1
            dfs(item, dac, fft)
    dfs("svr", 0, 0)

    return res

if __name__ == "__main__":
    fp = open("input11.txt", "r")
    print(main())
    fp.close()
