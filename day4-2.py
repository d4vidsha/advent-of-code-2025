def print_list(lst):
    for l in lst:
        print(l)

def main():
    res = 0
    input = fp.read()
    input = input.split("\n")[:-1]
    input = [list(s) for s in input]
    print_list(input)
    ROWS = len(input)
    COLS = len(input[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    while True:
        new_input = input.copy()
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                print("number", input[r][c])
                if input[r][c] != '@':
                    continue
                count = 0
                for (dr, dc) in dirs:
                    if 0 <= r+dr and r+dr < ROWS and 0 <= c+dc and c+dc < COLS and input[r+dr][c+dc] == "@":
                        print(f"r+dr: {r+dr}, c+dc: {c+dc}, input[][]{input[r+dr][c+dc]}")
                        count += 1
                        new_input[r][c] = "."
                print(count)
                if count < 4:
                    total += 1
        if total == 0:
            return res
        res += total
        input = new_input

if __name__ == "__main__":
    fp = open("input4.txt", "r")
    print(main())
    fp.close()

