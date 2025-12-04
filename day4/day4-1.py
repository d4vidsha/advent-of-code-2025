import json
def main():
    res = 0
    input = fp.read()
    input = input.split("\n")[:-1]
    print(json.dumps(input, indent=2))
    ROWS = len(input)
    COLS = len(input[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
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
            print(count)
            if count < 4:
                res += 1
    return res

if __name__ == "__main__":
    fp = open("input4.txt", "r")
    print(main())
    fp.close()
