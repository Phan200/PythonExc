# Enter your code here. Read input from STDIN. Print output to
from collections import Counter

n = int(input())
for i in range(n):
    id = input()
    if(len(id)!=10):
        print("Invalid")
    else:
        res = Counter(sorted(id))
        count_letter = count_number = 0

        for letter, freq in res.most_common(len(res)):
            if freq > 1 : break
            if letter.isnumeric():
                count_number += 1
            if letter.isupper():
                count_letter+=1

        if count_number>=3 and count_letter>=2: print("Valid")
        else: print("Invalid")


