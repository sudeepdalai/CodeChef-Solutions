'''
URL: https://www.codechef.com/submit/SC31?tab=statement

use bitwise XOR for each of the elements
'''


for _ in range(int(input())):
    N = int(input())
    arr = []
    for __ in range(N):
        cur = [int(i) for i in input()]
        arr.append(cur)

    ans = arr[0]

    for i in range(1, len(arr)):

        for j in range(len(arr[i])):
            ans[j] = ans[j] ^ arr[i][j]

    count = 0

    for i in ans:
        if i == 1:
            count += 1

    print(count)
