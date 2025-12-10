import ast
from collections import deque
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
        light_diagram, schematics, joltage = input[i]
        start = [0] * len(joltage)

        queue = deque([(start, 0)])
        while queue:
            curr, ops = queue.popleft()
            print(curr, ops)
            if curr == joltage:
                res += ops
                break
            for j in range(len(schematics)):
                new = apply(schematics[j], curr)
                if less(curr, joltage):
                    queue.append((new, ops + 1))
    
    return res

def less(curr, target):
    # assume curr length is same as target length
    for i in range(len(target)):
        if curr[i] >= target[i]:
            return False
    return True

def apply(schematic, joltage):
    for i in range(len(schematic)):
        joltage[schematic[i]] += 1
    return joltage

if __name__ == "__main__":
    fp = open("input10-small.txt")
    print(main())
    fp.close()
