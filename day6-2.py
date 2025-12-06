def main():
    file = fp.read()
    numbers = [[int(d) for d in line.split(" ") if d != ""] for line in file.split("\n")[:-2]]
    # print(numbers)
    numbers = file.split("\n")[:-2]
    operations = [s for s in file.split("\n")[-2].split(" ") if s != ""]
    print(operations)
    res = 0
    operation_idx = 0
    if operations[operation_idx] == "*":
        partial = 1
    else:
        partial = 0


    # add one more space to each input
    numbers = [line + " " for line in numbers]

    for i in range(len(numbers[0])):
        val = ""
        for j in range(len(numbers)):
            val += numbers[j][i]
        if val.strip() == "":
            # new operation
            print(partial)
            res += partial
            operation_idx += 1
            if operation_idx >= len(operations):
                continue
            if operations[operation_idx] == "*":
                partial = 1
            else:
                partial = 0
            continue
        val = int(val.strip())
        print(val)
        if operations[operation_idx] == "*":
            partial *= val
        else:
            partial += val
    return res

if __name__ == "__main__":
    fp = open("input6.txt", "r")
    print(main())
    fp.close()
