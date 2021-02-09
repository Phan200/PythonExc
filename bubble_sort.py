#!/bin/python3

def bubble_sort(n,l):
    swap = []
    count=0
    for k in range(0,n):
        for i in range (0,n-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]= l[i+1],l[i]
                count+=1
    swap.append(count)
    swap.append(l[0])
    swap.append(l[n-1])
    return swap


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
res=bubble_sort(n,a)
print("Array is sorted in ",res[0],"swaps.")
print("First Elements:",res[1])
print("Last Elements: ",res[2])
