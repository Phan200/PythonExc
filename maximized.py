import itertools as it


if __name__=="__main__":
    def sumModulo(nums):
        return sum(x * x for x in nums) % m
    k,m = map(int,input().split())
    a=[]
    for i in range(k):
        a.append([int(x) for x in input().split()][1:])
    # su dung itertools.product() de dua ra ca
    # to hop co the cua 3 phan tu lay tu 3 mang khac nhau
    # *a
    combination=list(it.product(*a))
    max_res=max(list(map(sumModulo,combination)))
    print(max_res)

