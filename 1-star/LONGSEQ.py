'''
URL: https://www.codechef.com/submit/LONGSEQ?tab=statement

count the num of 1s and 0s in binary string: if any of them is 1 => then only Yes else No
'''
for _ in range(int(input())):

    n1, n0 = 0, 0
    num = input()

    for i in num:
        if i == '0':
            n0 += 1
        else:
            n1 += 1

    if n0 == 1 or n1 == 1:
        print('Yes')
    else:
        print('No')
