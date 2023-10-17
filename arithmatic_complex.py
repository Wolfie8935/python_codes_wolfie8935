input1 = complex(input("Enter the first complex number: "))
input2 = complex(input("Enter the second complex number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(input1 + input2)
elif choice == 2:
    print(input1 - input2)
elif choice == 3:
    print(input1 * input2)
elif choice == 4:
    print(input1 / input2)
else:
    print("Invalid choice")
