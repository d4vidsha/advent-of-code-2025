def main():
    file = fp.read()
    numbers = [[int(d) for d in line.split(" ") if d != ""] for line in file.split("\n")[:-2]]
    print(numbers)
    operations = [s for s in file.split("\n")[-2].split(" ") if s != ""]
    print(operations)

    res = 0
    for i in range(len(numbers[0])):
        if operations[i] == "*":
            partial = 1
            for j in range(len(numbers)):
                partial *= numbers[j][i]
            res += partial
        elif operations[i] == "+":
            partial = 0
            for j in range(len(numbers)):
                partial += numbers[j][i]
            res += partial
    return res

if __name__ == "__main__":
    fp = open("input6.txt", "r")
    print(main())
    fp.close()
