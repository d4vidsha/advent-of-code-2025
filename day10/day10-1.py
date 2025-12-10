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
        joltage = ast.literal_eval(line[i:])
        input.append((light_diagram, schematics, joltage))
    print(input)
    
    ### the code, takes 1 min to run on the input

    res = 0
    n = len(input)
    for i in range(n):
        light_diagram, schematics, joltage = input[i]
        start = "." * len(light_diagram)

        queue = deque([(start, 0)])
        while queue:
            diagram, ops = queue.popleft()
            if diagram == light_diagram:
                res += ops
                break
            for j in range(len(schematics)):
                new_diagram = apply(schematics[j], diagram)
                queue.append((new_diagram, ops + 1))
    
    return res

def apply(schematic, diagram):
    for i in range(len(schematic)):
        if diagram[schematic[i]] == "#":
            diagram = diagram[:schematic[i]] + "." + diagram[schematic[i]+1:]
        elif diagram[schematic[i]] == ".":
            diagram = diagram[:schematic[i]] + "#" + diagram[schematic[i]+1:]
    return diagram

if __name__ == "__main__":
    fp = open("input10.txt")
    print(main())
    fp.close()
