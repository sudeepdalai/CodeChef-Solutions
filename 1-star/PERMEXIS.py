'''
URL: https://www.codechef.com/submit/PERMEXIS

sort and compare
'''
for _ in range(int(input())):
    n = int(input())
    ip = input().split(' ')
    arr = []
    for x in ip:
        if x:
            arr.append(int(x))

    arr.sort()

    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            print('NO')
            break
    else:
        print('YES')
