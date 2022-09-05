from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = []
    for a in input().split(' '):
        arr.append(int(a))
    

    if n <= 2:
        print(0)
        continue
    freq = Counter(arr)
    ans = min(n-2, n-max(freq.values()))
    print(ans)
