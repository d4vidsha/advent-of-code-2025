def main():
    input = [tuple([int(j) for j in i.split(",")]) for i in fp.read().split("\n")[:-1]]

    res = 0

    for i in range(len(input)):
        for j in range(i+1, len(input)):
            size = (abs(input[i][0] - input[j][0]) + 1) * (abs(input[i][1] - input[j][1]) + 1)
            res = max(res, size)

    return res

if __name__ == "__main__":
    fp = open("input9.txt", "r")
    print(main())
    fp.close()
