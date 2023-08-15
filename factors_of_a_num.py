num=int(input("Enter input: "))
factors=[]
for i in range (1,num+1):
    if num%1==0:
        factors.append(i)
        
print("The factors of ",num,"are:\n",factors,sep="")