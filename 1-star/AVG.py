'''
URL: https://www.codechef.com/submit/AVG?tab=statement

Self Explanatory
'''

T = int(input())

for _ in range(T):
    N, K, V = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    cur_sum = sum(arr)

    total = (N+K)*V

    rem = total - cur_sum

    if rem % K == 0 and rem / K > 0:
        print(rem // K)
    else:
        print(-1)
