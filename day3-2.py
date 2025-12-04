length = 12

def main():
    res = 0
    while line := fp.readline():
        banks = list(line[:-1])
        n = len(banks)
        removable = n - length
        stack = [banks[0]]
        for i in range(1, len(banks)):
            print(stack, removable, stack[-1], banks[i])
            while removable > 0 and stack and stack[-1] < banks[i]:
                stack.pop()
                removable -= 1
            stack.append(banks[i])
            print(stack)
        res += int("".join(stack[:length]))

    return res


# def main():
#     res = 0
#     while line := fp.readline():
#         banks = list(line[:-1])
#         picked = 0
#         new = [""] * len(banks)
#         for i in range(9, -1, -1):
#             for j in range(len(banks)-1, -1, -1):
#                 if picked >= length:
#                     break
#                 if str(i) == banks[j]:
#                     new[j] = banks[j]
#                     picked += 1
#         print(new)
#         res += int("".join(new))
#     return res

# def main():
#     res = 0
#     while line := fp.readline():
#         banks = line[:-1]
#         best_joltage = 0
#         banks = list(banks)
#         for i in range(length, len(banks)):
#             candidates = "".join(banks[:i+1])
#             print("candidates:", candidates, i)
#             for j in range(length+1):
#                 print(int("".join(candidates[:j]) + "".join(candidates[j:])))
#                 if (joltage := int("".join(candidates[:j]) + "".join(candidates[j:]))) > best_joltage:
#                     best_joltage = joltage
#                     remove = j
#             banks[remove] = ""
#             print(banks)
#         print(best_joltage)
#         res += best_joltage
#     return res

if __name__ == "__main__":
    fp = open("input3.txt")
    print(main())
    fp.close()
