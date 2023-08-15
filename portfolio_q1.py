#RA2211003011296
t=int(input())
l=[]
for i in range(t):
    x,y=input().split()
    index1=0
    index2=0
    while(index1<len(x) and index2<len(y)):
        if(x[index1]==y[index2]):
            index1+=1
        index2+=1
    if index1==len(x):
        l.append("YES")
    else:
        l.append("NO")
    t=t-1
for i in l:
    print(i)