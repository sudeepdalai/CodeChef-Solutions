# cook your dish here
for _ in range(int(input())):
    n, b, a = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    bob, alice, both = 0, 0, 0
    
    for i in range(len(arr)):
        if arr[i] % b == 0 and arr[i] % a == 0:
            both += 1
        elif arr[i] % b == 0:
            bob += 1
        elif arr[i] % a == 0:
            alice += 1
    
    if both > 0:
        bob += 1
    
    if bob > alice:
        print('BOB')
    else:
        print('ALICE')
        
    
    
