'''
url: https://www.codechef.com/submit/NAME1

'''
# cook your dish here
for _ in range(int(input())):
    A, B = input().split(' ')
    C = ''
    for _c in range(int(input())):
        C += input()

    pf = [0] * 26
    cf = [0] * 26

    for ch in A:
        pf[ord(ch)-ord('a')] += 1

    for ch in B:
        pf[ord(ch)-ord('a')] += 1

    for ch in C:
        cf[ord(ch)-ord('a')] += 1

    for i in range(len(cf)):
        if cf[i] > pf[i]:
            print('NO')
            break
    else:
        print('YES')
