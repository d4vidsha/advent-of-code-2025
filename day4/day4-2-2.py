def print_list(lst):
    for l in lst:
        print(l)

def main():
    res = 0
    input = fp.read()
    input = input.split("\n")[:-1]
    input = [list(s) for s in input]
    # print_list(input)
    ROWS = len(input)
    COLS = len(input[0])
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    grid = [[0] * COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            for (dr, dc) in dirs:
                if 0 <= r+dr and r+dr < ROWS and 0 <= c+dc and c+dc < COLS and input[r][c] == "@":
                    grid[r+dr][c+dc] += 1
    print_list(grid)
    while True:
        diff = 0
        for r in range(ROWS):
            for c in range(COLS):
                if input[r][c] == "@" and grid[r][c] < 4:
                    input[r][c] = "."
                    for (dr, dc) in dirs:
                        if 0 <= r+dr and r+dr < ROWS and 0 <= c+dc and c+dc < COLS:
                            grid[r+dr][c+dc] -= 1
                    diff += 1
        if diff == 0:
            return res
        res += diff

if __name__ == "__main__":
    fp = open("input4.txt", "r")
    print(main())
    fp.close()

