from collections import Counter
if __name__ =="__main__":
    l=[]
    t=int(input())
    for _ in range(t):
        s=input()
        l.append(s)
    count = Counter(l)
    res=0
    for i in count:
        res+=1
    print(res)
    for i in count:
        print(count[i], end=" ")