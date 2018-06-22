import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap=0
for i in range(n):

    for j in range(n-1):
        if a[j] > a[j + 1]: 
            a[j], a[j + 1]=a[j+1],a[j]
            swap+=1

    if swap==0:
        break
        
print('Array is sorted in',swap,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[n-1])
