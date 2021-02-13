from collections import Counter

if __name__ == '__main__':
    s = input()
    # Counter and sort
    res = Counter(sorted(s))
    print(res)
    for i,j in res.most_common(3):
        print(i)

