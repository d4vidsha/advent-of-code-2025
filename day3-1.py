def main():
    res = 0

    while line := fp.readline():
        banks = line[:-1]
        best_joltage = 0
        for i in range(len(banks)):
            for j in range(i+1, len(banks)):
                if (joltage := int(f"{banks[i]}{banks[j]}")) > best_joltage:
                    best_joltage = joltage
        res += best_joltage
        print(banks, best_joltage)
    return res

if __name__ == "__main__":
    fp = open("input3.txt")
    print(main())
    fp.close()
