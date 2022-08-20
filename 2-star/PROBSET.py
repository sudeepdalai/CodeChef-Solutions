'''
url: https://www.codechef.com/submit/PROBSET
'''


def test_solution(inp):
    cw = inp[0]
    sol = [int(c) for c in inp[1]]
    # print(cw, sol)
    if cw == 'correct':
        for ss in sol:
            if ss != 1:
                return 2
        return 0
    else:
        for ss in sol:
            if ss == 0:
                return 0
        return 1


for _ in range(int(input())):
    m, n = map(int, input().split(' '))
    ans = 0
    lookup = {
        0: 'FINE',
        1: 'WEAK',
        2: 'INVALID'
    }
    for test in range(m):
        ans = max(ans, test_solution(input().split(' ')))

    print(lookup[ans])
