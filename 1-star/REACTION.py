'''
URL: https://www.codechef.com/submit/REACTION?tab=statement
'''
T = int(input())

for _ in range(T):
    ROWS, COLS = map(int, input().split(' '))
    grid = []
    for r in range(ROWS):
        rr = map(int, input().split(' '))
        grid.append(list(rr))

    stable = True

    for r in range(ROWS):
        for c in range(COLS):
            n_adj = 0
            if r+1 in range(ROWS):
                n_adj += 1
            if r-1 in range(ROWS):
                n_adj += 1

            if c + 1 in range(COLS):
                n_adj += 1

            if c-1 in range(COLS):
                n_adj += 1

            if grid[r][c] >= n_adj:
                stable = False
                break

    if stable:
        print('Stable')
    else:
        print('Unstable')
