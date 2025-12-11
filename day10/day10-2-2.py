import math
import ast
def main():
    lines = fp.read().split("\n")[:-1]
    input = []
    for line in lines:
        i = 0
        light_diagram = ""
        while line[i] != "]":
            if line[i] in "#.":
                light_diagram += line[i]
            i += 1
        j = i
        while line[i] != "{":
            i += 1
        schematics = ast.literal_eval(("(" + ",".join(line[j+1:i].strip().split(" ")) + ")").replace("(", "[").replace(")", "]"))
        joltage = ast.literal_eval(line[i:].replace("{", "[").replace("}", "]"))
        input.append((light_diagram, schematics, joltage))
    print(input)
    
    ### the code, takes 1 min to run on the input

    res = 0
    n = len(input)

    for i in range(n):
        _, schematics, joltage = input[i]
        print("solve", joltage, schematics)
        res += solve(joltage, schematics)
    return res

def solve(joltage, schematics):
    target = tuple([0] * len(joltage))
    dp = {}

    def counts(joltage):
        # schematics is the same per row of input
        for i in range(len(joltage)):
            if joltage[i] < 0:
                return math.inf
        if joltage == target:
            # print("solved!", joltage)
            return 0
        if joltage in dp:
            return dp[joltage]
        best = math.inf
        for i in range(len(schematics)):
            best = min(best, counts(apply(schematics[i], joltage)) + 1)
        # print("result", joltage, best)
        dp[joltage] = best
        return best

    return counts(tuple(joltage))


def apply(schematic, joltage):
    joltage = list(joltage)
    for i in range(len(schematic)):
        joltage[schematic[i]] -= 1
    return tuple(joltage)

if __name__ == "__main__":
    fp = open("input10.txt")
    print(main())
    fp.close()
