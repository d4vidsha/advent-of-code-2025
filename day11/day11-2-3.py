
def main():
    lines = [line for line in fp.read().split("\n")[:-1]]
    input = {}
    for line in lines:
        k, v = line.split(":")
        input[k.strip()] = v.strip().split()
    print(input)
    input["out"] = []

    dp = {}
    def dfs(curr, end):
        if (curr, end) in dp:
            return dp[(curr, end)]
        if curr == end:
            return 1
        ways = 0
        for item in input[curr]:
            ways += dfs(item, end)
        dp[(curr, end)] = ways
        return ways
    svr_fft = dfs("svr", "fft")
    fft_dac = dfs("fft", "dac")
    dac_out = dfs("dac", "out")
    return svr_fft * fft_dac * dac_out


    # res = dfs("svr", "dac")
    # res = dfs("dac", "fft") # is 0 in test cases, meaning that fft always comes before dac
    # res = dfs("fft", "out")
    #

if __name__ == "__main__":
    fp = open("input11.txt", "r")
    print(main())
    fp.close()
