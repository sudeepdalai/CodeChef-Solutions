'''
URL: https://www.codechef.com/submit/HOWMANYMAX?tab=statement

Approach:
'01' - _ < _ > _  -->> Local Maxima
Hence append 0 at start & 1 at end => then check How many 01 are there
'''

T = int(input())

for _ in range(T):
    n = int(input())

    arr = f'0{input()}1'

    count = 0

    for i in range(1, len(arr)):
        if arr[i] == '1' and arr[i-1] == '0':
            count += 1

    print(count)
