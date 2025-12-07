def main():
    # initialise
    line = fp.readline()[:-1]
    beams = set()
    for i in range(len(line)):
        if line[i] == "S":
            beams.add(i)

    res = 0
    while line := fp.readline()[:-1]:
        for i in range(len(line)):
            if line[i] == "^" and i in beams:
                beams.add(i-1)
                beams.add(i+1)
                beams.remove(i)
                res += 1
    return res

if __name__ == "__main__":
    fp = open("input7.txt", "r")
    print(main())
    fp.close()
