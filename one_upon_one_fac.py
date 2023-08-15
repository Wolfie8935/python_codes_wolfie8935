def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)

def sause(x):
    sum=0
    for i in range (1,x+1):
        sum += i/fac(i)
    return sum

n=int(input("n: "))
k=sause(n)
print(k)