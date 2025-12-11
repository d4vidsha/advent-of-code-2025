def main():
    lines = [line for line in fp.read().split("\n")[:-1]]
    input = {}
    for line in lines:
        k, v = line.split(":")
        input[k.strip()] = v.strip().split()
    print(input)

    res = 0

    topsort = []
    states = [0] * len(input)
    
    topsort.append()


    return res

if __name__ == "__main__":
    fp = open("input11-small-2.txt", "r")
    print(main())
    fp.close()
