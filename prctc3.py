x=int(input())
k=[]
for i in range (0,x):
    r=int(input("",sep=" "))
    k.append(r)

t=tuple(k)
print(t)
print(hash(t))