'''
URL: https://www.codechef.com/submit/BALLOON?tab=statement

'''

for _ in range(int(input())):

    n = int(input())

    arr = list(map(int, input().split(' ')))

    ans = 0

    for i in range(len(arr)):
        if arr[i] in range(1, 8):
            ans += 1

        if ans == 7:
            print(i+1)
            break
