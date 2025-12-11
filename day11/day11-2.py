def main():
    lines = [line for line in fp.read().split("\n")[:-1]]
    input = {}
    for line in lines:
        k, v = line.split(":")
        input[k.strip()] = v.strip().split()
    print(input)

    def dfs(curr):
        dac = 0
        fft = 0
        if curr == "out":
            print("out")
            return 1, 0, 0
        if curr == "dac":
            dac = 1
        if curr == "fft":
            fft = 1
        waysdac = 0
        waysfft = 0
        for next in input[curr]:
            ways, nextdac, nextfft = dfs(next)
            if dac < nextdac:
                dac = nextdac
                waysdac = ways
            if fft < nextfft:
                fft = nextfft
                waysfft = ways
        print(curr, waysdac, waysfft, dac, fft)
        if dac == 1 and fft == 0:
            return waysdac, dac, fft
        elif dac == 0 and fft == 1:
            return waysfft, dac, fft
        elif dac == 1 and fft == 1:
            return 0, dac, fft
        return 0, dac, fft
        
    res, dac, fft = dfs("svr")
    print(res, dac, fft)
    if not dac and not fft:
        return "NOTHING"
    return res

if __name__ == "__main__":
    fp = open("input11-small-3.txt", "r")
    print(main())
    fp.close()
