def checkName(s):
    if len(s)<=0 or len(s)>20: return False
    for i in s:
        if i.isupper():return False
    return True
def checkEmail(s):
    if len(s)<=0 or len(s)>50: return False
    for i in range(len(s)):
        if s[i].isnumeric() or s[i].isupper(): return False
        if s[i]=='@':
            c= slice(i,len(s),1)
            s1=s[c]
            if s1 != "@gmail.com":return False
            return True



N = int(input())
db=[]
for N_itr in range(N):
    id = input().split()
    inf={}
    if checkName(id[0]) and checkEmail(id[1]):
        inf['name']=id[0]
        inf['email'] = id[1]
        db.append(inf)
res= sorted(db,key=lambda i: i['name'])
for i in res:
    print(i['name'])
