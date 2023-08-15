#RA2211003011296
temp=0
x=[]
res=[]
t=int(input())
for i in range(0,t):
    x=[]
    n=int(input())
    x=list(input().split(" "))
    a=max(x)
    for j in x:
        if a==j:
            temp+=1
    res.append(temp)
    temp=0
for i in res:
    print(i)