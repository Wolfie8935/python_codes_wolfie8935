def sum_of_two_numbers(a,b):
  return a + b


def sum_of_three_numbers(a,b,c):
  return a + b + c
  
a=int(input("Enter no of numbers you want to enter:"))
if(a==2):
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2:"))
    z= sum_of_two_numbers(x,y)
    if(z>=120 and z<=320):
        print("200")
    else:
        print(z)
elif(a==3):
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2:"))
    z=int(input("Enter number 3:"))
    q= sum_of_two_numbers(x,y,z)
    if(q>=120 and q<=320):
        print("200")
    else:
        print(q)