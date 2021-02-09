from collections import Counter
def merge_the_tools(string, k):
    # your code goes here
    res=[]
    arr=[string[i:i+k] for i in range(0,len(string),k)]
    for i in range (len(arr)):
        char= list(arr[i])
        char= Counter(char)
        for i in char:
            print(i,end="")
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)