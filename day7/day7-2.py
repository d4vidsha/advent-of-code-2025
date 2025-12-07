def main():
    # initialise
    line = fp.readline()[:-1]
    beam = None
    for i in range(len(line)):
        if line[i] == "S":
            beam = i

    splitters = fp.read().split("\n")[:-1]

    def dfs(splitters, beam, trace):
        # print(splitters, beam, trace)
        if len(splitters) == 1:
            # print(splitters, beam, trace)
            # print("final: 1")
            return 1
        line = splitters[1]
        if 0 <= beam and beam < len(splitters[0]) and line[beam] == "^":
            res1 = dfs(splitters[2:], beam-1, trace + [beam])
            res2 = dfs(splitters[2:], beam+1, trace + [beam])
            res = res1+res2
            # print(splitters, beam, trace)
            # print(f"going: {res1} + {res2} = {res1+res2}")
            return res
        # print(splitters, beam, trace)
        return 0

    return dfs(splitters, beam, [])


if __name__ == "__main__":
    fp = open("input7.txt", "r")
    print(main())
    fp.close()
