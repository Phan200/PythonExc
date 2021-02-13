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

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(k - 1 if (k - 1) | k <= n else k - 2)


