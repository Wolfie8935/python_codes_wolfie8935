a=input("Enter word: ")
x=len(a)
if x%2==0:
    for i in range (0,x,2):
        print(a[i],a[i+1])
else:
    for i in range (0,x-1,2):
        print(a[i],a[i+1])