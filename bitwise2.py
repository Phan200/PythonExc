
from itertools import combinations
class listOfNumber:
    def __init__(self,n):
        self.limit=n

    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=self.limit:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

if __name__ == '__main__':

    def solution(n,k):
        list=listOfNumber(n)
        l= combinations(list,2)
        max_res=-1
        for i in l:
            res=i[0]&i[1]
            #print(res)
            if res<k and max_res < res:max_res=res
            if k-res==1:
                max_res=res
                break
        print(max_res)

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        solution(n,k)

